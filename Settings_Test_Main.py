import sys
import os
import toml
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog
from Settings_Test_GUI import Ui_BAPD_Settings


class SettingsDialog(QDialog, Ui_BAPD_Settings):
    def __init__(self, settings):
        super().__init__()
        self.setupUi(self)

        # Load initial settings
        self.load_settings(settings)

        # Connect browse button
        self.browseZmacButton.clicked.connect(self.browse_zmac_path)

        # Connect checkbox signals (stub implementations)
        self.expandIncludeFiles.stateChanged.connect(lambda: self.checkbox_toggled("expandIncludeFiles"))
        self.expandMacros.stateChanged.connect(lambda: self.checkbox_toggled("expandMacros"))
        self.useUndocumentedInstructions.stateChanged.connect(
            lambda: self.checkbox_toggled("useUndocumentedInstructions"))
        self.outputHexFile.stateChanged.connect(lambda: self.checkbox_toggled("outputHexFile"))
        self.omitSymbolTable.stateChanged.connect(lambda: self.checkbox_toggled("omitSymbolTable"))
        self.labelsMustHaveColons.stateChanged.connect(lambda: self.checkbox_toggled("labelsMustHaveColons"))

    def load_settings(self, settings):
        self.zmacPathLineEdit.setText(settings.get('paths', {}).get('zmac_exe', ''))

        # Load checkbox settings here as well...
        # (You'll need to add code to set the checkbox states based on the settings data)

    def save_settings(self):
        settings = {}
        settings['paths'] = {
            'zmac_exe': self.zmacPathLineEdit.text(),
            # ... other paths ...
        }
        settings['options'] = {
            'expand_include_files': self.expandIncludeFiles.isChecked(),
            'expand_macros': self.expandMacros.isChecked(),
            # ... other checkbox settings ...
        }
        save_toml_settings(settings)

    def browse_zmac_path(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Select Zmac Executable", "", "Executable Files (*.exe);;All Files (*)", options=options
        )
        if fileName:
            self.zmacPathLineEdit.setText(fileName)

    def checkbox_toggled(self, checkbox_name):
        print(f"{checkbox_name} toggled")


def load_toml_settings():
    settings_path = os.path.join(
        os.environ['USERPROFILE'], "BAPD", "_Programs", "config", "settings.toml"
    )
    try:
        with open(settings_path, 'r') as f:
            return toml.load(f)
    except FileNotFoundError:
        return {}


def save_toml_settings(settings):
    settings_path = os.path.join(
        os.environ['USERPROFILE'], "BAPD", "_Programs", "config", "settings.toml"
    )
    with open(settings_path, 'w') as f:
        toml.dump(settings, f)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Load initial settings
    settings = load_toml_settings()

    dialog = SettingsDialog(settings)
    if dialog.exec() == QDialog.Accepted:
        dialog.save_settings()  # Save all settings (including Zmac path and checkboxes)
        print("Settings saved successfully.")
    else:
        print("Dialog canceled.")
    sys.exit(app.exec())
