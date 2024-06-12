# file_management.py

from typing import Dict
import toml


class FileManager:

    # *****************************************************************************
    # Reads the contents of a TOML file and returns them as a dictionary.
    # This function takes the file path as input and returns the file contents as a
    # dictionary.
    # *****************************************************************************
    @staticmethod
    def read_toml(file_path: str) -> Dict:
        try:
            with open(file_path, "r") as toml_file:
                settings = toml.load(toml_file)
                return settings
        except FileNotFoundError:
            print(f"Error: TOML file not found at {file_path}")
            return {}
        except toml.TomlDecodeError:
            print(f"Error: Invalid TOML format in {file_path}")
            return {}

    # *****************************************************************************
    # Writes the provided settings to a TOML file.
    # This function takes the file path and settings dictionary as input and writes
    # the settings to the specified file.
    # *****************************************************************************
    @staticmethod
    def write_toml(file_path: str, settings: Dict) -> None:
        try:
            with open(file_path, "w") as toml_file:
                toml.dump(settings, toml_file)

        except Exception as e:
            print(f"Error: Failed to write TOML file at {file_path}. Error: {e}")

    # *****************************************************************************
    # Opens a file in the user's preferred editor.
    # This function takes the file path as input and opens it in the default editor.
    # *****************************************************************************
    @staticmethod
    def open_file(self, file_path: str) -> None:
        pass

    # *****************************************************************************
    # Saves the provided content to a file.
    # This function takes the file path and content as input and saves the content
    # to the specified file.
    # *****************************************************************************
    @staticmethod
    def save_file(file_path: str, content: str) -> None:
        try:
            with open(file_path, "w") as file:
                file.write(content)
        except Exception as e:
            print(f"Error: Failed to write to file at {file_path}. Error: {e}")
