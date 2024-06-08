# *****************************************************************************
# This will be a class that handles all the directory management.
# Right now, it only creates a directory based on the structure in config.py
# I may expand it to handle all directory and file defaults or other stuff ???
# Note: When called it will use the DIRECTORY_TREE structure in config.py
# Should this class be in a separate file for readability ???
# *****************************************************************************
from pathlib import Path
from typing import TypeAlias, Dict

# Type alias for the directory tree structure
TreeStructure: TypeAlias = Dict[str, Dict]


class DirectoryManagement:
    def __init__(self, tree_structure: TreeStructure):
        self.tree_structure: TreeStructure = tree_structure
        self.base_dir: Path = Path.home()

    def create_directories(self) -> None:
        if self._validate_tree_structure():
            self._create_directories_recursive(self.base_dir, self.tree_structure)
        else:
            print("Invalid directory structure provided.")

    def _validate_tree_structure(self) -> bool:
        # Implement your validation logic here (e.g., check for valid characters in names)
        return True  # For now, assume the structure is always valid

    def _create_directories_recursive(self, base_path: Path, node: TreeStructure) -> None:
        for key, value in node.items():
            new_path: Path = base_path / key
            new_path.mkdir(parents=True, exist_ok=True)
            if value:  # If the value is a non-empty dictionary (i.e., a subdirectory)
                self._create_directories_recursive(new_path, value)


# Example of use
# manager = DirectoryManagement(DIRECTORY_TREE)
# manager.create_directories()
