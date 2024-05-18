# src/settings.py

# settings.py
import toml
import os
from ui.BAPD_Settings_GUI import Ui_BAPD_Settings
from PySide6.QtWidgets import QDialog


# Dummy SettingsDialog class


class SettingsDialog(QDialog, Ui_BAPD_Settings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.settings = load_toml_settings()  # Load settings

        # Load ZMAC path from settings and update line edit
        zmac_path = self.settings.get("zmac", {}).get("path", "")
        self.zmacPathLineEdit.setText(zmac_path)  # Update the line edit
        self.zmacBrowseButton.clicked.connect(self.browse_zmac_path)


def save_settings(self):
    self.settings["zmac"]["path"] = self.zmacPathLineEdit.text()
    save_toml_settings(self.settings)


def save_toml_settings(settings):  # Moved above SettingsDialog
    with open("config/settings.toml", "w") as f:
        toml.dump(settings, f)


def create_default_zmac_dir():
    """Creates the default ZMAC directory if it doesn't exist."""
    zmac_dir = os.path.join(os.environ['USERPROFILE'], "BAPD", "_Programs", "ZMAC")
    os.makedirs(zmac_dir, exist_ok=True)
    return zmac_dir


def load_toml_settings():
    """Loads settings from TOML file and creates default ZMAC dir."""
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
                # ... other zmac options
            },
            "mame": {
                "path": "",
            }
        }
