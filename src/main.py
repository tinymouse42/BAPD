# main.py

# *****************************************************************************
# Imports:
# *****************************************************************************

# Standard Library Imports
import os
import subprocess
import sys

# Third-party library imports
from PySide6.QtWidgets import QApplication, QMainWindow

from config.config import DEFAULT_MAME_PATH, DIRECTORY_TREE, TOML_FULL_PATH, DEFAULT_ZMAC_PATH
from settings import SettingsDialog
from src.program_initializer import ProgramInitializer
from ui.BAPD_Main_GUI import Ui_MainWindow
from src.file_management import FileManager


# *****************************************************************************
# MainWindow is the name of OUR class defining our program class.
#   =>  Inherits from PS6 QMainWindow provides a pre-built framework for
#       the main window of your application.
#   =>  Inherits from Ui_MainWindow, which is the name of the OUR class
#       in a separate file called BAPD_Main_GUI which contains the GUI code
#       created by Designer.
# *****************************************************************************

class MainWindow(QMainWindow, Ui_MainWindow):  # QMainWindow <- PS6
    # ==========================================================================
    # Initialization section. This is run when MainWindow is instantiated.
    # ==========================================================================
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # =====================================================================
        # Initialize the program environment
        # =====================================================================
        program_initializer = ProgramInitializer(DIRECTORY_TREE)
        program_initializer.create_directory_structure()
        program_initializer.validate_and_normalize_toml_settings()

        # Load settings from the TOML file
        self.settings = FileManager.read_toml(TOML_FULL_PATH)

        # Initialize attributes from the loaded settings
        self.current_project_path = self.settings.get("project", {}).get("path", None)

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
        self.clearScreenButton.clicked.connect(self.clear_output_screen)
        self.openProjectFolderButton.clicked.connect(self.open_project_folder)
        self.versionPushButton.clicked.connect(self.print_version)
        self.settingsButton.clicked.connect(self.open_settings_dialog)

    # =====================================================================
    # Creates an instance of the SettingsDialog which is the class
    # in the settings.py file. How this is supposed to work is when
    # you save or cancel the by hitting OK, Apply or Cancel, the
    # setting dialog should return a signal which can be acted upon
    # in the main code, which would most likely be to save the settings
    # in the TOML file.
    # =====================================================================
    def open_settings_dialog(self):
        settings_dialog = SettingsDialog(self)
        settings_dialog.accepted.connect(self.handle_settings_accepted)
        settings_dialog.rejected.connect(self.handle_settings_rejected)
        settings_dialog.exec()

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
        self.plainTextEdit.appendPlainText("Select Project Directory (not yet implemented)")

    # =====================================================================
    # Compiles the current Astrocade project using Zmac.
    # =====================================================================
    def compile(self):
        """Compiles the current Astrocade project using Zmac."""

        # Re-read settings to get the latest project path
        self.settings = FileManager.read_toml(TOML_FULL_PATH)
        self.current_project_path = self.settings.get("project", {}).get("path", "")

        if not self.current_project_path:
            self.plainTextEdit.appendPlainText("No project selected.")
            return

        # Get ZMAC path from settings, with better error handling
        zmac_path = self.settings.get("zmac", {}).get("path", DEFAULT_ZMAC_PATH)
        if not os.path.isfile(zmac_path):
            self.plainTextEdit.appendPlainText(
                f"Zmac executable not found at '{zmac_path}'. Please check your settings."
            )
            return

        try:
            # Change to the project directory
            os.chdir(self.current_project_path)
        except FileNotFoundError:
            self.plainTextEdit.appendPlainText(f"Project directory not found: {self.current_project_path}")
            return

        # Build Zmac command based on TOML settings
        project_name = os.path.basename(self.current_project_path)
        zmac_command = [
            zmac_path,
            "-o",
            f"{project_name}.bin",  # No need for os.path.join
            "-x",
            f"{project_name}.lst",  # No need for os.path.join
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
        zmac_command.append(f"{project_name}.asm")  # No need for os.path.join

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
    def run_current_program(self):
        project_name = os.path.basename(self.current_project_path)
        bin_file_path = os.path.normpath(os.path.join(self.current_project_path, f"{project_name}.bin"))

        # Get MAME path and settings from TOML
        mame_settings = self.settings.get("mame", {})
        mame_path = mame_settings.get("path", DEFAULT_MAME_PATH)
        mame_dir = os.path.dirname(mame_path)

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

        os.chdir(mame_dir)
        subprocess.Popen(mame_command)
        self.plainTextEdit.appendPlainText("MAME has been launched.")

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
        if self.current_project_path:
            os.startfile(self.current_project_path)

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
