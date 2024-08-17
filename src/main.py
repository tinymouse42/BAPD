# main.py


import os
import subprocess
import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

from config.config import (
    DEFAULT_MAME_PATH,
    DIRECTORY_TREE,
    TOML_FULL_PATH,
    DEFAULT_TOML_SETTINGS, DEFAULT_PROJECT_PATH,
)
from src.program_settings import SettingsDialog
from src.file_management import FileManager
from src.program_initializer import ProgramInitializer
from src.project_selection import ProjectSelectionManager
from ui.BAPD_Main_GUI import Ui_MainWindow


# **************************************************************************
# MainWindow Class - This is where all the magic happens. Usually dark magic.
# **************************************************************************
class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Verifies the physical directory tree structure and fills in missing items.
        # if it doesn't exist it creates it from the DIRECTORY_TREE constant
        ProgramInitializer(DIRECTORY_TREE).create_directory_structure()

        # Validate and normalize TOML settings. After return there is a valid TOML in place.
        self.settings: dict = ProgramInitializer(DEFAULT_TOML_SETTINGS).validate_and_normalize_toml_settings(self)

        # Retrieves the path to the current project directory from user settings.
        project_path = self.settings.get("project", {}).get("path", "")
        self.current_project_path = os.path.realpath(project_path)

        # Retrieves the source file name in the current project directory from user settings.
        # source_file_name = self.settings.get("project", {}).get("source_file_name", "")

        # =====================================================================
        # This is a standard way to connect the button signals to a function.
        # In this case, the locations are pulled from the Ui_MainWindow inherited
        # class which hold the GUI code.
        # =====================================================================
        self.selectProjectButton.clicked.connect(self.select_project_directory)
        self.editSourceButton.clicked.connect(self.edit_source)
        self.viewListingButton.clicked.connect(self.view_listing)
        self.compileButton.clicked.connect(self.compile)
        self.runCurrentButton.clicked.connect(self.run_current_program)
        self.runStandardMameButton.clicked.connect(self.run_standard_mame)
        self.clearScreenButton.clicked.connect(self.plainTextEdit.clear)
        self.openProjectFolderButton.clicked.connect(self.open_project_folder)
        self.settingsButton.clicked.connect(self.open_settings_dialog)
        self.mameDebugCheckBox.stateChanged.connect(self._debug_update)

    # =====================================================================
    # Creates an instance of the SettingsDialog which is the class
    # in the program_settings.py file. How this is supposed to work is when
    # you save or cancel the by hitting OK, Apply or Cancel, the
    # setting dialog should return a signal which can be acted upon
    # in the main code, which would most likely be to save the settings
    # in the TOML file.
    # =====================================================================
    def open_settings_dialog(self):
        settings_dialog = SettingsDialog(self, self.settings)  # Pass settings to the dialog
        if settings_dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            self.settings = settings_dialog.settings  # Update settings from dialog
            FileManager.write_toml(TOML_FULL_PATH, self.settings)  # Save settings
            self.plainTextEdit.appendPlainText("Settings saved successfully.")
        else:
            self.plainTextEdit.appendPlainText("Settings dialog was canceled.")

    # =====================================================================
    # If the OK or Apply button is pressed in the settings dialog, then do
    # the following function. Right now it is stub code. ???
    # =====================================================================
    def handle_settings_accepted(self):
        self.plainTextEdit.appendPlainText("Settings Accepted (not yet implemented.")

    # =====================================================================
    # If the cancel button is pressed in the settings dialog, then do
    # the following function. Right now it is stub code. ???
    # =====================================================================
    def handle_settings_rejected(self):
        self.plainTextEdit.appendPlainText("Settings dialog was canceled.")

    # =====================================================================
    # Opens a dialog to let the user select an Astrocade project directory.
    # =====================================================================
    def select_project_directory(self):
        # Create an instance of the project selection dialog class
        dialog = ProjectSelectionManager(self)

        # If either Apply or Okay is pressed, then this code executes.
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            self.current_project_path = dialog.selected_project_path
            self.fileNameLabel.setText(os.path.basename(self.current_project_path))

    def compile(self):
        """Compiles the current Astrocade project using Zmac."""

        # Re-read settings to get the latest project path
        self.settings = FileManager.read_toml(TOML_FULL_PATH)

        self.current_project_path = self.settings.get("project", {}).get("path", "")

        if not self.current_project_path:
            self.plainTextEdit.appendPlainText("No project selected.")
            return

        # Get ZMAC path from settings, with better error handling
        zmac_path = self.settings.get("zmac", {}).get("path", str(DEFAULT_PROJECT_PATH).replace("\\", "/"))

        try:
            # Change to the project directory using os.chdir
            project_dir = self.current_project_path
            os.chdir(project_dir)  # Make sure to change to the directory
        except FileNotFoundError:
            self.plainTextEdit.appendPlainText(f"Project directory not found: {self.current_project_path}")
            return

        # Build Zmac command based on TOML settings
        project_name = os.path.basename(self.current_project_path)
        output_bin_path = os.path.join(project_dir, f"{project_name}.bin")
        output_lst_path = os.path.join(project_dir, f"{project_name}.lst")

        zmac_command = [
            zmac_path,
            "-o",
            output_bin_path,
            "-x",
            output_lst_path,
        ]

        # Add options based on TOML settings using match-case
        match self.settings.get("zmac", {}):
            case {"expand_macros": True}:
                zmac_command.append("-m")
            case {"expand_include_files": False}:
                zmac_command.append("-i")
            case {"expand_if": True}:
                zmac_command.append("-f")
            case {"omit_symbol_table": False}:
                zmac_command.append("-s")
            case {"allow_8080_instructions": False}:
                zmac_command.append("-z")
            case {"output_hex_file": True}:
                zmac_command.append("-o")
                zmac_command.append(f"{project_name}.hex")

        # Source file (always included)
        source_file_name = self.settings.get("project", {}).get("source_file_name", f"{project_name}.asm")
        source_file_path = os.path.join(self.current_project_path, source_file_name)
        zmac_command.append(source_file_path)  # Append the full source file path

        self.plainTextEdit.appendPlainText(f"ZMAC\nCompiling {source_file_name}")

        try:
            completed_process = subprocess.run(zmac_command, capture_output=True, text=True)
            if completed_process.returncode == 0:
                self.plainTextEdit.appendPlainText("Compilation successful!\n")
            else:
                error_message = completed_process.stderr.strip()  # Remove leading/trailing whitespace
                project_name = os.path.basename(self.current_project_path)
                error_message = error_message.replace(f"{self.current_project_path}\\",
                                                      "")  # Remove path using project_name
                error_message = error_message.replace(f"{self.current_project_path}/",
                                                      "")  # Remove path using project_name
                self.plainTextEdit.appendPlainText(f"Zmac Compilation Error:\n{error_message}\n")
        except FileNotFoundError as e:
            self.plainTextEdit.appendPlainText(f"Error running Zmac: {e}")

    # =====================================================================
    # Runs the currently compiled program with some standard options and
    # any user specified options from the settings menu.
    # =====================================================================

    def run_current_program(self):

        # subprocess.Popen(mame_command, cwd=mame_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        project_name = os.path.basename(self.current_project_path)
        bin_file_path = os.path.join(self.current_project_path, f"{project_name}.bin")

        # Get MAME path and settings from TOML
        mame_settings = self.settings.get("mame", {})
        mame_path = mame_settings.get("path", DEFAULT_MAME_PATH)
        mame_dir = os.path.dirname(os.path.abspath(mame_path))  # Get parent directory of MAME path

        # Build MAME command based on TOML settings
        mame_command = [mame_path]

        # Add system flag based on TOML settings
        system_flags = {
            "bally_pro_arcade": "astrocde",
            "bally_home_library_computer": "astrocdl",
            "bally_computer_system": "astrocdw",
        }
        for flag, system in system_flags.items():
            if mame_settings.get(flag, False):
                mame_command.append(system)
                break

        mame_command.extend(["-cart", bin_file_path, "-filter"])

        # Add optional flags based on TOML settings
        optional_flags = {
            "debug_mode": "-debug",
            "window_mode": "-window",
            "skip_game_info": "-skip_gameinfo",
        }
        for flag, arg in optional_flags.items():
            if mame_settings.get(flag, False):
                mame_command.append(arg)

        FileManager.write_toml(TOML_FULL_PATH, self.settings)  # Save settings

        # Redirect MAME's standard output and error to null
        subprocess.Popen(mame_command, cwd=mame_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        self.plainTextEdit.appendPlainText("MAME has been launched.")

    # =====================================================================
    # This handles the debug checkbox on the main GUI.
    # =====================================================================
    def _debug_update(self):
        # Update the debug mode setting based on the checkbox
        self.settings["mame"]["debug_mode"] = self.mameDebugCheckBox.isChecked()
        FileManager.write_toml(TOML_FULL_PATH, self.settings)

    # =====================================================================
    # Opens the source code using the default editor
    # =====================================================================
    def edit_source(self):
        # Step 1: Retrieve the path to PSPad.exe
        user_profile_dir = os.environ.get('USERPROFILE')
        pspad_path = os.path.join(user_profile_dir, "BAPD", "Programs", "PSPad", "PSPad.exe")

        # Step 2: Determine the .asm file path of the current project
        project_path = self.settings["project"]["path"]
        asm_file_name = self.settings["project"]["source_file_name"]
        asm_file_path = os.path.join(project_path, asm_file_name)

        # Step 3: Construct the command to open the .asm file in PSPad
        command = [pspad_path, asm_file_path]

        # Step 4: Execute the command without blocking
        subprocess.Popen(command)

        self.plainTextEdit.appendPlainText(f"Viewing Source file: {asm_file_name}\n")

    # =====================================================================
    # Opens the listing file using PSPad.
    # =====================================================================
    def view_listing(self):
        # Step 1: Retrieve the path to PSPad.exe
        user_profile_dir = os.environ.get('USERPROFILE')
        pspad_path = os.path.join(user_profile_dir, "BAPD", "Programs", "PSPad", "PSPad.exe")

        # Step 2: Determine the .lst file path of the current project
        project_path = self.settings["project"]["path"]
        lst_file_name = self.settings["project"]["source_file_name"].replace(".asm", ".lst")
        lst_file_path = os.path.join(project_path, lst_file_name)

        # Step 3: Construct the command to open the .lst file in PSPad
        command = [pspad_path, lst_file_path]

        # Step 4: Execute the command without blocking
        subprocess.Popen(command)

        # Log the action (optional)
        self.plainTextEdit.appendPlainText(f"Viewing listing file: {lst_file_name}\n")

    # =====================================================================
    # Runs the standard version of MAME without regard to project.
    # =====================================================================
    def run_standard_mame(self):

        """
        Runs the standard version of MAME without regard to the project.
        """
        # Get MAME path from settings
        mame_path = self.settings.get("mame", {}).get("path", DEFAULT_MAME_PATH)

        if not mame_path or not os.path.exists(mame_path):
            self.plainTextEdit.appendPlainText("MAME path is not set or does not exist in settings.")
            return

        # Build the MAME command
        mame_command = [mame_path]
        mame_dir = os.path.dirname(os.path.abspath(mame_path))

        # Example: Add default system flag (e.g., 'astrocde' for Bally Professional Arcade)
        # mame_command.append("astrocde")

        # Optional: Add other default flags if necessary (e.g., window mode)
        mame_command.append("-window")

        # Log the command being run for debugging purposes
        self.plainTextEdit.appendPlainText(f"Running standard MAME command: {' '.join(mame_command)}")

        try:
            # Run the MAME command
            subprocess.Popen(mame_command, cwd=mame_dir)
            self.plainTextEdit.appendPlainText("Standard MAME has been launched.")
        except Exception as e:
            self.plainTextEdit.appendPlainText(f"Failed to run standard MAME: {e}")

    # =====================================================================
    # Opens current project folder in Windows Explorer file manager.
    # =====================================================================
    def open_project_folder(self):
        project_dir = os.path.abspath(self.current_project_path)
        if os.path.isdir(project_dir):  # Check if it's a directory
            os.startfile(project_dir)
        else:
            # Handle the case where the path is not a directory
            print(f"Error: {project_dir} is not a valid directory.")

    # =====================================================================
    # Clears the output window. Self explanatory.
    # =====================================================================
    def clear_output_screen(self):
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText("[Screen Cleared]")


# *****************************************************************************
# Main program loop.
# *****************************************************************************
if __name__ == "__main__":
    app = QApplication(sys.argv)  # app is part of PySide6 - Initializes whole program?
    window = MainWindow()  # window: Creates object for class above
    window.show()  # show is a PySid6 method. How did it get into our class?
    sys.exit(app.exec())  # Explain this?
