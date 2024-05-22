# settings.py  - large comments are for learning purposes

import os
import glob
import toml
from ui.BAPD_Settings_GUI import Ui_BAPD_Settings
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox, QDialogButtonBox

# Import constants defined in the config.py file
from config.config import (TOML_FULL_PATH, DEFAULT_ZMAC_PATH, DEFAULT_MAME_PATH,
                           DEFAULT_ORIGINAL_MAME_ROMS_PATH, DEFAULT_PROJECT_PATH,
                           DEFAULT_SOURCE_NAME, ZMAC_NOT_FOUND)


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
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Load settings from TOML file
        self.settings = load_settings_from_toml()

        # Connect button box signals to slots
        self.zmacButtonBox.clicked.connect(self.handle_button_click)
        self.mameButtonBox.clicked.connect(self.handle_button_click)

        # Now, set the ZMAC path in the line edit after loading settings
        zmac_path = self.settings.get("zmac", {}).get("path", "")
        self.zmacPathLineEdit.setText(zmac_path)

        # ==========================================================================
        # Connect signals to slots (button clicks, etc.)
        # ==========================================================================
        self.zmacBrowseButton.clicked.connect(self.browse_zmac_path)
        self.mameButtonBox.clicked.connect(self.handle_button_click)

    def handle_button_click(self, button):
        role = self.zmacButtonBox.buttonRole(button)

        if role == QDialogButtonBox.ButtonRole.ApplyRole:
            self.save_settings_to_toml()
        elif role == QDialogButtonBox.ButtonRole.AcceptRole:
            self.save_settings_to_toml()
            self.accept()
        elif role == QDialogButtonBox.ButtonRole.RejectRole:
            self.reject()

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
    def save_settings_to_toml(self):
        """Saves the current settings to the TOML file."""
        try:
            # Gather settings from the UI elements
            self.settings["zmac"]["path"] = self.zmacPathLineEdit.text()
            self.settings["zmac"]["output_hex_file"] = self.outputHexFile.isChecked()
            self.settings["zmac"]["expand_include_files"] = self.expandIncludeFiles.isChecked()
            self.settings["zmac"]["expand_macros"] = self.expandMacros.isChecked()
            self.settings["zmac"]["omit_symbol_table"] = self.omitSymbolTable.isChecked()

            # Save to TOML file (using the centralized function)
            save_toml_settings(self.settings)

            # Optionally, provide user feedback (e.g., status bar message)
            print("Settings saved successfully!")  # Or use a logging mechanism

        except Exception as e:  # Catch any potential errors during saving
            # Handle the error (e.g., log it, show an error message to the user)
            print(f"Error saving settings: {e}")  # Or use a logging mechanism


# *****************  End SettingsDialog Class  *****************************


# ==========================================================================
# Loads settings from the TOML file, creating it with defaults
# if it doesn't exist.
# ==========================================================================
def load_settings_from_toml():
    try:
        # Attempt to load settings from the TOML file
        with open(TOML_FULL_PATH, "r") as f:
            settings = toml.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, create it with default settings
        settings = {
            "zmac": {
                "path": DEFAULT_ZMAC_PATH,
                "output_hex_file": True,
                "expand_include_files": False,
                "expand_macros": False,
                "omit_symbol_table": False,
            },
            "mame": {
                "path": DEFAULT_MAME_PATH,
            },
            "original_mame_roms_path": {
                "path": DEFAULT_ORIGINAL_MAME_ROMS_PATH,
            },
            "project": {
                "path": DEFAULT_PROJECT_PATH,
                "source_file_name": DEFAULT_SOURCE_NAME,
            },
        }

        save_toml_settings(settings)  # Save the default settings to the file

    # Ensure all expected settings are present (add missing ones with defaults)
    add_missing_settings(settings)  # Reusing the same function

    # Search for ZMAC executable
    zmac_pattern = os.path.join(DEFAULT_ZMAC_PATH, "zmac*.exe")
    zmac_matches = glob.glob(zmac_pattern)
    if zmac_matches:
        settings["zmac"]["path"] = zmac_matches[0]  # Use the first match
    else:
        settings["zmac"]["path"] = ZMAC_NOT_FOUND

    return settings


# ==========================================================================
# Saves settings to the TOML file.
# ==========================================================================
def save_toml_settings(settings):
    """Saves settings to the TOML file."""  # More descriptive name
    with open(TOML_FULL_PATH, "w") as f:
        toml.dump(settings, f)


# ==========================================================================
# Adds any missing settings to the given settings dictionary with their default values.
# ==========================================================================
def add_missing_settings(settings):
    default_settings = {  # Define your default settings here
        "zmac": {
            "path": DEFAULT_ZMAC_PATH,
            "output_hex_file": True,
            "expand_include_files": False,
            "expand_macros": False,
            "omit_symbol_table": False,
        },
        "mame": {
            "path": DEFAULT_MAME_PATH,
        },
        "original_mame_roms_path": {
            "path": DEFAULT_ORIGINAL_MAME_ROMS_PATH,
        },
        "project": {
            "path": DEFAULT_PROJECT_PATH,
            "source_file_name": DEFAULT_SOURCE_NAME,
        },
    }

    for section, section_defaults in default_settings.items():
        if section not in settings:
            settings[section] = section_defaults
        else:
            for key, default_value in section_defaults.items():
                if key not in settings[section]:
                    settings[section][key] = default_value
