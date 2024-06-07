# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BAPD_Main_GUI.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 817)
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(12)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.compileButton = QPushButton(self.centralwidget)
        self.compileButton.setObjectName(u"compileButton")
        self.compileButton.setGeometry(QRect(360, 120, 140, 50))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.compileButton.sizePolicy().hasHeightForWidth())
        self.compileButton.setSizePolicy(sizePolicy)
        self.compileButton.setFont(font)
        self.editSourceButton = QPushButton(self.centralwidget)
        self.editSourceButton.setObjectName(u"editSourceButton")
        self.editSourceButton.setGeometry(QRect(40, 120, 140, 50))
        sizePolicy.setHeightForWidth(self.editSourceButton.sizePolicy().hasHeightForWidth())
        self.editSourceButton.setSizePolicy(sizePolicy)
        self.editSourceButton.setFont(font)
        self.editSourceButton.setCursor(QCursor(Qt.IBeamCursor))
        self.runCurrentButton = QPushButton(self.centralwidget)
        self.runCurrentButton.setObjectName(u"runCurrentButton")
        self.runCurrentButton.setGeometry(QRect(520, 120, 140, 50))
        sizePolicy.setHeightForWidth(self.runCurrentButton.sizePolicy().hasHeightForWidth())
        self.runCurrentButton.setSizePolicy(sizePolicy)
        self.runCurrentButton.setFont(font)
        self.mameDebugCheckBox = QCheckBox(self.centralwidget)
        self.mameDebugCheckBox.setObjectName(u"mameDebugCheckBox")
        self.mameDebugCheckBox.setGeometry(QRect(670, 120, 81, 50))
        self.mameDebugCheckBox.setFont(font)
        self.versionPushButton = QPushButton(self.centralwidget)
        self.versionPushButton.setObjectName(u"versionPushButton")
        self.versionPushButton.setGeometry(QRect(600, 760, 161, 24))
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(9)
        font1.setBold(False)
        self.versionPushButton.setFont(font1)
        self.versionPushButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.versionPushButton.setFlat(True)
        self.viewListingButton = QPushButton(self.centralwidget)
        self.viewListingButton.setObjectName(u"viewListingButton")
        self.viewListingButton.setGeometry(QRect(200, 120, 140, 50))
        sizePolicy.setHeightForWidth(self.viewListingButton.sizePolicy().hasHeightForWidth())
        self.viewListingButton.setSizePolicy(sizePolicy)
        self.viewListingButton.setFont(font)
        self.viewListingButton.setCursor(QCursor(Qt.IBeamCursor))
        self.clearScreenButton = QPushButton(self.centralwidget)
        self.clearScreenButton.setObjectName(u"clearScreenButton")
        self.clearScreenButton.setGeometry(QRect(300, 690, 191, 51))
        self.clearScreenButton.setFont(font)
        self.clearScreenButton.setAutoDefault(True)
        self.runStandardMameButton = QPushButton(self.centralwidget)
        self.runStandardMameButton.setObjectName(u"runStandardMameButton")
        self.runStandardMameButton.setGeometry(QRect(610, 690, 140, 50))
        self.runStandardMameButton.setFont(font)
        self.runStandardMameButton.setAutoDefault(True)
        self.selectProjectButton = QPushButton(self.centralwidget)
        self.selectProjectButton.setObjectName(u"selectProjectButton")
        self.selectProjectButton.setGeometry(QRect(30, 30, 75, 61))
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.selectProjectButton.setFont(font2)
        self.openProjectFolderButton = QPushButton(self.centralwidget)
        self.openProjectFolderButton.setObjectName(u"openProjectFolderButton")
        self.openProjectFolderButton.setGeometry(QRect(690, 30, 75, 61))
        font3 = QFont()
        font3.setFamilies([u"Comic Sans MS"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.openProjectFolderButton.setFont(font3)
        self.fileNameLabel = QLabel(self.centralwidget)
        self.fileNameLabel.setObjectName(u"fileNameLabel")
        self.fileNameLabel.setGeometry(QRect(128, 30, 531, 61))
        font4 = QFont()
        font4.setFamilies([u"Comic Sans MS"])
        font4.setPointSize(16)
        font4.setBold(True)
        self.fileNameLabel.setFont(font4)
        self.fileNameLabel.setFrameShape(QFrame.Shape.Box)
        self.fileNameLabel.setFrameShadow(QFrame.Shadow.Plain)
        self.fileNameLabel.setLineWidth(2)
        self.fileNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(23, 200, 751, 471))
        font5 = QFont()
        font5.setFamilies([u"Consolas"])
        font5.setPointSize(12)
        font5.setBold(False)
        self.plainTextEdit.setFont(font5)
        self.plainTextEdit.setReadOnly(True)
        self.settingsButton = QPushButton(self.centralwidget)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setGeometry(QRect(40, 690, 140, 50))
        self.settingsButton.setFont(font)
        self.settingsButton.setAutoDefault(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"BAPD - Bally Astrocade Program Development", None))
        self.compileButton.setText(QCoreApplication.translate("MainWindow", u"Compile", None))
        self.editSourceButton.setText(QCoreApplication.translate("MainWindow", u"Edit Source", None))
        self.runCurrentButton.setText(QCoreApplication.translate("MainWindow", u"Run Current", None))
        self.mameDebugCheckBox.setText(QCoreApplication.translate("MainWindow", u"MAME \n"
"Debug", None))
        self.versionPushButton.setText("")
        self.viewListingButton.setText(QCoreApplication.translate("MainWindow", u"View Listing ", None))
        self.clearScreenButton.setText(QCoreApplication.translate("MainWindow", u"Clear Screen", None))
        self.runStandardMameButton.setText(QCoreApplication.translate("MainWindow", u"Run Standard\n"
"MAME", None))
        self.selectProjectButton.setText(QCoreApplication.translate("MainWindow", u"Select\n"
"Project", None))
        self.openProjectFolderButton.setText(QCoreApplication.translate("MainWindow", u"Open\n"
"Project\n"
"Folder", None))
        self.fileNameLabel.setText(QCoreApplication.translate("MainWindow", u"Astrocade_Program.asm", None))
        self.settingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

