# program_initializer.py

import shutil
from pathlib import Path
from typing import TypeAlias, Dict, Union, List

import toml

from config.config import DEFAULT_TOML_SETTINGS, CONFIG_DIR, TOML_FILE_NAME
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
        self.base_dir = Path.home()
        self.toml_file_path = Path(CONFIG_DIR) / TOML_FILE_NAME

    # *************************************************************************
    # PUBLIC METHOD:
    # Checks the actual production directory and files against the expected
    # directory and file tree structure (see config.py)
    # Creates any missing items but leaves existing or extra items alone.
    # *************************************************************************
    def create_directory_structure(self) -> None:
        self._create_directory_structure_recursive(self.base_dir, self.tree_structure)

    # *************************************************************************
    # PRIVATE METHOD:
    # Check for a complete directory structure adding any missing items.
    # *************************************************************************
    def _create_directory_structure_recursive(self, base_path: Path, node: TreeStructure) -> None:
        for key, value in node.items():
            new_path: Path = base_path / key

            if key == "files":  # If it's a list of files
                self._verify_files(base_path, value)
            else:
                new_path.mkdir(parents=True, exist_ok=True)
                if isinstance(value, dict):  # If it's a subdirectory, recurse
                    self._create_directory_structure_recursive(new_path, value)

    # *************************************************************************
    # PRIVATE METHOD:
    # Check that all default files exist and add any missing items.
    # *************************************************************************
    @classmethod
    def _verify_files(cls, directory: Path, expected_files: List[str]) -> None:
        # Get the project directory path
        project_dir = Path(__file__).parent.parent

        # Construct the path to the default_files directory
        default_files_dir = project_dir / "config" / "default_files"

        for file_name in expected_files:
            file_path = directory / file_name
            source_file = default_files_dir / file_name

            if not file_path.exists():
                shutil.copy(source_file, file_path)

    # *****************************************************************************
    # Validates the TOML file format and normalizes the settings against the defaults.
    # If the TOML file is invalid or missing, a new file is created with the defaults.
    # If the TOML file is valid, missing settings are added from the default settings.
    # *****************************************************************************
    def validate_and_normalize_toml_settings(self) -> None:
        try:
            with open(self.toml_file_path, "r") as toml_file:
                settings = toml.load(toml_file)
        except (FileNotFoundError, toml.TomlDecodeError):
            # TOML file is missing or invalid, create a new file with default settings
            FileManager.write_toml(self.toml_file_path, DEFAULT_TOML_SETTINGS)
            return

        # Normalize settings by adding any missing keys from the default settings
        normalized_settings = self._normalize_settings(settings, DEFAULT_TOML_SETTINGS)

        # Write the normalized settings back to the TOML file
        FileManager.write_toml(self.toml_file_path, normalized_settings)

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


'''
def main():
    manager = ProgramInitializer(DIRECTORY_TREE)

    # Verify and create the directory structure
    manager.create_directory_structure()

    # Validate and normalize the TOML file settings
    manager.validate_and_normalize_toml_settings()


if __name__ == "__main__":
    main()
'''
