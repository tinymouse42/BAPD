# main.py - large comments are for learning purposes

# *****************************************************************************
# Imports:
# *****************************************************************************

import os
import subprocess
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from config.config import DEFAULT_MAME_PATH
from settings import SettingsDialog
from ui.BAPD_Main_GUI import Ui_MainWindow


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
        pass

    # =====================================================================
    # If the cancel button is pressed in the settings dialog, then do
    # the following function. Right now it is stub code. ???
    # =====================================================================
    def handle_settings_rejected(self):
        """Handles the rejected signal from the settings dialog."""
        self.plainTextEdit.appendPlainText("Settings dialog was canceled.")

    # =====================================================================
    # Opens a dialog to let the user select an Astrocade project directory.
    # This needs to be checked to see if this goes in settings.py ???
    # =====================================================================
    def select_project_directory(self):
        pass

    # =====================================================================
    # Compiles the current Astrocade project using Zmac.
    # Review this code for redundancies. ???
    # =====================================================================
    def compile(self):

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

    # =====================================================================
    # Opens the source code using the default editor
    # NOT IMPLEMENTED YET. THIS IS STUB CODE ???
    # =====================================================================
    def edit_source(self):
        self.plainTextEdit.appendPlainText("Editing source file (not yet implemented)")

    # =====================================================================
    # Opens the listing file using the default editor.
    # NOT IMPLEMENTED YET. THIS IS STUB CODE ???
    # =====================================================================
    def view_listing(self):
        self.plainTextEdit.appendPlainText("Viewing listing file (not yet implemented)")

    # =====================================================================
    # Runs the standard version of MAME without regard to project.
    # NOT IMPLEMENTED YET. THIS IS STUB CODE ???
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
    # Runs the currently compiled program with some standard options and
    # any user specified options from the settings menu.
    # =====================================================================
    def run_current_program(self):
        project_name = os.path.basename(self.current_project_path)
        bin_file_path = os.path.normpath(os.path.join(self.current_project_path, f"{project_name}.bin"))

        mame_path = DEFAULT_MAME_PATH
        mame_dir = os.path.dirname(mame_path)

        mame_command = [
            mame_path,
            "astrocde",
            "-cart", bin_file_path,
            "-filter",
            "-window"
        ]

        if self.mameDebugCheckBox.isChecked():
            mame_command.append("-debug")

        os.chdir(mame_dir)
        subprocess.Popen(mame_command)
        self.plainTextEdit.appendPlainText("MAME has been launched.")

    # =====================================================================
    # While this is a button, I do not have a use for it at this time
    # I am thinking about making it an easter egg or some extra info
    # about zmac or both. This will probably be implemented last.
    # =====================================================================
    def print_version(self):
        pass


# *****************************************************************************
# Main program loop.
# *****************************************************************************

if __name__ == "__main__":
    app = QApplication(sys.argv)  # app is part of PySide6 - Initializes whole program?
    window = MainWindow()  # window: Creates object for class above
    window.show()  # show is a PySid6 method. How did it get into our class?
    sys.exit(app.exec())  # Explain this?
