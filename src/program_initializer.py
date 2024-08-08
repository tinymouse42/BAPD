# program_initializer.py

import os
import shutil
from typing import TypeAlias, Dict, Union, List, Any

import toml

from config.config import DEFAULT_TOML_SETTINGS, BASE_DIR, DEFAULT_FILES_DIR, TOML_FULL_PATH, USER_PROFILE_DIR
from src.file_management import FileManager

# *****************************************************************************
# This will be a class that handles all the directory management.
# Right now, it only creates a directory based on the structure in config.py
# I may expand it to handle all directory and file defaults or other stuff ???
# Note: When called it will use the DIRECTORY_TREE structure in config.py
# *****************************************************************************

# Type alias for the directory tree structure
TreeStructure: TypeAlias = Dict[str, Union[Dict, List[str]]]


class ProgramInitializer:
    def __init__(self, tree_structure: TreeStructure):
        self.tree_structure = tree_structure

    # *************************************************************************
    # PUBLIC METHOD:
    # Checks the actual production directory and files against the expected
    # directory and file tree structure (see config.py)
    # Creates any missing items but leaves existing or extra items alone.
    # *************************************************************************
    def create_directory_structure(self) -> None:
        self._create_directory_structure_recursive(USER_PROFILE_DIR, self.tree_structure)

    # *************************************************************************
    # PRIVATE METHOD:
    # Check for a complete directory structure adding any missing items.
    # *************************************************************************

    # ??? Problem is that I am getting BAPD\BAPD. It lies somewhere in this code.

    def _create_directory_structure_recursive(self, base_path: str, node: TreeStructure) -> None:
        for key, value in node.items():
            new_path = os.path.join(base_path, key)
            if key == "files":  # If it's a list of files

                self._verify_files(base_path, value)
            else:
                # Create directory with parents using os.makedirs
                os.makedirs(new_path, exist_ok=True)
                if isinstance(value, dict):  # If it's a subdirectory, recurse
                    self._create_directory_structure_recursive(new_path, value)

    # *************************************************************************
    # PRIVATE METHOD:
    # Check that all default files exist and add any missing items.
    # *************************************************************************

    @classmethod
    def _verify_files(cls, directory: str, expected_files: List[str]) -> None:
        for file_name in expected_files:
            file_path = os.path.join(directory, file_name)
            source_file = os.path.join(DEFAULT_FILES_DIR, file_name)

            if not os.path.exists(file_path):
                shutil.copy(source_file, file_path)

    # *****************************************************************************
    # Validates the TOML file format and normalizes the settings against the defaults.
    # If the TOML file is invalid or missing, a new file is created with the defaults.
    # If the TOML file is valid, missing settings are added from the default settings.
    # *****************************************************************************
    def validate_and_normalize_toml_settings(self, main_window: Any) -> Dict:
        try:
            with open(TOML_FULL_PATH, "r") as toml_file:
                settings = toml.load(toml_file)
        except (FileNotFoundError, toml.TomlDecodeError):
            # TOML file is missing or invalid, create a new file with default settings
            FileManager.write_toml(TOML_FULL_PATH, DEFAULT_TOML_SETTINGS)
            settings = DEFAULT_TOML_SETTINGS  # Assign default settings to be returned

        # Update GUI elements based on TOML settings
        self._update_gui_from_settings(main_window, settings)

        # Normalize settings by adding any missing keys from the default settings
        normalized_settings = self._normalize_settings(settings, DEFAULT_TOML_SETTINGS)

        # Write the normalized settings back to the TOML file
        FileManager.write_toml(TOML_FULL_PATH, normalized_settings)

        # Returns a complete and validated TOML file dictionary.
        return normalized_settings  # type: Dict[str, Any]

    @classmethod
    def _update_gui_from_settings(cls, main_window, settings):
        # Update MAME debug checkbox
        main_window.mameDebugCheckBox.setChecked(settings.get("mame", {}).get("debug_mode", False))
        # Update fileNameLabel with the current project name
        project_path = settings.get("project", {}).get("path", "")
        main_window.fileNameLabel.setText(os.path.basename(project_path))

    # *****************************************************************************
    # Normalizes the provided settings against the default settings.
    # Missing keys from the default settings are added to the provided settings.
    # *****************************************************************************
    @staticmethod
    def _normalize_settings(settings: Dict, default_settings: Dict) -> Dict:
        normalized_settings = settings.copy()

        for key, value in default_settings.items():
            if isinstance(value, dict):
                normalized_settings.setdefault(key, {})
                normalized_settings[key] = ProgramInitializer._normalize_settings(
                    normalized_settings.get(key, {}), value
                )
            else:
                normalized_settings.setdefault(key, value)
        return normalized_settings
