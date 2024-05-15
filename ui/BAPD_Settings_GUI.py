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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTabWidget, QVBoxLayout,
    QWidget)

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
        self.zmacSettingsLayout = QGroupBox(self.zmacTab)
        self.zmacSettingsLayout.setObjectName(u"zmacSettingsLayout")
        self.zmacSettingsLayout.setGeometry(QRect(20, 20, 871, 541))
        font = QFont()
        font.setPointSize(14)
        self.zmacSettingsLayout.setFont(font)
        self.zmacSettingsLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.zmacSettingsLayout.setFlat(False)
        self.optionsGroupBox = QGroupBox(self.zmacSettingsLayout)
        self.optionsGroupBox.setObjectName(u"optionsGroupBox")
        self.optionsGroupBox.setGeometry(QRect(620, 90, 231, 361))
        self.verticalLayoutWidget = QWidget(self.optionsGroupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 40, 202, 301))
        self.zmacOptionsVerticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.zmacOptionsVerticalLayout.setObjectName(u"zmacOptionsVerticalLayout")
        self.zmacOptionsVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.expandIncludeFiles = QCheckBox(self.verticalLayoutWidget)
        self.expandIncludeFiles.setObjectName(u"expandIncludeFiles")
        font1 = QFont()
        font1.setPointSize(12)
        self.expandIncludeFiles.setFont(font1)

        self.zmacOptionsVerticalLayout.addWidget(self.expandIncludeFiles)

        self.expandMacros = QCheckBox(self.verticalLayoutWidget)
        self.expandMacros.setObjectName(u"expandMacros")
        self.expandMacros.setFont(font1)

        self.zmacOptionsVerticalLayout.addWidget(self.expandMacros)

        self.useUndocumentedInstructions = QCheckBox(self.verticalLayoutWidget)
        self.useUndocumentedInstructions.setObjectName(u"useUndocumentedInstructions")
        self.useUndocumentedInstructions.setFont(font1)

        self.zmacOptionsVerticalLayout.addWidget(self.useUndocumentedInstructions)

        self.outputHexFile = QCheckBox(self.verticalLayoutWidget)
        self.outputHexFile.setObjectName(u"outputHexFile")
        self.outputHexFile.setFont(font1)

        self.zmacOptionsVerticalLayout.addWidget(self.outputHexFile)

        self.omitSymbolTable = QCheckBox(self.verticalLayoutWidget)
        self.omitSymbolTable.setObjectName(u"omitSymbolTable")
        self.omitSymbolTable.setFont(font1)

        self.zmacOptionsVerticalLayout.addWidget(self.omitSymbolTable)

        self.labelsMustHaveColons = QCheckBox(self.verticalLayoutWidget)
        self.labelsMustHaveColons.setObjectName(u"labelsMustHaveColons")
        self.labelsMustHaveColons.setFont(font1)

        self.zmacOptionsVerticalLayout.addWidget(self.labelsMustHaveColons)

        self.zmacVersionButton = QLabel(self.zmacSettingsLayout)
        self.zmacVersionButton.setObjectName(u"zmacVersionButton")
        self.zmacVersionButton.setGeometry(QRect(620, 490, 231, 31))
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
        self.zmacFilePathLayout.setGeometry(QRect(10, 90, 571, 161))
        self.zmacFilePathLayout.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.horizontalLayoutWidget = QWidget(self.zmacFilePathLayout)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 30, 551, 111))
        self.zmacPathInputLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.zmacPathInputLayout.setObjectName(u"zmacPathInputLayout")
        self.zmacPathInputLayout.setContentsMargins(0, 0, 0, 0)
        self.zmacPathLabel = QLabel(self.horizontalLayoutWidget)
        self.zmacPathLabel.setObjectName(u"zmacPathLabel")

        self.zmacPathInputLayout.addWidget(self.zmacPathLabel)

        self.zmacPathLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.zmacPathLineEdit.setObjectName(u"zmacPathLineEdit")

        self.zmacPathInputLayout.addWidget(self.zmacPathLineEdit)

        self.browseZmacButton = QPushButton(self.horizontalLayoutWidget)
        self.browseZmacButton.setObjectName(u"browseZmacButton")
        self.browseZmacButton.setFont(font1)
        self.browseZmacButton.setAutoDefault(True)

        self.zmacPathInputLayout.addWidget(self.browseZmacButton)

        self.settingsTabWidget.addTab(self.zmacTab, "")
        self.mameTab = QWidget()
        self.mameTab.setObjectName(u"mameTab")
        self.settingsTabWidget.addTab(self.mameTab, "")

        self.horizontalLayout.addWidget(self.settingsTabWidget)


        self.retranslateUi(BAPD_Settings)

        self.settingsTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(BAPD_Settings)
    # setupUi

    def retranslateUi(self, BAPD_Settings):
        BAPD_Settings.setWindowTitle(QCoreApplication.translate("BAPD_Settings", u"Settings", None))
        self.zmacSettingsLayout.setTitle(QCoreApplication.translate("BAPD_Settings", u"ZMAC Settings", None))
        self.optionsGroupBox.setTitle(QCoreApplication.translate("BAPD_Settings", u"Options", None))
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
        self.browseZmacButton.setText(QCoreApplication.translate("BAPD_Settings", u"Browse...", None))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.zmacTab), QCoreApplication.translate("BAPD_Settings", u"ZMAC", None))
        self.settingsTabWidget.setTabText(self.settingsTabWidget.indexOf(self.mameTab), QCoreApplication.translate("BAPD_Settings", u"MAME", None))
    # retranslateUi

