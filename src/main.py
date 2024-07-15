# main.py


import os
import subprocess
import sys
from pathlib import Path

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

from config.config import (
    DEFAULT_MAME_PATH,
    DIRECTORY_TREE,
    TOML_FULL_PATH,
    DEFAULT_ZMAC_PATH, DEFAULT_TOML_SETTINGS, DEFAULT_PROJECT_PATH,
)
from program_settings import SettingsDialog
from src.file_management import FileManager
from src.program_initializer import ProgramInitializer
from src.project_selection import ProjectSelectionManager
from ui.BAPD_Main_GUI import Ui_MainWindow


# **************************************************************************
# MainWindow Class - This is where all the magic happens. Usually dark magic.
# **************************************************************************
class MainWindow(QMainWindow, Ui_MainWindow):

    # ==========================================================================
    # Temp comment: The init section is complete and using paths now
    # ==========================================================================
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Creates a physical directory structure based on DIRECTORY_TREE constant
        ProgramInitializer(DIRECTORY_TREE).create_directory_structure()

        # Validate and normalize TOML settings. After return there is a valid TOML in place.
        self.settings: dict = ProgramInitializer(DEFAULT_TOML_SETTINGS).validate_and_normalize_toml_settings(self)
        print(self.settings)
        # Retrieves the absolute path to the current project directory from user settings.
        self.current_project_path: Path = Path(self.settings.get("project", {}).get("path", "")).resolve()

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
        print("settings: ", type(self.settings))
        print("settings: ", self.settings)

        self.current_project_path = self.settings.get("project", {}).get("path", "")
        print("current_project_path: ", type(self.current_project_path))
        print("current_project_path: ", self.current_project_path)

        if not self.current_project_path:
            self.plainTextEdit.appendPlainText("No project selected.")
            return

        # Get ZMAC path from settings, with better error handling
        zmac_path = self.settings.get("zmac", {}).get("path", str(DEFAULT_PROJECT_PATH).replace("\\", "/"))
        print("zmac_path: ", zmac_path, type(zmac_path))

        try:
            # Change to the project directory using os.chdir
            project_dir = self.current_project_path
            self.plainTextEdit.appendPlainText(f"Changing directory to: {project_dir}")
            os.chdir(project_dir)  # Make sure to change to the directory
        except FileNotFoundError:
            self.plainTextEdit.appendPlainText(f"Project directory not found: {self.current_project_path}")
            return

        # Build Zmac command based on TOML settings
        project_name = os.path.basename(self.current_project_path)
        print("Project Name: ", type(project_name))
        output_bin_path = os.path.join(project_dir, f"{project_name}.bin")
        print("project_dir: ", type(project_dir))

        print("output_bin_path", type(output_bin_path))
        output_lst_path = os.path.join(project_dir, f"{project_name}.lst")
        print("output_lst_path", output_lst_path)

        zmac_command = [
            zmac_path,
            "-o",
            output_bin_path,
            "-x",
            output_lst_path,
        ]

        print("zmac_path: ", zmac_path)
        print("zmac_command: ", zmac_command)

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
        zmac_command.append(self.current_project_path)  # Use the Path object directly

        # Display the Zmac command (for debugging)
        self.plainTextEdit.appendPlainText(f"Running Zmac command: {' '.join(zmac_command)}")

        try:
            completed_process = subprocess.run(zmac_command, capture_output=True, text=True)
            if completed_process.returncode == 0:
                self.plainTextEdit.appendPlainText("Zmac Output:\nCompilation Successful!")
                # ... (potential post-compilation actions)
            else:
                self.plainTextEdit.appendPlainText(f"Zmac Error:\n{completed_process.stderr}")
        except FileNotFoundError as e:
            self.plainTextEdit.appendPlainText(f"Error running Zmac: {e}")

    # =====================================================================
    # Runs the currently compiled program with some standard options and
    # any user specified options from the settings menu.
    # =====================================================================
    import os
    import subprocess

    def run_current_program(self):
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

        # Change directory to MAME's parent directory using os
        subprocess.Popen(mame_command, cwd=mame_dir)  # Launch MAME with correct working directory

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
        self.plainTextEdit.appendPlainText("Editing source file (not yet implemented)")

    # =====================================================================
    # Opens the listing file using the default editor.
    # =====================================================================
    def view_listing(self):
        self.plainTextEdit.appendPlainText("Viewing listing file (not yet implemented)")

    # =====================================================================
    # Runs the standard version of MAME without regard to project.
    # =====================================================================
    def run_standard_mame(self):
        self.plainTextEdit.appendPlainText("Running standard MAME (not yet implemented)")

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

    # =====================================================================
    # While this is a button, I do not have a use for it at this time
    # I am thinking about making it an easter egg or some extra info
    # about zmac or both. This will probably be implemented last.
    # =====================================================================
    def print_version(self):
        self.plainTextEdit.appendPlainText("Editing source file (not yet implemented)")


# *****************************************************************************
# Main program loop.
# *****************************************************************************
if __name__ == "__main__":
    app = QApplication(sys.argv)  # app is part of PySide6 - Initializes whole program?
    window = MainWindow()  # window: Creates object for class above
    window.show()  # show is a PySid6 method. How did it get into our class?
    sys.exit(app.exec())  # Explain this?
