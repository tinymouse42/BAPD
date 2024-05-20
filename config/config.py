# config.py
"""
This file is for holding paths to different aspects of the BAPD project.
These paths will be set to the project directory locations and later they will be
changed to the production locations.
"""

import os

# Project Directories
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))  # Root of the BAPD project
CONFIG_DIR = os.path.join(PROJECT_ROOT, "config")  # Directory for configuration files
PROJECTS_DIR = os.path.join(PROJECT_ROOT, "projects")  # Default directory for user projects

# Settings File
TOML_PATH = os.path.join(CONFIG_DIR, "settings.toml")

# Default Paths for External Tools (Update for your system)
ZMAC_DEFAULT_PATH = "path/to/zmac"  # Replace with the actual path to Zmac
MAME_DEFAULT_PATH = "path/to/mame"  # Replace with the actual path to MAME
