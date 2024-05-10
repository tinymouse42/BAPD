# settings_test_main.py
import sys
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog  # Import QFileDialog as well
from Settings_Test_GUI import Ui_BAPD_Settings
import toml  # Add this import
import os


class SettingsDialog(QDialog, Ui_BAPD_Settings):  # Inherit from both QDialog and Ui_BAPD_Settings
    def __init__(self, settings):
        super().__init__()
        self.setupUi(self)  # Set up the UI from the generated class

        self.load_zmac_path(settings)  # Load the Zmac path (from the generated Ui_BAPD_Settings class)
        self.browseZmacButton.clicked.connect(self.browse_zmac_path)  # Connect browse button

        # Connect checkbox signals (stub implementations)
        self.expandIncludeFiles.stateChanged.connect(lambda: self.checkbox_toggled("expandIncludeFiles"))
        self.expandMacros.stateChanged.connect(lambda: self.checkbox_toggled("expandMacros"))
        self.useUndocumentedInstructions.stateChanged.connect(
            lambda: self.checkbox_toggled("useUndocumentedInstructions"))
        self.outputHexFile.stateChanged.connect(lambda: self.checkbox_toggled("outputHexFile"))
        self.omitSymbolTable.stateChanged.connect(lambda: self.checkbox_toggled("omitSymbolTable"))
        self.labelsMustHaveColons.stateChanged.connect(lambda: self.checkbox_toggled("labelsMustHaveColons"))

        # Connect button signals (stub implementations)
        # ... (You would connect other buttons here as needed)

    def browse_zmac_path(self):
        print("Browse Zmac Path button clicked")
        # ... (Your implementation to open a file dialog and get the Zmac path) ...

    def checkbox_toggled(self, checkbox_name):
        print(f"{checkbox_name} toggled")


def load_toml_settings():
    # ... (Implementation from the previous response)
    pass


def save_toml_settings(settings):
    # ... (Implementation from the previous response)
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Load initial settings
    settings = load_toml_settings()

    dialog = SettingsDialog(settings)
    if dialog.exec() == QtWidgets.QDialog.Accepted:
        dialog.save_zmac_path(settings)  # Save the Zmac path
        save_toml_settings(settings)  # Save other settings
        print("Settings saved successfully.")
    else:
        print("Dialog canceled.")
    sys.exit(app.exec())
