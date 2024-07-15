# project_selection

import os
import shutil

from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox

from config.config import (
    TOML_FULL_PATH,
    PROJECT_DIR, DEFAULT_SOURCE_NAME,
)

from src.file_management import FileManager
from ui.project_selection_dialog import Ui_projectSelectionDialog


class ProjectSelectionManager(QtWidgets.QDialog, Ui_projectSelectionDialog):
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
        # This function likely resides elsewhere (potentially moved to ProgramInitializer or a utility class)
        # ... (implementation to get project paths)
        # project_paths = self.get_project_directories()  # Placeholder

        self.existingProjectsListWidget.clear()
        for project in os.listdir(PROJECT_DIR):
            if os.path.isdir(os.path.join(PROJECT_DIR, project)):
                project_name = project
                self.existingProjectsListWidget.addItem(QtWidgets.QListWidgetItem(project_name))

    def get_project_directories(self):
        return [os.path.join(PROJECT_DIR, project) for project in os.listdir(PROJECT_DIR)
                if os.path.isdir(os.path.join(PROJECT_DIR, project))]

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
        print(project_name)
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
            self.selected_project_path = os.path.join(PROJECT_DIR, project_name)  # Use os.path.join for path joining
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
        # 1. Construct project path using os.path.join
        project_path = os.path.join(PROJECT_DIR, project_name)

        # 2. Create the project directory with os.makedirs
        os.makedirs(project_path, exist_ok=True)

        # 3. Create Version_Archive subdirectory
        version_archive_path = os.path.join(project_path, "Version_Archive")
        os.makedirs(version_archive_path, exist_ok=True)  # Create parent directories if needed

        # 4. Copy "Hello_World.asm" to Version_Archive (unchanged)
        source_archive_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "default_files", "Hello_World.asm")
        destination_archive_path = os.path.join(project_path, "Version_Archive", "Hello_World.asm")
        shutil.copy2(source_archive_path, destination_archive_path)

        # 5. Copy "Hello_World.asm" to project directory with renaming
        source_project_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "default_files", "Hello_World.asm")
        destination_project_path = os.path.join(project_path, f"{project_name}.asm")
        shutil.copy2(source_project_path, destination_project_path)

        # 6. Define default files for project directory
        project_files = ["HVGLIB.H"]

        # 7. Loop through project files and copy with project name
        for file_name in project_files:
            source_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "default_files", file_name)
            destination_path = os.path.join(project_path, file_name)
            shutil.copy2(source_path, destination_path)