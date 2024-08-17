# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BAPD_Settings_GUI.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QButtonGroup, QCheckBox,
    QDialog, QDialogButtonBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_BAPD_Settings(object):
    def setupUi(self, BAPD_Settings):
        if not BAPD_Settings.objectName():
            BAPD_Settings.setObjectName(u"BAPD_Settings")
        BAPD_Settings.resize(915, 615)
        self.horizontalLayout = QHBoxLayout(BAPD_Settings)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.settingsTabWidget = QTabWidget(BAPD_Settings)
        self.settingsTabWidget.setObjectName(u"settingsTabWidget")
        self.settingsTabWidget.setStyleSheet(u"QTabBar::tab {\n"
"    height: 30px; /* Adjust tab height */\n"
"    width: 120px; /* Adjust tab width */\n"
"}\n"
"")
        self.settingsTabWidget.setUsesScrollButtons(False)
        self.zmacTab = QWidget()
        self.zmacTab.setObjectName(u"zmacTab")
        self.zmacTab.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.gridLayout = QGridLayout(self.zmacTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.zmacSettingsLayout = QGroupBox(self.zmacTab)
        self.zmacSettingsLayout.setObjectName(u"zmacSettingsLayout")
        self.zmacSettingsLayout.setEnabled(True)
        font = QFont()
        font.setPointSize(14)
        self.zmacSettingsLayout.setFont(font)
        self.zmacSettingsLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.zmacSettingsLayout.setFlat(False)
        self.zmacOptionsGroupBox = QGroupBox(self.zmacSettingsLayout)
        self.zmacOptionsGroupBox.setObjectName(u"zmacOptionsGroupBox")
        self.zmacOptionsGroupBox.setGeometry(QRect(20, 210, 311, 319))
        self.gridLayout_2 = QGridLayout(self.zmacOptionsGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.zmacOptionsVerticalLayout = QVBoxLayout()
        self.zmacOptionsVerticalLayout.setSpacing(17)
        self.zmacOptionsVerticalLayout.setObjectName(u"zmacOptionsVerticalLayout")
        self.outputHexFile = QCheckBox(self.zmacOptionsGroupBox)
        self.outputHexFile.setObjectName(u"outputHexFile")
        self.outputHexFile.setEnabled(False)
        font1 = QFont()
        font1.setPointSize(12)
        self.outputHexFile.setFont(font1)

        self.zmacOptionsVerticalLayout.addWidget(self.outputHexFile)

        self.expandMacros = QCheckBox(self.zmacOptionsGroupBox)
        self.expandMacros.setObjectName(u"expandMacros")
        self.expandMacros.setEnabled(False)
        self.expandMacros.setFont(font1)

        self.zmacOptionsVerticalLayout.addWidget(self.expandMacros)

        self.expandIncludeFiles = QCheckBox(self.zmacOptionsGroupBox)
        self.expandIncludeFiles.setObjectName(u"expandIncludeFiles")
        self.expandIncludeFiles.setEnabled(False)
        self.expandIncludeFiles.setFont(font1)

        self.zmacOptionsVerticalLayout.addWidget(self.expandIncludeFiles)

        self.expandIf = QCheckBox(self.zmacOptionsGroupBox)
        self.expandIf.setObjectName(u"expandIf")
        self.expandIf.setEnabled(False)
        self.expandIf.setFont(font1)

        self.zmacOptionsVerticalLayout.addWidget(self.expandIf)

        self.omitSymbolTable = QCheckBox(self.zmacOptionsGroupBox)
        self.omitSymbolTable.setObjectName(u"omitSymbolTable")
        self.omitSymbolTable.setEnabled(False)
        self.omitSymbolTable.setFont(font1)

        self.zmacOptionsVerticalLayout.addWidget(self.omitSymbolTable)

        self.allow8080Instructions = QCheckBox(self.zmacOptionsGroupBox)
        self.allow8080Instructions.setObjectName(u"allow8080Instructions")
        self.allow8080Instructions.setEnabled(False)
        self.allow8080Instructions.setFont(font1)

        self.zmacOptionsVerticalLayout.addWidget(self.allow8080Instructions)


        self.gridLayout_2.addLayout(self.zmacOptionsVerticalLayout, 0, 0, 1, 1)

        self.zmacVersionLabel = QLabel(self.zmacSettingsLayout)
        self.zmacVersionLabel.setObjectName(u"zmacVersionLabel")
        self.zmacVersionLabel.setEnabled(False)
        self.zmacVersionLabel.setGeometry(QRect(650, 40, 221, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zmacVersionLabel.sizePolicy().hasHeightForWidth())
        self.zmacVersionLabel.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(11)
        self.zmacVersionLabel.setFont(font2)
        self.zmacVersionLabel.setFrameShape(QFrame.Shape.Box)
        self.zmacVersionLabel.setScaledContents(False)
        self.zmacVersionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.zmacFilePathLayout = QGroupBox(self.zmacSettingsLayout)
        self.zmacFilePathLayout.setObjectName(u"zmacFilePathLayout")
        self.zmacFilePathLayout.setGeometry(QRect(20, 90, 851, 101))
        self.zmacFilePathLayout.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.gridLayout_3 = QGridLayout(self.zmacFilePathLayout)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.zmacPathInputLayout = QHBoxLayout()
        self.zmacPathInputLayout.setObjectName(u"zmacPathInputLayout")
        self.zmacPathLabel = QLabel(self.zmacFilePathLayout)
        self.zmacPathLabel.setObjectName(u"zmacPathLabel")

        self.zmacPathInputLayout.addWidget(self.zmacPathLabel)

        self.zmacPathLineEdit = QLineEdit(self.zmacFilePathLayout)
        self.zmacPathLineEdit.setObjectName(u"zmacPathLineEdit")
        self.zmacPathLineEdit.setEnabled(False)

        self.zmacPathInputLayout.addWidget(self.zmacPathLineEdit)

        self.zmacBrowseButton = QPushButton(self.zmacFilePathLayout)
        self.zmacBrowseButton.setObjectName(u"zmacBrowseButton")
        self.zmacBrowseButton.setEnabled(False)
        self.zmacBrowseButton.setFont(font1)
        self.zmacBrowseButton.setAutoDefault(True)

        self.zmacPathInputLayout.addWidget(self.zmacBrowseButton)


        self.gridLayout_3.addLayout(self.zmacPathInputLayout, 0, 0, 1, 1)

        self.zmacButtonBox = QDialogButtonBox(self.zmacSettingsLayout)
        self.zmacButtonBox.setObjectName(u"zmacButtonBox")
        self.zmacButtonBox.setEnabled(False)
        self.zmacButtonBox.setGeometry(QRect(620, 510, 241, 31))
        font3 = QFont()
        font3.setPointSize(13)
        self.zmacButtonBox.setFont(font3)
        self.zmacButtonBox.setStandardButtons(QDialogButtonBox.StandardButton.Apply|QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.zmacButtonBox.setCenterButtons(True)
        self.zmacCommandLineGroupBox = QGroupBox(self.zmacSettingsLayout)
        self.zmacCommandLineGroupBox.setObjectName(u"zmacCommandLineGroupBox")
        self.zmacCommandLineGroupBox.setGeometry(QRect(350, 210, 521, 91))
        self.layoutWidget = QWidget(self.zmacCommandLineGroupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 501, 41))
        self.zmacCommandLineHorzBoxLayout = QHBoxLayout(self.layoutWidget)
        self.zmacCommandLineHorzBoxLayout.setObjectName(u"zmacCommandLineHorzBoxLayout")
        self.zmacCommandLineHorzBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.zmacCommandLineDisplayLabel = QLabel(self.layoutWidget)
        self.zmacCommandLineDisplayLabel.setObjectName(u"zmacCommandLineDisplayLabel")
        self.zmacCommandLineDisplayLabel.setFont(font1)
        self.zmacCommandLineDisplayLabel.setFrameShape(QFrame.Shape.StyledPanel)

        self.zmacCommandLineHorzBoxLayout.addWidget(self.zmacCommandLineDisplayLabel)


        self.gridLayout.addWidget(self.zmacSettingsLayout, 0, 0, 1, 1)

        self.settingsTabWidget.addTab(self.zmacTab, "")
        self.mameTab = QWidget()
        self.mameTab.setObjectName(u"mameTab")
        self.mameTab.setFont(font1)
        self.gridLayout_6 = QGridLayout(self.mameTab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.mameSettingsLayout = QGroupBox(self.mameTab)
        self.mameSettingsLayout.setObjectName(u"mameSettingsLayout")
        self.mameSettingsLayout.setFont(font)
        self.mameSettingsLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mameSettingsLayout.setFlat(False)
        self.mameFilePathLayout = QGroupBox(self.mameSettingsLayout)
        self.mameFilePathLayout.setObjectName(u"mameFilePathLayout")
        self.mameFilePathLayout.setGeometry(QRect(20, 90, 851, 101))
        self.mameFilePathLayout.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.gridLayout_5 = QGridLayout(self.mameFilePathLayout)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.mamePathInputLayout = QHBoxLayout()
        self.mamePathInputLayout.setObjectName(u"mamePathInputLayout")
        self.mamePathLabel = QLabel(self.mameFilePathLayout)
        self.mamePathLabel.setObjectName(u"mamePathLabel")

        self.mamePathInputLayout.addWidget(self.mamePathLabel)

        self.mamePathLineEdit = QLineEdit(self.mameFilePathLayout)
        self.mamePathLineEdit.setObjectName(u"mamePathLineEdit")
        self.mamePathLineEdit.setEnabled(False)

        self.mamePathInputLayout.addWidget(self.mamePathLineEdit)

        self.mameBrowseButton = QPushButton(self.mameFilePathLayout)
        self.mameBrowseButton.setObjectName(u"mameBrowseButton")
        self.mameBrowseButton.setEnabled(False)
        self.mameBrowseButton.setFont(font1)
        self.mameBrowseButton.setAutoDefault(True)

        self.mamePathInputLayout.addWidget(self.mameBrowseButton)


        self.gridLayout_5.addLayout(self.mamePathInputLayout, 0, 0, 1, 1)

        self.mameButtonBox = QDialogButtonBox(self.mameSettingsLayout)
        self.mameButtonBox.setObjectName(u"mameButtonBox")
        self.mameButtonBox.setGeometry(QRect(620, 510, 241, 31))
        self.mameButtonBox.setFont(font3)
        self.mameButtonBox.setStandardButtons(QDialogButtonBox.StandardButton.Apply|QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.mameButtonBox.setCenterButtons(True)
        self.mameCommandLineGroupBox = QGroupBox(self.mameSettingsLayout)
        self.mameCommandLineGroupBox.setObjectName(u"mameCommandLineGroupBox")
        self.mameCommandLineGroupBox.setGeometry(QRect(350, 210, 521, 91))
        self.layoutWidget_2 = QWidget(self.mameCommandLineGroupBox)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 40, 501, 41))
        self.mameCommandLineHorzBoxLayout = QHBoxLayout(self.layoutWidget_2)
        self.mameCommandLineHorzBoxLayout.setObjectName(u"mameCommandLineHorzBoxLayout")
        self.mameCommandLineHorzBoxLayout.setContentsMargins(0, 0, 0, 0)
        self.mameCommandLineDisplayLabel = QLabel(self.layoutWidget_2)
        self.mameCommandLineDisplayLabel.setObjectName(u"mameCommandLineDisplayLabel")
        self.mameCommandLineDisplayLabel.setFont(font1)
        self.mameCommandLineDisplayLabel.setFrameShape(QFrame.Shape.StyledPanel)

        self.mameCommandLineHorzBoxLayout.addWidget(self.mameCommandLineDisplayLabel)

        self.mameOptionsGroupBox = QGroupBox(self.mameSettingsLayout)
        self.mameOptionsGroupBox.setObjectName(u"mameOptionsGroupBox")
        self.mameOptionsGroupBox.setGeometry(QRect(20, 210, 311, 319))
        self.gridLayout_4 = QGridLayout(self.mameOptionsGroupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.mameOptionsVerticalLayout = QVBoxLayout()
        self.mameOptionsVerticalLayout.setSpacing(17)
        self.mameOptionsVerticalLayout.setObjectName(u"mameOptionsVerticalLayout")
        self.debugModeOn = QCheckBox(self.mameOptionsGroupBox)
        self.debugModeOn.setObjectName(u"debugModeOn")
        self.debugModeOn.setFont(font1)

        self.mameOptionsVerticalLayout.addWidget(self.debugModeOn)

        self.windowModeOn = QCheckBox(self.mameOptionsGroupBox)
        self.windowModeOn.setObjectName(u"windowModeOn")
        self.windowModeOn.setFont(font1)

        self.mameOptionsVerticalLayout.addWidget(self.windowModeOn)

        self.skipGameInfo = QCheckBox(self.mameOptionsGroupBox)
        self.skipGameInfo.setObjectName(u"skipGameInfo")
        self.skipGameInfo.setFont(font1)

        self.mameOptionsVerticalLayout.addWidget(self.skipGameInfo)

        self.ballyProArcade = QRadioButton(self.mameOptionsGroupBox)
        self.buttonGroup = QButtonGroup(BAPD_Settings)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.ballyProArcade)
        self.ballyProArcade.setObjectName(u"ballyProArcade")
        self.ballyProArcade.setFont(font1)

        self.mameOptionsVerticalLayout.addWidget(self.ballyProArcade)

        self.ballyHomeLibraryComputer = QRadioButton(self.mameOptionsGroupBox)
        self.buttonGroup.addButton(self.ballyHomeLibraryComputer)
        self.ballyHomeLibraryComputer.setObjectName(u"ballyHomeLibraryComputer")
        self.ballyHomeLibraryComputer.setFont(font1)

        self.mameOptionsVerticalLayout.addWidget(self.ballyHomeLibraryComputer)

        self.ballyComputerSystem = QRadioButton(self.mameOptionsGroupBox)
        self.buttonGroup.addButton(self.ballyComputerSystem)
        self.ballyComputerSystem.setObjectName(u"ballyComputerSystem")
        self.ballyComputerSystem.setFont(font1)

        self.mameOptionsVerticalLayout.addWidget(self.ballyComputerSystem)


        self.gridLayout_4.addLayout(self.mameOptionsVerticalLayout, 0, 0, 1, 1)

        self.mameVersionLabel = QLabel(self.mameSettingsLayout)
        self.mameVersionLabel.setObjectName(u"mameVersionLabel")
        self.mameVersionLabel.setEnabled(False)
        self.mameVersionLabel.setGeometry(QRect(650, 40, 221, 31))
        sizePolicy.setHeightForWidth(self.mameVersionLabel.sizePolicy().hasHeightForWidth())
        self.mameVersionLabel.setSizePolicy(sizePolicy)
        self.mameVersionLabel.setFont(font2)
        self.mameVersionLabel.setFrameShape(QFrame.Shape.Box)
        self.mameVersionLabel.setScaledContents(False)
        self.mameVersionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.mameSettingsLayout, 0, 0, 1, 1)

        self.settingsTabWidget.addTab(self.mameTab, "")

        self.horizontalLayout.addWidget(self.settingsTabWidget)


        self.retranslateUi(BAPD_Settings)

        self.settingsTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(BAPD_Settings)
    # setupUi

    def retranslateUi(self, BAPD_Settings):
        BAPD_Settings.setWindowTitle(QCoreApplication.translate("BAPD_Settings", u"Settings", None))
        self.zmacSettingsLayout.setTitle(QCoreApplication.translate("BAPD_Settings", u"ZMAC Settings", None))
        self.zmacOptionsGroupBox.setTitle(QCoreApplication.translate("BAPD_Settings", u"Options", None))
        self.outputHexFile.setText(QCoreApplication.translate("BAPD_Settings", u"Produce .hex file as well as .bin", None))
        self.expandMacros.setText(QCoreApplication.translate("BAPD_Settings", u"Expand Macros", None))
        self.expandIncludeFiles.setText(QCoreApplication.translate("BAPD_Settings", u"Expand Include Files ", None))
        self.expandIf.setText(QCoreApplication.translate("BAPD_Settings", u"Expand \"if\" expressions not compiled", None))
        self.omitSymbolTable.setText(QCoreApplication.translate("BAPD_Settings", u"Omit Symbol Table", None))
        self.allow8080Instructions.setText(QCoreApplication.translate("BAPD_Settings", u"Allow 8080 instructions", None))
        self.zmacVersionLabel.setText(QCoreApplication.translate("BAPD_Settings", u"ZMAC Version 3.1", None))
        self.zmacFilePathLayout.setTitle(QCoreApplication.translate("BAPD_Settings", u"File Locations", None))
        self.zmacPathLabel.setText(QCoreApplication.translate("BAPD_Settings", u"ZMAC Path:", None))
        self.zmacBrowseButton.setText(QCoreApplication.translate("BAPD_Settings", u"Browse...", None))
        self.zmacCommandLineGroupBox.setTitle(QCoreApplication.translate("BAPD_Settings", u"Command Line", None))
        self.zmacCommandLineDisplayLabel.setText(QCoreApplication.translate("BAPD_Settings", u"Coming Soon...", None))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.zmacTab), QCoreApplication.translate("BAPD_Settings", u"ZMAC", None))
        self.mameSettingsLayout.setTitle(QCoreApplication.translate("BAPD_Settings", u"MAME Settings", None))
        self.mameFilePathLayout.setTitle(QCoreApplication.translate("BAPD_Settings", u"File Locations", None))
        self.mamePathLabel.setText(QCoreApplication.translate("BAPD_Settings", u"MAME Path:", None))
        self.mameBrowseButton.setText(QCoreApplication.translate("BAPD_Settings", u"Browse...", None))
        self.mameCommandLineGroupBox.setTitle(QCoreApplication.translate("BAPD_Settings", u"Command Line", None))
        self.mameCommandLineDisplayLabel.setText(QCoreApplication.translate("BAPD_Settings", u"Coming soon...", None))
        self.mameOptionsGroupBox.setTitle(QCoreApplication.translate("BAPD_Settings", u"Options", None))
        self.debugModeOn.setText(QCoreApplication.translate("BAPD_Settings", u"Debug Mode ON", None))
        self.windowModeOn.setText(QCoreApplication.translate("BAPD_Settings", u"Start in Window Mode", None))
        self.skipGameInfo.setText(QCoreApplication.translate("BAPD_Settings", u"Skip Game Information on Startup", None))
        self.ballyProArcade.setText(QCoreApplication.translate("BAPD_Settings", u"Bally Professional Arcade", None))
        self.ballyHomeLibraryComputer.setText(QCoreApplication.translate("BAPD_Settings", u"Bally Home Library Computer", None))
        self.ballyComputerSystem.setText(QCoreApplication.translate("BAPD_Settings", u"Bally Computer System", None))
        self.mameVersionLabel.setText(QCoreApplication.translate("BAPD_Settings", u"MAME Version x.x", None))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.mameTab), QCoreApplication.translate("BAPD_Settings", u"MAME", None))
    # retranslateUi

