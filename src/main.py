import os
import subprocess
import sys

from PySide6.QtCore import QDir
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog

from settings import SettingsDialog  # Import the SettingsDialog class
from ui.BAPD_Main_GUI import Ui_MainWindow

USER_PROFILE_PATH = os.environ['USERPROFILE']
DEFAULT_PROJECT_PATH = os.path.join(USER_PROFILE_PATH, "BAPD", "Projects", "Astrocade_Program")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Set default project path
        self.current_project_path = DEFAULT_PROJECT_PATH
        self.fileNameLabel.setText("Astrocade_Program")

        # Connect button signals
        self.selectProjectButton.clicked.connect(self.select_project_directory)
        self.editSourceButton.clicked.connect(self.edit_source)
        self.viewListingButton.clicked.connect(self.view_listing)
        self.compileButton.clicked.connect(self.compile)
        self.runCurrentButton.clicked.connect(self.run_current_program)
        self.runStandardMameButton.clicked.connect(self.run_standard_mame)
        self.clearScreenButton.clicked.connect(self.clear_output_screen)
        self.openProjectFolderButton.clicked.connect(self.open_project_folder)
        self.versionPushButton.clicked.connect(self.print_version)

        # Enable Buttons Initially
        self.openProjectFolderButton.setEnabled(True)
        self.editSourceButton.setEnabled(True)
        self.viewListingButton.setEnabled(True)
        self.compileButton.setEnabled(True)
        self.runCurrentButton.setEnabled(True)

        settings_action = QAction("Settings", self)
        settings_action.triggered.connect(self.open_settings_dialog)
        self.menuSettings.addAction(settings_action)

        # Set the icon for the Settings menu item
        icon = QIcon(":/icons/icons/gear.png")
        settings_action.setIcon(icon)

    def open_settings_dialog(self):
        settings_dialog = SettingsDialog(self)  # Create an instance of the SettingsDialog
        settings_dialog.exec()  # Show the settings dialog as a modal window
        print("Settings dialog closed")

    def edit_source(self):
        print("Edit Source button clicked")

    def view_listing(self):
        print("View Listing button clicked")

    def run_standard_mame(self):
        print("Run Standard MAME button clicked")

    def print_version(self):
        print("Version Information")

    def open_project_folder(self):
        if self.current_project_path:
            os.startfile(self.current_project_path)

    def select_project_directory(self):
        start_dir = os.path.join(USER_PROFILE_PATH, "BAPD", "Projects")
        directory = QFileDialog.getExistingDirectory(
            self,
            "Select Astrocade Project Directory",
            QDir.toNativeSeparators(start_dir)
        )
        directory = os.path.normpath(directory)

        # Since the normpath function returns "." if it tries to normalize an
        # empty variable, we have to consider "." as path not chosen.
        if directory and directory != ".":
            print("Entered if directory", directory)
            self.current_project_path = directory
            # Enable Buttons

            self.fileNameLabel.setText(os.path.basename(directory))

            # Enable Buttons

            self.openProjectFolderButton.setEnabled(True)
            self.editSourceButton.setEnabled(True)
            self.viewListingButton.setEnabled(True)
            self.compileButton.setEnabled(True)
            self.runCurrentButton.setEnabled(True)

        else:
            # Dialog was canceled or invalid selection
            print("No directory selected or invalid directory.")
            return

    def compile(self):
        project_name = os.path.basename(self.current_project_path)
        source_file = os.path.join(self.current_project_path, f"{project_name}.asm")
        output_file = os.path.join(self.current_project_path, f"{project_name}.bin")
        listing_file = os.path.join(self.current_project_path, f"{project_name}.lst")

        os.chdir(self.current_project_path)

        zmac_path = os.path.join(USER_PROFILE_PATH, "BAPD", "_Programs", "Zmac", "zmac.exe")
        zmac_command = [zmac_path, "-i", "-m", "-o", output_file, "-x", listing_file, source_file]

        try:
            completed_process = subprocess.run(zmac_command, capture_output=True, text=True)
            if completed_process.returncode == 0:
                self.plainTextEdit.appendPlainText("Zmac Output:\nCompilation Successful!")
            else:
                self.plainTextEdit.appendPlainText(f"Zmac Error:\n{completed_process.stderr}")
        except FileNotFoundError:
            self.plainTextEdit.appendPlainText("Error: Zmac.exe not found.")

    def clear_output_screen(self):
        self.plainTextEdit.clear()
        self.plainTextEdit.appendPlainText("[Screen Cleared]")

    def run_current_program(self):
        project_name = os.path.basename(self.current_project_path)
        bin_file_path = os.path.normpath(os.path.join(self.current_project_path, f"{project_name}.bin"))

        mame_path = os.path.join(USER_PROFILE_PATH, "BAPD", "_Programs", "MAME", "mame64.exe")
        mame_dir = os.path.dirname(mame_path)

        mame_command = [
            mame_path,
            "astrocde",
            "-cart", bin_file_path,
            "-nofilter",
            "-window"
        ]

        if self.mameDebugCheckBox.isChecked():
            mame_command.append("-debug")

        os.chdir(mame_dir)
        subprocess.Popen(mame_command)
        self.plainTextEdit.appendPlainText("MAME has been launched.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
