# directory_management.py

import shutil
from pathlib import Path
from typing import TypeAlias, Dict, Union, List

import toml

from config.config import DIRECTORY_TREE, TOML_FULL_PATH

# *****************************************************************************
# This will be a class that handles all the directory management.
# Right now, it only creates a directory based on the structure in config.py
# I may expand it to handle all directory and file defaults or other stuff ???
# Note: When called it will use the DIRECTORY_TREE structure in config.py
# *****************************************************************************

# Type alias for the directory tree structure
TreeStructure: TypeAlias = Dict[str, Union[Dict, List[str]]]


class DirectoryManagement:
    def __init__(self, tree_structure: TreeStructure):
        self.tree_structure = tree_structure
        self.base_dir = Path.home()

    # *************************************************************************
    # PUBLIC METHOD:
    # Checks the actual production directory and files against the expected
    # directory and file tree structure (see config.py)
    # Creates any missing items but leaves existing or extra items alone.
    # *************************************************************************
    def verify_directory_structure(self) -> None:
        self._verify_directory_structure_recursive(self.base_dir, self.tree_structure)

    # *************************************************************************
    # PUBLIC METHOD:
    # Loads the TOML file
    # *************************************************************************
    def read_toml(self):
        return self._read_toml()

    # *************************************************************************
    # PUBLIC METHOD:
    # Writes a modified entries to the TOML file
    # *************************************************************************
    def write_toml(self):
        return self._write_toml()

    # *************************************************************************
    # PRIVATE METHOD:
    # Check for a complete directory structure adding any missing items.
    # *************************************************************************
    def _verify_directory_structure_recursive(self, base_path: Path, node: TreeStructure) -> None:
        for key, value in node.items():
            new_path: Path = base_path / key

            if key == "files":  # If it's a list of files
                self._verify_files(base_path, value)
            else:
                new_path.mkdir(parents=True, exist_ok=True)
                if isinstance(value, dict):  # If it's a subdirectory, recurse
                    self._verify_directory_structure_recursive(new_path, value)

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

    # *************************************************************************
    # PRIVATE METHOD:
    # Read the TOML file. Checks to see if the file is there and if it
    # is a valid TOML file.
    # *************************************************************************
    @classmethod
    def _read_toml(cls) -> dict:
        try:
            with open(TOML_FULL_PATH, "r") as toml_file:
                settings = toml.load(toml_file)
                return settings
        except FileNotFoundError:
            print(f"Error: TOML file not found at {TOML_FULL_PATH}")
            return {}  # Return an empty dictionary if file is not found
        except toml.TomlDecodeError:
            print(f"Error: Invalid TOML format in {TOML_FULL_PATH}")
            return {}

    # *************************************************************************
    # PRIVATE METHOD:
    # Write the modified TOML file.
    # *************************************************************************
    @classmethod
    def _write_toml(cls) -> dict:
        return {}


def main():
    # Create an instance of the DirectoryManagement class
    manager = DirectoryManagement(DIRECTORY_TREE)

    # Verify and create the directory structure
    manager.verify_directory_structure()

    # Optionally, you can add more tests or operations here


if __name__ == "__main__":
    main()
