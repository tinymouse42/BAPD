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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QVBoxLayout, QWidget)

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
        self.settingsTabWidget.setUsesScrollButtons(False)
        self.zmacTab = QWidget()
        self.zmacTab.setObjectName(u"zmacTab")
        self.zmacTab.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.gridLayout = QGridLayout(self.zmacTab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.zmacSettingsLayout = QGroupBox(self.zmacTab)
        self.zmacSettingsLayout.setObjectName(u"zmacSettingsLayout")
        font = QFont()
        font.setPointSize(14)
        self.zmacSettingsLayout.setFont(font)
        self.zmacSettingsLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.zmacSettingsLayout.setFlat(False)
        self.zmacOptionsGroupBox = QGroupBox(self.zmacSettingsLayout)
        self.zmacOptionsGroupBox.setObjectName(u"zmacOptionsGroupBox")
        self.zmacOptionsGroupBox.setGeometry(QRect(20, 210, 222, 319))
        self.gridLayout_2 = QGridLayout(self.zmacOptionsGroupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.zmacOptionsVerticalLayout = QVBoxLayout()
        self.zmacOptionsVerticalLayout.setSpacing(17)
        self.zmacOptionsVerticalLayout.setObjectName(u"zmacOptionsVerticalLayout")
        self.expandIncludeFiles = QCheckBox(self.zmacOptionsGroupBox)
        self.expandIncludeFiles.setObjectName(u"expandIncludeFiles")
        font1 = QFont()
        font1.setPointSize(12)
        self.expandIncludeFiles.setFont(font1)

        self.zmacOptionsVerticalLayout.addWidget(self.expandIncludeFiles)

        self.expandMacros = QCheckBox(self.zmacOptionsGroupBox)
        self.expandMacros.setObjectName(u"expandMacros")
        self.expandMacros.setFont(font1)

        self.zmacOptionsVerticalLayout.addWidget(self.expandMacros)

        self.useUndocumentedInstructions = QCheckBox(self.zmacOptionsGroupBox)
        self.useUndocumentedInstructions.setObjectName(u"useUndocumentedInstructions")
        self.useUndocumentedInstructions.setFont(font1)

        self.zmacOptionsVerticalLayout.addWidget(self.useUndocumentedInstructions)

        self.outputHexFile = QCheckBox(self.zmacOptionsGroupBox)
        self.outputHexFile.setObjectName(u"outputHexFile")
        self.outputHexFile.setFont(font1)

        self.zmacOptionsVerticalLayout.addWidget(self.outputHexFile)

        self.omitSymbolTable = QCheckBox(self.zmacOptionsGroupBox)
        self.omitSymbolTable.setObjectName(u"omitSymbolTable")
        self.omitSymbolTable.setFont(font1)

        self.zmacOptionsVerticalLayout.addWidget(self.omitSymbolTable)

        self.labelsMustHaveColons = QCheckBox(self.zmacOptionsGroupBox)
        self.labelsMustHaveColons.setObjectName(u"labelsMustHaveColons")
        self.labelsMustHaveColons.setFont(font1)

        self.zmacOptionsVerticalLayout.addWidget(self.labelsMustHaveColons)


        self.gridLayout_2.addLayout(self.zmacOptionsVerticalLayout, 0, 0, 1, 1)

        self.zmacVersionButton = QLabel(self.zmacSettingsLayout)
        self.zmacVersionButton.setObjectName(u"zmacVersionButton")
        self.zmacVersionButton.setGeometry(QRect(650, 40, 221, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.zmacVersionButton.sizePolicy().hasHeightForWidth())
        self.zmacVersionButton.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setPointSize(11)
        self.zmacVersionButton.setFont(font2)
        self.zmacVersionButton.setFrameShape(QFrame.Shape.Box)
        self.zmacVersionButton.setScaledContents(False)
        self.zmacVersionButton.setAlignment(Qt.AlignmentFlag.AlignCenter)
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

        self.zmacPathInputLayout.addWidget(self.zmacPathLineEdit)

        self.zmacBrowseButton = QPushButton(self.zmacFilePathLayout)
        self.zmacBrowseButton.setObjectName(u"zmacBrowseButton")
        self.zmacBrowseButton.setFont(font1)
        self.zmacBrowseButton.setAutoDefault(True)

        self.zmacPathInputLayout.addWidget(self.zmacBrowseButton)


        self.gridLayout_3.addLayout(self.zmacPathInputLayout, 0, 0, 1, 1)

        self.buttonBox_2 = QDialogButtonBox(self.zmacSettingsLayout)
        self.buttonBox_2.setObjectName(u"buttonBox_2")
        self.buttonBox_2.setGeometry(QRect(620, 510, 241, 31))
        font3 = QFont()
        font3.setPointSize(13)
        self.buttonBox_2.setFont(font3)
        self.buttonBox_2.setStandardButtons(QDialogButtonBox.StandardButton.Apply|QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox_2.setCenterButtons(True)

        self.gridLayout.addWidget(self.zmacSettingsLayout, 0, 0, 1, 1)

        self.settingsTabWidget.addTab(self.zmacTab, "")
        self.mameTab = QWidget()
        self.mameTab.setObjectName(u"mameTab")
        self.gridLayout_6 = QGridLayout(self.mameTab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.mameSettingsLayout = QGroupBox(self.mameTab)
        self.mameSettingsLayout.setObjectName(u"mameSettingsLayout")
        self.mameSettingsLayout.setFont(font)
        self.mameSettingsLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mameSettingsLayout.setFlat(False)
        self.mameOptionsGroupBox = QGroupBox(self.mameSettingsLayout)
        self.mameOptionsGroupBox.setObjectName(u"mameOptionsGroupBox")
        self.mameOptionsGroupBox.setGeometry(QRect(20, 210, 222, 319))
        self.gridLayout_4 = QGridLayout(self.mameOptionsGroupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
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

        self.mamePathInputLayout.addWidget(self.mamePathLineEdit)

        self.mameBrowseButton = QPushButton(self.mameFilePathLayout)
        self.mameBrowseButton.setObjectName(u"mameBrowseButton")
        self.mameBrowseButton.setFont(font1)
        self.mameBrowseButton.setAutoDefault(True)

        self.mamePathInputLayout.addWidget(self.mameBrowseButton)


        self.gridLayout_5.addLayout(self.mamePathInputLayout, 0, 0, 1, 1)

        self.buttonBox_3 = QDialogButtonBox(self.mameSettingsLayout)
        self.buttonBox_3.setObjectName(u"buttonBox_3")
        self.buttonBox_3.setGeometry(QRect(620, 510, 241, 31))
        self.buttonBox_3.setFont(font3)
        self.buttonBox_3.setStandardButtons(QDialogButtonBox.StandardButton.Apply|QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.buttonBox_3.setCenterButtons(True)

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
        self.expandIncludeFiles.setText(QCoreApplication.translate("BAPD_Settings", u"Expand Include Files", None))
        self.expandMacros.setText(QCoreApplication.translate("BAPD_Settings", u"Expand Macros", None))
        self.useUndocumentedInstructions.setText(QCoreApplication.translate("BAPD_Settings", u"Use Undocumented \n"
"Z80 Instructions", None))
        self.outputHexFile.setText(QCoreApplication.translate("BAPD_Settings", u"Output .hex File", None))
        self.omitSymbolTable.setText(QCoreApplication.translate("BAPD_Settings", u"Omit Symbol Table", None))
        self.labelsMustHaveColons.setText(QCoreApplication.translate("BAPD_Settings", u"Labels Must Have Colons", None))
        self.zmacVersionButton.setText(QCoreApplication.translate("BAPD_Settings", u"ZMAC Version 3.1", None))
        self.zmacFilePathLayout.setTitle(QCoreApplication.translate("BAPD_Settings", u"File Locations", None))
        self.zmacPathLabel.setText(QCoreApplication.translate("BAPD_Settings", u"ZMAC Path:", None))
        self.zmacBrowseButton.setText(QCoreApplication.translate("BAPD_Settings", u"Browse...", None))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.zmacTab), QCoreApplication.translate("BAPD_Settings", u"ZMAC", None))
        self.mameSettingsLayout.setTitle(QCoreApplication.translate("BAPD_Settings", u"MAME Settings", None))
        self.mameOptionsGroupBox.setTitle(QCoreApplication.translate("BAPD_Settings", u"Options", None))
        self.mameFilePathLayout.setTitle(QCoreApplication.translate("BAPD_Settings", u"File Locations", None))
        self.mamePathLabel.setText(QCoreApplication.translate("BAPD_Settings", u"MAME Path:", None))
        self.mameBrowseButton.setText(QCoreApplication.translate("BAPD_Settings", u"Browse...", None))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.mameTab), QCoreApplication.translate("BAPD_Settings", u"MAME", None))
    # retranslateUi

