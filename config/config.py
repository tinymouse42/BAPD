# config.py

"""
This module provides configuration settings for the Bally Astrocade
Program Development (BAPD) tool.

It defines constants for file paths and default settings,
ensuring a consistent and organized way to manage configuration
throughout the application.
"""

import os

# BAPD Base Directory
BASE_DIR = os.path.join(os.environ['USERPROFILE'], "BAPD")

# Program Directories (Not changeable by user)
PROGRAMS_DIR = os.path.join(BASE_DIR, "_Programs")
PROJECT_DIR = os.path.join(BASE_DIR, "Projects")
CONFIG_DIR = os.path.join(PROGRAMS_DIR, "Config")

# Settings File
TOML_FILE_NAME = "BAPD_settings.toml"
TOML_FULL_PATH = os.path.join(CONFIG_DIR, TOML_FILE_NAME)

# Default Paths (Used if not specified in settings)
DEFAULT_ZMAC_PATH = os.path.join(PROGRAMS_DIR, "Zmac", "zmac.exe")
DEFAULT_MAME_PATH = os.path.join(PROGRAMS_DIR, "MAME", "mame64.exe")

DEFAULT_ORIGINAL_MAME_ROMS_PATH = os.path.join(PROGRAMS_DIR, "ROMS")
DEFAULT_PROJECT_PATH = os.path.join(PROJECT_DIR, "Astrocade_Program")
DEFAULT_SOURCE_NAME = "Astrocade_Program.asm"

# Other constants
ZMAC_NOT_FOUND = 'ZMAC NOT FOUND'

# Define default settings in a global variable or a separate module
DEFAULT_SETTINGS = {
    "project": {
        "path": DEFAULT_PROJECT_PATH,
        "source_file_name": DEFAULT_SOURCE_NAME,
    },
    "zmac": {
        "path": "",
        "output_hex_file": False,
        "expand_macros": False,
        "expand_include_files": False,
        "expand_if": False,
        "omit_symbol_table": False,
        "allow_8080_instructions": False,
    },
    "mame": {
        "path": "",
        "debug_mode": False,
        "window_mode": True,
        "skip_game_info": True,
        "bally_pro_arcade": True,
        "bally_home_library_computer": False,
        "bally_computer_system": False,
    },
}

# *************************************************************************
# Directory tree structure that will be used to validate
# the default directory and files. Files will be pulled from
# the config/Default_Files directory. The easiest way to modify this
# structure is to tell and AI what you need modified.
# *************************************************************************

DIRECTORY_TREE = {
    "BAPDTest": {       # Change this before put into production.
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
            "MAME": {},
            "PSPad": {
                "files": ["Z80.INI"]
            },
            "Zmac": {
                "files": ["zmac.exe"]
            }
        }
    }
}

