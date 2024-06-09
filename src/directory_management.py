# directory_management.py
import shutil
from pathlib import Path
from typing import TypeAlias, Dict, Union, List

from config.config import DIRECTORY_TREE

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
    # Checks the actual production directory against the expected directory
    # tree structure (see config.py) and creates any missing directories.
    # If a directory already exists, it is left unchanged.
    # *************************************************************************

    def verify_directory_structure(self) -> None:
        self._verify_directory_structure_recursive(self.base_dir, self.tree_structure)

    # *************************************************************************
    # Private method to implement the public verify_directory_structure method.
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
    # Private method to check for and default files and copy them
    # over if necessary. If a file exists, it is left alone.The default files
    # are kept in the code project directory config/default_files.
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
                print(f"Copied {source_file} to {file_path}")
            else:
                print(f"File {file_path} already exists, skipping.")


'''
def main():
    # Create an instance of the DirectoryManagement class
    manager = DirectoryManagement(DIRECTORY_TREE)

    # Verify and create the directory structure
    manager.verify_directory_structure()

    # Optionally, you can add more tests or operations here


if __name__ == "__main__":
    main()
'''
