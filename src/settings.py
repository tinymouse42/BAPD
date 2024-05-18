# settings.py
import toml
import os
from ui.BAPD_Settings_GUI import Ui_BAPD_Settings
from PySide6.QtWidgets import QDialog, QFileDialog


class SettingsDialog(QDialog, Ui_BAPD_Settings):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.settings = load_toml_settings()

        # Load ZMAC path from settings and update line edit
        zmac_path = self.settings.get("zmac", {}).get("path", "")
        self.zmacPathLineEdit.setText(zmac_path)  # Update the line edit
        self.zmacBrowseButton.clicked.connect(self.browse_zmac_path)

        # ===> THIS IS NOT WORKING and GEMINI is sending me down a rabbit hole.
        # Connect the accept button to the save_settings method
        self.buttonBox.accepted.connect(self.accept)  # Connect to built-in accept method
        self.buttonBox.rejected.connect(self.reject)  # Connect to built-in reject method

    def browse_zmac_path(self):
        """Opens a file dialog to select the ZMAC executable path."""
        current_path = self.settings.get("zmac", {}).get("path", "")
        zmac_path, _ = QFileDialog.getOpenFileName(
            self, "Select ZMAC Executable", os.path.dirname(current_path), "Executable Files (*.exe)"
        )
        if zmac_path:
            self.zmacPathLineEdit.setText(zmac_path)


def save_settings(self):
    self.settings["zmac"]["path"] = self.zmacPathLineEdit.text()
    save_toml_settings(self.settings)


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


def save_toml_settings(settings):
    """Saves settings to TOML file."""
    with open("config/settings.toml", "w") as f:
        toml.dump(settings, f)


def create_default_zmac_dir():
    """Creates the default ZMAC directory if it doesn't exist."""
    zmac_dir = os.path.join(os.environ['USERPROFILE'], "BAPD", "_Programs", "ZMAC")
    os.makedirs(zmac_dir, exist_ok=True)
    return zmac_dir
