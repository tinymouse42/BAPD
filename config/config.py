# config.py

"""
This module provides configuration settings for the Bally Astrocade
Program Development (BAPD) tool.

It defines constants for file paths and default settings,
ensuring a consistent and organized way to manage configuration
throughout the application.

The pathlib library is used throughout the code
"""

from pathlib import Path

# I am converting the whole program to use pathlib.
# This config.py has been converted.

# *************************************************************************
# Constants for paths and files
#
# PROGRAMMER NOTE! THE CONSTANTS BELOW HAVE TO BE THE SAME AS THE
# DIRECTORY TREE OR IT GO BOOM. THE EASIEST WAY TO CHECK IS TO TAKE BOTH
# AND RUN IT THROUGH AN AI. ALSO, I DO NOT EXPECT THE LOCATIONS TO CHANGE
# IN THIS VERSION SO THERE IS NO NEED TO GO THROUGH WRITING A
# GENERATOR TO MAKE ALL THIS AUTOMATIC.
#
# *************************************************************************

# Get user profile directory
USER_PROFILE_DIR = Path.home()
print(USER_PROFILE_DIR, type(USER_PROFILE_DIR))

# Program Directories (Not changeable by user)
BASE_DIR = USER_PROFILE_DIR / "BAPD"
PROGRAMS_DIR = BASE_DIR / "Programs"
PROJECT_DIR = BASE_DIR / "Projects"
CONFIG_DIR = PROGRAMS_DIR / "Config"

# DEFAULT_ORIGINAL_MAME_ROMS_PATH = PROGRAMS_DIR / "ROMS" (Commented out for now)
DEFAULT_PROJECT_PATH = PROJECT_DIR / "Astrocade_Program"
DEFAULT_SOURCE_NAME = Path("Astrocade_Program.asm")  # relative path

# Settings File
TOML_FILE_NAME = Path("user_settings.toml")  # relative path
TOML_FULL_PATH = CONFIG_DIR / TOML_FILE_NAME

# Default Paths (Used if not specified in settings)
DEFAULT_ZMAC_PATH = PROGRAMS_DIR / "Zmac" / "zmac.exe"
DEFAULT_MAME_PATH = PROGRAMS_DIR / "MAME" / "mame.exe"

# *************************************************************************
# Directory tree structure that will be used to validate
# the default directory and files. Files will be pulled from
# the config/Default_Files directory. The easiest way to modify this
# structure is to tell and AI what you need modified.
#
# PROGRAMMER NOTE! THIS MUST MATCH THE CONSTANTS ABOVE OR PROGRAM GO BOOM!
# SEE THE COMMENT FOR CONSTANTS FOR MORE INFORMATION.
# *************************************************************************

DIRECTORY_TREE = {
    "BAPD": {
        "Projects": {
            "Astrocade_Program": {
                "Version_Archive": {
                    "files": ["Astrocade_Demo_Cartridge.asm"]
                },
                "files": ["Astrocade_Program.asm", "HVGLIB.H"]
            }
        },
        "Documentation": {},
        "Programs": {
            "MAME": {
                "roms": {
                    "astrocde": {
                        "files": ["astrcde.bin", "astro.bin"]
                    },
                    "astrocdl": {
                        "files": ["ballyhlc.bin"]
                    },
                    "astrocdw": {
                        "files": ["bioswhit.bin"]
                    }
                }
            },
            "PSPad": {
                "Syntax": {
                    "files": ["Z80.INI"]
                }
            },
            "Zmac": {
                "files": ["zmac.exe"]
            },
            "Config": {}
        }
    }
}

# *************************************************************************
# Default user settings for the TOML file.
# *************************************************************************
DEFAULT_TOML_SETTINGS = {
    "project": {
        "path": str(DEFAULT_PROJECT_PATH).replace("\\", "/"),
        "source_file_name": str(DEFAULT_SOURCE_NAME).replace("\\", "/"),
    },
    "zmac": {
        "path": str(DEFAULT_ZMAC_PATH).replace("\\", "/"),
        "output_hex_file": False,
        "expand_macros": False,
        "expand_include_files": False,
        "expand_if": False,
        "omit_symbol_table": False,
        "allow_8080_instructions": False,
    },
    "mame": {
        "path": str(DEFAULT_MAME_PATH).replace("\\", "/"),
        "debug_mode": False,
        "window_mode": True,
        "skip_game_info": True,
        "bally_pro_arcade": True,
        "bally_home_library_computer": False,
        "bally_computer_system": False,
    },
}
print(DEFAULT_TOML_SETTINGS)

"""
# *************************************************************************
# THIS IS A POSSIBLE FUTURE IMPLEMENTATION
# *************************************************************************
def validate_directory_structure(base_dir: Path, directory_tree: dict) -> bool:
 
  This function validates the directory structure based on the provided tree.

  Args:
      base_dir: The base directory to start the validation from.
      directory_tree: A dictionary representing the expected directory structure.

  Returns:
      True if the directory structure matches the provided tree, False otherwise.
  
  for subdir_name, subdir_contents in directory_tree.items():
    subdir_path = base_dir / subdir_name
    if not subdir_path.is_dir():
      print(f"Error: Directory '{subdir_path}' not found.")
      return False
    validate_directory_structure(subdir_path, subdir_contents)

  # Check for expected files within the current directory
  for filename, file_info in directory_tree.get("files", {}).items():
    file_path = base_dir / filename
    if not file_path.is_file():
      print(f"Error: File '{file_path}' not found.")
      return False
  return True
  
  
  # Example usage
if __name__ == "__main__":
  if validate_directory_structure(BASE_DIR, DIRECTORY_TREE):
    print("Directory structure is valid!")
  else:
    print("Directory structure validation failed.")
  
  """
