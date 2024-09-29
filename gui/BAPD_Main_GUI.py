# BAPD_Main_GUI.py
# 09/28/2024
# Currently displays but needs tweaking
# The AI made it where it would resize.

import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QCursor
from PySide6.QtWidgets import (
    QCheckBox, QFrame, QHBoxLayout, QLabel, QPushButton,
    QPlainTextEdit, QSizePolicy, QStatusBar, QVBoxLayout, QWidget
)


class MainWindowGUI(object):
    def __init__(self):
        # Initialize attributes
        self.centralwidget = None
        self.select_project_button = None
        self.open_folder_button = None
        self.edit_source_button = None
        self.view_listing_button = None
        self.compile_button = None
        self.run_current_button = None
        self.clear_screen_button = None
        self.settings_button = None
        self.run_standard_mame_button = None
        self.version_button = None
        self.filename_label = None
        self.mame_debug_checkbox = None
        self.plain_text_edit = None
        self.statusbar = None

    def setup_ui(self, main_window):
        main_window.setWindowTitle("BAPD - Bally Astrocade Program Development")
        main_window.resize(800, 600)  # Set a default size
        self.centralwidget = QWidget(main_window)
        main_layout = QVBoxLayout(self.centralwidget)

        # Top section
        top_layout = QHBoxLayout()
        self.select_project_button = self.create_button("Select\nProject", font_size=11)
        top_layout.addWidget(self.select_project_button)

        self.filename_label = QLabel("Astrocade_Program.asm")
        font = QFont("Comic Sans MS", 16)
        font.setBold(True)
        self.filename_label.setFont(font)
        self.filename_label.setFrameShape(QFrame.Shape.Box)
        self.filename_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        top_layout.addWidget(self.filename_label)

        self.open_folder_button = self.create_button("Open\nProject\nFolder", font_size=10)
        top_layout.addWidget(self.open_folder_button)
        main_layout.addLayout(top_layout)

        # Editing section
        edit_layout = QHBoxLayout()
        edit_buttons = [
            ("edit_source_button", "Edit Source"),
            ("view_listing_button", "View Listing"),
            ("compile_button", "Compile"),
            ("run_current_button", "Run Current")
        ]
        for attr_name, text in edit_buttons:
            button = self.create_button(text)
            edit_layout.addWidget(button)
            setattr(self, attr_name, button)

        # Set cursor for Edit Source button
        self.edit_source_button.setCursor(QCursor(Qt.CursorShape.IBeamCursor))

        self.mame_debug_checkbox = QCheckBox("MAME\nDebug")
        checkbox_font = QFont("Comic Sans MS", 12)
        checkbox_font.setBold(True)
        self.mame_debug_checkbox.setFont(checkbox_font)
        edit_layout.addWidget(self.mame_debug_checkbox)
        main_layout.addLayout(edit_layout)

        # Text editor
        self.plain_text_edit = QPlainTextEdit()
        self.plain_text_edit.setFont(QFont("Consolas", 12))
        self.plain_text_edit.setReadOnly(True)
        self.plain_text_edit.setPlainText("Your code will appear here.")
        main_layout.addWidget(self.plain_text_edit)

        # Bottom section
        bottom_layout = QHBoxLayout()
        bottom_buttons = [
            ("clear_screen_button", "Clear Screen"),
            ("settings_button", "Settings"),
            ("run_standard_mame_button", "Run Standard\nMAME"),
            ("version_button", "Version")
        ]
        for attr_name, text in bottom_buttons:
            button = self.create_button(text)
            bottom_layout.addWidget(button)
            setattr(self, attr_name, button)
        main_layout.addLayout(bottom_layout)

        # Set central widget and status bar
        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(main_window)
        main_window.setStatusBar(self.statusbar)
        self.statusbar.showMessage("Ready")

    @staticmethod
    def create_button(text, font_size=12):
        button = QPushButton(text)
        font = QFont("Comic Sans MS", font_size)
        font.setBold(True)
        button.setFont(font)
        button.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        return button


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainWindowGUI()
        self.ui.setup_ui(self)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
