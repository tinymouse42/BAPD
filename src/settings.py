# settings.py

import os

from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox

from config.config import DEFAULT_TOML_SETTINGS, DEFAULT_ZMAC_PATH, DEFAULT_MAME_PATH
from ui.BAPD_Settings_GUI import Ui_BAPD_Settings


# *****************************************************************************
# SettingsDialog is the name of OUR class defining our program class.
#   =>  Inherits from QDialog provides a pre-built framework for
#       the settings window.
#   =>  Inherits from Ui_BAPD_Settings, which is the name of the OUR class
#       in a separate file called BAPD_Settings_GUI which contains the GUI code
#       created by Designer.
# *****************************************************************************

class SettingsDialog(QDialog, Ui_BAPD_Settings):
    # ==========================================================================
    # Initialization section. This is run when SettingsDialog is instantiated.
    # ==========================================================================
    def __init__(self, parent, settings):
        super().__init__(parent)
        self.setupUi(self)

        self.settings = settings.copy()

        # Load initial settings into the UI elements
        self.load_settings()

        # Connect buttons to their respective slots
        self.zmacButtonBox.accepted.connect(self.save_settings)  # Use zmacButtonBox
        self.zmacButtonBox.rejected.connect(self.reject)  # Use zmacButtonBox
        self.mameButtonBox.accepted.connect(self.save_settings)  # Use mameButtonBox
        self.mameButtonBox.rejected.connect(self.reject)  # Use mameButtonBox

    # ==========================================================================
    # Opens a file dialog to select the ZMAC executable path.
    # ==========================================================================
    def browse_zmac_path(self):

        current_path = self.settings.get("zmac", {}).get("path", "")
        zmac_path, _ = QFileDialog.getOpenFileName(
            self, "Select ZMAC Executable", os.path.dirname(current_path), "Executable Files (*.exe)"
        )
        if zmac_path:
            # Validate the selected file (e.g., check if it's a valid Zmac executable)
            if not zmac_path.lower().endswith(".exe"):  # Basic validation
                # Show an error message to the user
                QMessageBox.warning(self, "Invalid File", "Please select a valid ZMAC executable (.exe).")
                return  # Don't update the path if it's invalid

            self.settings["zmac"]["path"] = zmac_path  # Update settings immediately
            self.zmacPathLineEdit.setText(zmac_path)  # Update the line edit display

    # ==========================================================================
    # Saves the current settings to the TOML file
    # ==========================================================================
    def load_settings(self):
        """Loads the settings from the dictionary into the UI elements."""
        # ZMAC Settings
        self.zmacPathLineEdit.setText(self.settings.get("zmac", {}).get("path", DEFAULT_ZMAC_PATH))
        self.outputHexFile.setChecked(self.settings.get("zmac", {}).get("output_hex_file", False))
        self.expandMacros.setChecked(self.settings.get("zmac", {}).get("expand_macros", False))
        self.expandIncludeFiles.setChecked(self.settings.get("zmac", {}).get("expand_include_files", False))
        self.expandIf.setChecked(self.settings.get("zmac", {}).get("expand_if", False))
        self.omitSymbolTable.setChecked(self.settings.get("zmac", {}).get("omit_symbol_table", False))
        self.allow8080Instructions.setChecked(self.settings.get("zmac", {}).get("allow_8080_instructions", False))

        # MAME Settings
        self.mamePathLineEdit.setText(self.settings.get("mame", {}).get("path", DEFAULT_MAME_PATH))
        self.debugModeOn.setChecked(self.settings.get("mame", {}).get("debug_mode", False))
        self.windowModeOn.setChecked(self.settings.get("mame", {}).get("window_mode", True))
        self.skipGameInfo.setChecked(self.settings.get("mame", {}).get("skip_game_info", True))

        # Radio buttons for MAME system
        if self.settings.get("mame", {}).get("bally_pro_arcade", True):
            self.ballyProArcade.setChecked(True)
        elif self.settings.get("mame", {}).get("bally_home_library_computer", False):
            self.ballyHomeLibraryComputer.setChecked(True)
        elif self.settings.get("mame", {}).get("bally_computer_system", False):
            self.ballyComputerSystem.setChecked(True)

    def save_settings(self):
        """Saves the settings from the UI elements into the dictionary."""

        # ZMAC Settings
        self.settings["zmac"]["path"] = self.zmacPathLineEdit.text()
        self.settings["zmac"]["output_hex_file"] = self.outputHexFile.isChecked()
        self.settings["zmac"]["expand_macros"] = self.expandMacros.isChecked()
        self.settings["zmac"]["expand_include_files"] = self.expandIncludeFiles.isChecked()
        self.settings["zmac"]["expand_if"] = self.expandIf.isChecked()
        self.settings["zmac"]["omit_symbol_table"] = self.omitSymbolTable.isChecked()
        self.settings["zmac"]["allow_8080_instructions"] = self.allow8080Instructions.isChecked()

        # MAME Settings
        self.settings["mame"]["path"] = self.mamePathLineEdit.text()
        self.settings["mame"]["debug_mode"] = self.debugModeOn.isChecked()
        self.settings["mame"]["window_mode"] = self.windowModeOn.isChecked()
        self.settings["mame"]["skip_game_info"] = self.skipGameInfo.isChecked()

        # Radio buttons for MAME system
        self.settings["mame"]["bally_pro_arcade"] = self.ballyProArcade.isChecked()
        self.settings["mame"]["bally_home_library_computer"] = self.ballyHomeLibraryComputer.isChecked()
        self.settings["mame"]["bally_computer_system"] = self.ballyComputerSystem.isChecked()

        self.accept()  # Accept the dialog to signal that settings are saved


# *****************  End SettingsDialog Class  *****************************

# ==========================================================================
# Adds any missing settings to the given settings dictionary with their default values.
# Returns True if settings were modified, False otherwise.
# ==========================================================================
def add_missing_settings(settings):
    modified = False
    for section, section_defaults in DEFAULT_TOML_SETTINGS.items():  # Use DEFAULT_TOML_SETTINGS
        if section not in settings:
            settings[section] = section_defaults.copy()
            modified = True
        else:
            for key, default_value in section_defaults.items():
                if key not in settings[section]:
                    settings[section][key] = default_value
                    modified = True

    return modified
