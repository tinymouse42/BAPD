import sys
import os
import subprocess
import toml
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QMessageBox
from PySide6.QtGui import QAction  # Import QAction from QtGui
from PySide6.QtCore import QDir
from PySide6 import QtGui




class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.settings = self.load_toml_settings()

        # ... (Your existing signal connections for buttons in main window) ...

        # Create Settings action
        settings_action = QAction("Settings", self)
        settings_action.triggered.connect(self.open_settings_dialog)
        self.menuSettings.addAction(settings_action)  # Add to the Settings menu

        # Set the icon for the Settings menu item
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/gear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        settings_action.setIcon(icon)

    def open_settings_dialog(self):
        dialog = SettingsDialog(self.settings)  # Pass the current settings to the dialog

        if dialog.exec() == QDialog.Accepted:
            self.settings = dialog.save_settings()  # Update settings after dialog closes
            print("Settings saved successfully.")
            # ... You can update any UI elements here based on new settings ...

        else:
            print("Dialog canceled.")

    def load_toml_settings(self):
        settings_path = os.path.join(
            os.environ['USERPROFILE'],
            "BAPD",
            "_Programs",
            "config",
            "settings.toml",
        )
        try:
            with open(settings_path, 'r') as f:
                return toml.load(f)
        except FileNotFoundError:
            return {}

    def save_toml_settings(self, settings):
        settings_path = os.path.join(
            os.environ['USERPROFILE'],
            "BAPD",
            "_Programs",
            "config",
            "settings.toml",
        )
        with open(settings_path, 'w') as f:
            toml.dump(settings, f)
    # ... (Your other existing methods in MainWindow) ...


class SettingsDialog(QDialog, Ui_BAPD_Settings):
    def __init__(self, settings):
        super().__init__()
        self.setupUi(self)

        # Load zmac_exe path from settings or use default
        self.load_settings(settings)

        # Connect browse button 
        self.browseZmacButton.clicked.connect(self.browse_zmac_path)

        # Connect checkbox signals (stub implementations)
        # ... (Same as before, in SettingsDialog class) ...

    def load_settings(self, settings):
        self.zmacPathLineEdit.setText(settings.get('paths', {}).get('zmac_exe', ''))
        self.expandIncludeFiles.setChecked(settings.get('options', {}).get('expand_include_files', False))
        self.expandMacros.setChecked(settings.get('options', {}).get('expand_macros', False))
        self.useUndocumentedInstructions.setChecked(
            settings.get('options', {}).get('use_undocumented_instructions', False))
        self.outputHexFile.setChecked(settings.get('options', {}).get('output_hex_file', False))
        self.omitSymbolTable.setChecked(settings.get('options', {}).get('omit_symbol_table', False))
        self.labelsMustHaveColons.setChecked(settings.get('options', {}).get('labels_must_have_colons', False))

    def save_settings(self):
        settings = {}
        settings['paths'] = {
            'zmac_exe': self.zmacPathLineEdit.text(),
            # ... other paths ...
        }
        settings['options'] = {
            'expand_include_files': self.expandIncludeFiles.isChecked(),
            'expand_macros': self.expandMacros.isChecked(),
            'use_undocumented_instructions': self.useUndocumentedInstructions.isChecked(),
            'output_hex_file': self.outputHexFile.isChecked(),
            'omit_symbol_table': self.omitSymbolTable.isChecked(),
            'labels_must_have_colons': self.labelsMustHaveColons.isChecked(),
        }

        save_toml_settings(settings)
        return settings  # Return the updated settings to the main window

    def browse_zmac_path(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Select Zmac Executable", "", "Executable Files (*.exe);;All Files (*)", options=options
        )
        if fileName:
            self.zmacPathLineEdit.setText(fileName)

    def checkbox_toggled(self, checkbox_name):
        print(f"{checkbox_name} toggled")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
