# settings.py  - large comments are for learning purposes

# *****************************************************************************
# Imports:
# *****************************************************************************

import os
import toml
from config.config import TOML_PATH
from ui.BAPD_Settings_GUI import Ui_BAPD_Settings
from PySide6.QtWidgets import QDialog, QFileDialog


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
        self.settings = load_toml_settings()

        # ==========================================================================
        # Load ZMAC path from TOML file and update line edit display
        # ==========================================================================
        zmac_path = self.settings.get("zmac", {}).get("path", "")
        self.zmacPathLineEdit.setText(zmac_path)  # Update the line edit
        self.zmacBrowseButton.clicked.connect(self.browse_zmac_path)

        # ==========================================================================
        # ===> THIS IS NOT WORKING
        # It is because I didn't have the DialogButtonBox in the Designer file.
        # I have fixed that and now just need to implement it. For now, I just
        # commented out the non-working lines of code.
        # ==========================================================================
        # self.buttonBox.accepted.connect(self.accept)  # Connect to built-in accept method
        # self.buttonBox.rejected.connect(self.reject)  # Connect to built-in reject method

        # ==========================================================================
        # Opens a file dialog to select the ZMAC executable path.
        # EVALUATE THIS. ???
        # ==========================================================================

    def browse_zmac_path(self):
        current_path = self.settings.get("zmac", {}).get("path", "")
        zmac_path, _ = QFileDialog.getOpenFileName(
            self, "Select ZMAC Executable", os.path.dirname(current_path), "Executable Files (*.exe)"
        )
        if zmac_path:
            self.zmacPathLineEdit.setText(zmac_path)


# *****************  End SettingsDialog Class  *****************************


# ==========================================================================
# Save ZMAC path.
# EVALUATE THIS AND RENAME FOR CLARITY ???
# ==========================================================================
def save_settings(self):
    self.settings["zmac"]["path"] = self.zmacPathLineEdit.text()
    save_toml_settings(self.settings)


# ==========================================================================
# Loads settings from TOML file and creates default ZMAC dir.
# EVALUATE THIS AND RENAME FOR CLARITY ???
# ==========================================================================
def load_toml_settings():
    create_default_zmac_dir()
    try:
        with open("config/settings.toml", "r") as f:
            settings = toml.load(f)
            # If the ZMAC path isn't set or is invalid, use the default directory
            if not settings.get("zmac", {}).get("path") or not os.path.exists(settings.get("zmac", {}).get("path")):
                settings["zmac"]["path"] = os.path.join(create_default_zmac_dir(), "zmac.exe")
            return settings
    except FileNotFoundError:
        return {  # Default settings with the default directory
            "zmac": {
                "path": os.path.join(create_default_zmac_dir(), "zmac.exe"),
            },
            "mame": {
                "path": "",
            }
        }


# ==========================================================================
# Saves settings to the TOML file.
# EVALUATE THIS AND RENAME ??? FOR CLARITY ???
# ==========================================================================
def save_toml_settings(settings):
    with open(os.path.join(TOML_PATH, "settings.toml"), "w") as f:
        toml.dump(settings, f)


# ==========================================================================
# Creates the default ZMAC directory if it doesn't exist.
# # EVALUATE THIS. POSSIBLE RENAME FOR CLARITY ???
# ==========================================================================
def create_default_zmac_dir():
    zmac_dir = os.path.join(os.environ['USERPROFILE'], "BAPD", "_Programs", "ZMAC")
    os.makedirs(zmac_dir, exist_ok=True)
    return zmac_dir
