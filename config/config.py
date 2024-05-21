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
BASE_DIR = os.path.join(os.path.expanduser('~'), "BAPD")

# Program Directories (Not changeable by user)
PROGRAMS_DIR = os.path.join(BASE_DIR, "_Programs")
PROJECT_DIR = os.path.join(BASE_DIR, "Projects")
CONFIG_DIR = os.path.join(PROGRAMS_DIR, "Config")

# Settings File
TOML_FILE_NAME = "BAPD_settings.toml"
TOML_FULL_PATH = os.path.join(CONFIG_DIR, TOML_FILE_NAME)

# Default Paths (Used if not specified in settings)
DEFAULT_ZMAC_PATH = os.path.join(PROGRAMS_DIR, "Zmac")
DEFAULT_MAME_PATH = os.path.join(PROGRAMS_DIR, "MAME")
DEFAULT_ORIGINAL_MAME_ROMS_PATH = os.path.join(PROGRAMS_DIR, "ROMS")
DEFAULT_PROJECT_PATH = os.path.join(PROJECT_DIR, "Astrocade_Program")
DEFAULT_SOURCE_NAME = "Astrocade_Program.asm"


# Other constants
ZMAC_NOT_FOUND = 'ZMAC NOT FOUND'