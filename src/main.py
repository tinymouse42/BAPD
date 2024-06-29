# main.py

# *****************************************************************************
# Imports:
# *****************************************************************************

# Standard Library Imports
import os
import shutil
import subprocess
import sys
from pathlib import Path

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from config.config import (
    DEFAULT_MAME_PATH,
    DIRECTORY_TREE,
    TOML_FULL_PATH,
    DEFAULT_ZMAC_PATH,
    PROJECT_DIR, DEFAULT_SOURCE_NAME,
)

from settings import SettingsDialog
from src.file_management import FileManager
from src.program_initializer import ProgramInitializer
from ui.BAPD_Main_GUI import Ui_MainWindow
from ui.project_selection_dialog import Ui_projectSelectionDialog


# *****************************************************************************
# MainWindow is the name of OUR class defining our program class.
#   =>  Inherits from PS6 QMainWindow provides a pre-built framework for
#       the main window of your application.
#   =>  Inherits from Ui_MainWindow, which is the name of the OUR class
#       in a separate file called BAPD_Main_GUI which contains the GUI code
#       created by Designer.
# *****************************************************************************

class MainWindow(QMainWindow, Ui_MainWindow):
    # ==========================================================================
    # Initialization section. This is run when MainWindow is instantiated.
    # ==========================================================================
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ProgramInitializer(DIRECTORY_TREE).create_directory_structure()
        self.settings = ProgramInitializer(DIRECTORY_TREE).validate_and_normalize_toml_settings(self)
        self.current_project_path = self.settings.get("project", {}).get("path")

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
    # in the settings.py file. How this is supposed to work is when
    # you save or cancel the by hitting OK, Apply or Cancel, the
    # setting dialog should return a signal which can be acted upon
    # in the main code, which would most likely be to save the settings
    # in the TOML file.
    # =====================================================================
    def open_settings_dialog(self):
        settings_dialog = SettingsDialog(self, self.settings)  # Pass settings to the dialog
        if settings_dialog.exec_() == QtWidgets.QDialog.DialogCode.Accepted:
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
        # It runs the init method of this class. The self refers
        # to this instance of the main window which is passed to the
        # init function in the ProjectSelectionDialog class. In that code
        # the parameter is called main_window.
        dialog = ProjectSelectionDialog(self)

        # If either Apply or Okay is pressed, then this code executes.
        if dialog.exec() == QtWidgets.QDialog.DialogCode.Accepted:
            print(self.current_project_path)
            self.current_project_path = dialog.selected_project_path
            self.fileNameLabel.setText(os.path.basename(self.current_project_path))

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

        FileManager.write_toml(TOML_FULL_PATH, self.settings)  # Save settings
        print(mame_command)

        os.chdir(mame_dir)
        subprocess.Popen(mame_command)
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


class ProjectSelectionDialog(QtWidgets.QDialog, Ui_projectSelectionDialog):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        # Stores the reference to the main window, so it can interact with it.
        # In the main dialog, it is passed as "self".
        self.main_window = main_window

        # The list of existing projects are created and the list widget is populated
        # with the information so one can be selected.
        self.populate_project_list()

        # Nothing has been selected so far so nothing is in the selected_project_path
        self.selected_project_path = None  # Initialize selected_project_path

        # Connect signals to slots
        self.createNewProjectRadioButton.toggled.connect(self.toggle_project_selection)
        self.dialogButtonBox.accepted.connect(self.accept_selection)
        self.dialogButtonBox.rejected.connect(self.reject)

        # Trigger the toggle_project_selection method initially to set the correct state
        self.toggle_project_selection(self.createNewProjectRadioButton.isChecked())

    def populate_project_list(self):
        # Get the existing projects and display the list
        project_paths = self.get_project_directories()
        self.existingProjectsListWidget.clear()
        for project_path in project_paths:
            project_name = os.path.basename(project_path)
            self.existingProjectsListWidget.addItem(QtWidgets.QListWidgetItem(project_name))

    def get_project_directories(self):
        projects_dir = PROJECT_DIR
        project_paths = []
        for item in os.listdir(projects_dir):
            project_path = os.path.join(projects_dir, item)
            if os.path.isdir(project_path):
                project_paths.append(project_path)
        return project_paths

    # Slot to handle toggling between existing and new project selection
    def toggle_project_selection(self, checked):
        # Enable/disable the project name input field based on the radio button state
        self.projectNameLineEdit.setEnabled(checked)  # Enable if checked, disable if not checked

    def accept_selection(self):
        if self.createNewProjectRadioButton.isChecked():
            self.create_new_project()
        else:
            self.select_existing_project()

    def create_new_project(self):
        project_name = self.projectNameLineEdit.text()
        if not project_name:
            QMessageBox.warning(self, "No Project Name", "Please enter a name for the new project.")
            return

        self.create_project_directory(project_name)
        self.selected_project_path = os.path.join(PROJECT_DIR, project_name)
        self.update_main_window(project_name)
        self.update_settings()
        self.refresh_project_list()
        self.main_window.plainTextEdit.appendPlainText(f"Created new project: {project_name}")
        self.accept()

    def select_existing_project(self):
        selected_item = self.existingProjectsListWidget.currentItem()
        if selected_item:
            project_name = selected_item.text()
            self.selected_project_path = os.path.join(PROJECT_DIR, project_name)
            self.update_main_window(project_name)
            self.update_settings()
            self.accept()
        else:
            QMessageBox.warning(self, "No Project Selected", "Please select a project from the list.")

    def update_main_window(self, project_name):
        self.main_window.current_project_path = self.selected_project_path
        self.main_window.fileNameLabel.setText(project_name)

    def update_settings(self):
        self.main_window.settings["project"]["path"] = self.selected_project_path
        self.main_window.settings["project"]["source_file_name"] = DEFAULT_SOURCE_NAME
        FileManager.write_toml(TOML_FULL_PATH, self.main_window.settings)

    def refresh_project_list(self):
        self.existingProjectsListWidget.clear()
        self.populate_project_list()

    def create_project_directory(self, project_name: str):
        """Creates the project directory, Version_Archive subdirectory, and copies default files."""
        # 1. Construct project path using Path object (pathlib)
        # project_path = PROJECT_DIR / project_name
        project_path = os.path.join(PROJECT_DIR, project_name)

        # 2. Create the project directory with mkdir (parents=True, exist_ok=True)
        project_path.mkdir(parents=True, exist_ok=True)

        # 3. Create Version_Archive subdirectory
        version_archive_path = os.path.join(project_path, "Version_Archive")
        version_archive_path.mkdir(parents=True, exist_ok=True)  # Create parent directories if needed

        # 4. Define default files and archive file
        default_files = ["HVGLIB.H"]
        archive_file = (version_archive_path, f"{project_name}.asm")  # Rename based on project name

        # 5. Copy archive file first
        source_path = Path(__file__).parent / "default_files" / "Hello_World.asm"
        destination_path = archive_file[0] / archive_file[1]
        shutil.copy2(source_path, destination_path)

        # 6. Loop through each default file and copy to the directory
        for file_name in default_files:
            source_path = Path(__file__).parent / "default_files" / file_name
            destination_path = project_path / file_name
            shutil.copy2(source_path, destination_path)


# *****************************************************************************
# Main program loop.
# *****************************************************************************
if __name__ == "__main__":
    app = QApplication(sys.argv)  # app is part of PySide6 - Initializes whole program?
    window = MainWindow()  # window: Creates object for class above
    window.show()  # show is a PySid6 method. How did it get into our class?
    sys.exit(app.exec())  # Explain this?
