# File: main.py

import os
import subprocess
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import QDir

from BAPD_GUI import Ui_MainWindow  # Assuming your Qt Designer file remains the same

USER_PROFILE_PATH = os.environ['USERPROFILE']


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect button signals
        self.ui.selectProjectButton.clicked.connect(self.select_project_directory)
        self.ui.editSourceButton.clicked.connect(self.print_button_label)
        self.ui.viewListingButton.clicked.connect(self.print_button_label)
        self.ui.compileButton.clicked.connect(self.compile)
        self.ui.runCurrentButton.clicked.connect(self.run_current_program)
        self.ui.runStandardMameButton.clicked.connect(self.print_button_label)
        self.ui.clearScreenButton.clicked.connect(self.clear_output_screen)  # Connect clear button
        self.ui.openProjectFolderButton.clicked.connect(self.open_project_folder)
        self.ui.versionPushButton.clicked.connect(self.print_version)

        self.current_project_path = None
        self.ui.fileNameLabel.setText("No Project Selected")

        # Disable Buttons Initially
        self.ui.openProjectFolderButton.setEnabled(False)
        self.ui.editSourceButton.setEnabled(False)
        self.ui.viewListingButton.setEnabled(False)
        self.ui.compileButton.setEnabled(False)
        self.ui.runCurrentButton.setEnabled(False)

    def print_button_label(self):
        button = self.sender()
        print(button.text())

    def print_version(self):
        print("Version Information")

    def open_project_folder(self):
        # Project must already be selected or option in GUI disabled
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
        if directory:
            self.current_project_path = directory
            self.ui.fileNameLabel.setText(os.path.basename(directory))

            # Enable Buttons
            self.ui.openProjectFolderButton.setEnabled(True)
            self.ui.editSourceButton.setEnabled(True)
            self.ui.viewListingButton.setEnabled(True)
            self.ui.compileButton.setEnabled(True)
            self.ui.runCurrentButton.setEnabled(True)
        else:
            # No directory selected
            self.current_project_path = None
            self.ui.fileNameLabel.setText("No Project Selected")

            # Disable Buttons
            self.ui.openProjectFolderButton.setEnabled(False)
            self.ui.editSourceButton.setEnabled(False)
            self.ui.viewListingButton.setEnabled(False)
            self.ui.compileButton.setEnabled(False)
            self.ui.runCurrentButton.setEnabled(False)

    def compile(self):

        # Construct paths and filenames
        project_name = os.path.basename(self.current_project_path)
        source_file = os.path.join(self.current_project_path, f"{project_name}.asm")
        output_file = os.path.join(self.current_project_path, f"{project_name}.bin")
        listing_file = os.path.join(self.current_project_path, f"{project_name}.lst")

        # Change working directory to project path for Zmac
        os.chdir(self.current_project_path)

        # Build the Zmac command
        zmac_path = os.path.join(USER_PROFILE_PATH, "BAPD", "_Programs", "Zmac", "zmac.exe")
        zmac_command = [zmac_path, "-i", "-m", "-o", output_file, "-x", listing_file, source_file]

        # Execute Zmac
        try:
            completed_process = subprocess.run(zmac_command, capture_output=True, text=True)
            if completed_process.returncode == 0:
                self.ui.plainTextEdit.appendPlainText("Zmac Output:\nCompilation Successful!")
            else:
                self.ui.plainTextEdit.appendPlainText(f"Zmac Error:\n{completed_process.stderr}")
        except FileNotFoundError:
            self.ui.plainTextEdit.appendPlainText("Error: Zmac.exe not found.")

    def clear_output_screen(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.appendPlainText("[Screen Cleared]")

    def run_current_program(self):
        # Get the project name
        project_name = os.path.basename(self.current_project_path)

        # Get the path to the current project's .bin file
        bin_file_path = os.path.normpath(os.path.join(self.current_project_path, f"{project_name}.bin"))

        # Build the path to the MAME executable
        mame_path = os.path.join(USER_PROFILE_PATH, "BAPD", "_Programs", "MAME", "mame64.exe")
        mame_dir = os.path.dirname(mame_path)  # Get the directory containing MAME

        # Build the MAME command
        mame_command = [
            mame_path,
            "astrocde",
            "-cart", bin_file_path,
            "-nofilter",
            "-window"

        ]
        # Add -debug if the checkbox is checked
        if self.ui.mameDebugCheckBox.isChecked():
            mame_command.append("-debug")

        # Change working directory to the MAME directory
        os.chdir(mame_dir)

        # Launch MAME as a separate process
        subprocess.Popen(mame_command)

        # Optional: Display a message indicating MAME has launched
        self.ui.plainTextEdit.appendPlainText("MAME has been launched.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
