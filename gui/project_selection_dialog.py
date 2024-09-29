# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'project_selection_dialog.gui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGroupBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QSizePolicy, QWidget)

class Ui_projectSelectionDialog(object):
    def setupUi(self, projectSelectionDialog):
        if not projectSelectionDialog.objectName():
            projectSelectionDialog.setObjectName(u"projectSelectionDialog")
        projectSelectionDialog.resize(550, 522)
        self.dialogButtonBox = QDialogButtonBox(projectSelectionDialog)
        self.dialogButtonBox.setObjectName(u"dialogButtonBox")
        self.dialogButtonBox.setGeometry(QRect(320, 470, 201, 32))
        font = QFont()
        font.setPointSize(12)
        self.dialogButtonBox.setFont(font)
        self.dialogButtonBox.setOrientation(Qt.Orientation.Horizontal)
        self.dialogButtonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.existingProjectsGroupBox = QGroupBox(projectSelectionDialog)
        self.existingProjectsGroupBox.setObjectName(u"existingProjectsGroupBox")
        self.existingProjectsGroupBox.setGeometry(QRect(10, 20, 520, 321))
        self.formLayout = QFormLayout(self.existingProjectsGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.existingProjectsListWidget = QListWidget(self.existingProjectsGroupBox)
        self.existingProjectsListWidget.setObjectName(u"existingProjectsListWidget")

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.existingProjectsListWidget)

        self.newProjectGroupBox = QGroupBox(projectSelectionDialog)
        self.newProjectGroupBox.setObjectName(u"newProjectGroupBox")
        self.newProjectGroupBox.setGeometry(QRect(10, 360, 520, 101))
        self.projectNameLabel = QLabel(self.newProjectGroupBox)
        self.projectNameLabel.setObjectName(u"projectNameLabel")
        self.projectNameLabel.setGeometry(QRect(10, 60, 111, 20))
        self.projectNameLabel.setFont(font)
        self.projectNameLineEdit = QLineEdit(self.newProjectGroupBox)
        self.projectNameLineEdit.setObjectName(u"projectNameLineEdit")
        self.projectNameLineEdit.setGeometry(QRect(120, 60, 371, 21))
        self.CreateProjectLabel = QLabel(self.newProjectGroupBox)
        self.CreateProjectLabel.setObjectName(u"CreateProjectLabel")
        self.CreateProjectLabel.setGeometry(QRect(170, 20, 171, 21))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.CreateProjectLabel.setFont(font1)
        self.CreateProjectLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(projectSelectionDialog)
        self.dialogButtonBox.accepted.connect(projectSelectionDialog.accept)
        self.dialogButtonBox.rejected.connect(projectSelectionDialog.reject)

        QMetaObject.connectSlotsByName(projectSelectionDialog)
    # setup_ui

    def retranslateUi(self, projectSelectionDialog):
        projectSelectionDialog.setWindowTitle(QCoreApplication.translate("projectSelectionDialog", u"Select or Create Project", None))
        self.existingProjectsGroupBox.setTitle(QCoreApplication.translate("projectSelectionDialog", u"Existing Projects", None))
        self.newProjectGroupBox.setTitle(QCoreApplication.translate("projectSelectionDialog", u"New Project", None))
        self.projectNameLabel.setText(QCoreApplication.translate("projectSelectionDialog", u"Project Name:", None))
        self.CreateProjectLabel.setText(QCoreApplication.translate("projectSelectionDialog", u"Create New Project", None))
    # retranslateUi

