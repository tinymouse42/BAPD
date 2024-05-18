# main.py
import os
import subprocess
import sys

from PySide6.QtCore import QDir
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog

from settings import SettingsDialog, load_toml_settings
from ui.BAPD_Main_GUI import Ui_MainWindow

USER_PROFILE_PATH = os.environ['USERPROFILE']
DEFAULT_PROJECT_PATH = os.path.join(USER_PROFILE_PATH, "BAPD", "Projects", "Astrocade_Program")


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.settings = load_toml_settings()

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
        self.runStandardMameButton.setEnabled(True)

        settings_action = QAction("Settings", self)
        settings_action.triggered.connect(self.open_settings_dialog)
        self.menuSettings.addAction(settings_action)

        # Set the icon for the Settings menu item
        icon = QIcon(":/icons/icons/gear.png")
        settings_action.setIcon(icon)

    def open_settings_dialog(self):
        """Opens the settings dialog."""
        settings_dialog = SettingsDialog(self)
        settings_dialog.accepted.connect(self.handle_settings_accepted)
        settings_dialog.rejected.connect(self.handle_settings_rejected)
        settings_dialog.exec_()

    def handle_settings_accepted(self):
        """Handles the accepted signal from the settings dialog."""
        self.settings = load_toml_settings()  # Reload settings after accepting changes

        # Check if the new ZMAC path is valid (add this error handling)
        zmac_path = self.settings.get("zmac", {}).get("path", "")
        if not zmac_path or not os.path.isfile(zmac_path):
            self.plainTextEdit.appendPlainText("Zmac path is not set or invalid. Please check your settings.")
        else:
            self.plainTextEdit.appendPlainText("ZMAC path is valid.")

    def handle_settings_rejected(self):
        """Handles the rejected signal from the settings dialog."""
        self.plainTextEdit.appendPlainText("Settings dialog was canceled.")

    def select_project_directory(self):
        """Opens a dialog to let the user select an Astrocade project directory."""
        start_dir = os.path.join(USER_PROFILE_PATH, "BAPD", "Projects")
        directory = QFileDialog.getExistingDirectory(
            self,
            "Select Astrocade Project Directory",
            QDir.toNativeSeparators(start_dir)
        )
        directory = os.path.normpath(directory)

        if directory and directory != ".":
            self.current_project_path = directory
            self.fileNameLabel.setText(os.path.basename(directory))

            # Enable Buttons (New code)
            self.openProjectFolderButton.setEnabled(True)
            self.editSourceButton.setEnabled(True)
            self.viewListingButton.setEnabled(True)
            self.compileButton.setEnabled(True)
            self.runCurrentButton.setEnabled(True)
            self.runStandardMameButton.setEnabled(True)
        else:
            # Dialog was canceled or invalid selection
            print("No directory selected or invalid directory.")

    def compile(self):
        """Compiles the current Astrocade project using Zmac."""
        if not self.current_project_path:
            self.plainTextEdit.appendPlainText("No project selected.")
            return

        project_name = os.path.basename(self.current_project_path)
        source_file = os.path.join(self.current_project_path, f"{project_name}.asm")
        output_file = os.path.join(self.current_project_path, f"{project_name}.bin")
        listing_file = os.path.join(self.current_project_path, f"{project_name}.lst")

        os.chdir(self.current_project_path)  # Change to project directory before running zmac

        zmac_path = self.settings.get("zmac", {}).get("path", "")  # Get ZMAC path from settings
        if not zmac_path or not os.path.isfile(zmac_path):
            self.plainTextEdit.appendPlainText("Zmac path is not set or invalid. Please check your settings.")
            return

        zmac_command = [zmac_path, "-i", "-m", "-o", output_file, "-x", listing_file, source_file]

        try:
            completed_process = subprocess.run(zmac_command, capture_output=True, text=True)
            if completed_process.returncode == 0:
                self.plainTextEdit.appendPlainText("Zmac Output:\nCompilation Successful!")
            else:
                self.plainTextEdit.appendPlainText(f"Zmac Error:\n{completed_process.stderr}")
        except FileNotFoundError as e:
            self.plainTextEdit.appendPlainText(f"Error running Zmac: {e}")

    def edit_source(self):
        """Opens the source file for editing (not yet implemented)."""
        # TODO: Implement the logic to open the source file in an external editor.
        self.plainTextEdit.appendPlainText("Editing source file (not yet implemented)")

    def view_listing(self):
        """Opens the listing file for viewing (not yet implemented)."""
        # TODO: Implement the logic to open the listing file.
        self.plainTextEdit.appendPlainText("Viewing listing file (not yet implemented)")

    def run_standard_mame(self):
        """Runs MAME with default settings (not yet implemented)."""
        # TODO: Implement the logic to launch MAME with default settings.
        self.plainTextEdit.appendPlainText("Running standard MAME (not yet implemented)")

    def open_project_folder(self):
        if self.current_project_path:
            os.startfile(self.current_project_path)

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

    def print_version(self):
        """Prints the version information of BAPD to the plain text edit area."""
        # TODO: Fetch actual version information (e.g., from a version file or package metadata)
        self.plainTextEdit.appendPlainText("BAPD Version: [Version Number Here]")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
