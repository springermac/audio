# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Feb 18 23:30:34 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(378, 426)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_6 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.recordingTab = QtGui.QWidget()
        self.recordingTab.setObjectName(_fromUtf8("recordingTab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.recordingTab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.audioMeter = QtGui.QProgressBar(self.recordingTab)
        self.audioMeter.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audioMeter.sizePolicy().hasHeightForWidth())
        self.audioMeter.setSizePolicy(sizePolicy)
        self.audioMeter.setMinimumSize(QtCore.QSize(40, 295))
        self.audioMeter.setProperty("value", 100)
        self.audioMeter.setTextVisible(False)
        self.audioMeter.setOrientation(QtCore.Qt.Vertical)
        self.audioMeter.setInvertedAppearance(True)
        self.audioMeter.setObjectName(_fromUtf8("audioMeter"))
        self.gridLayout_2.addWidget(self.audioMeter, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_2 = QtGui.QFrame(self.recordingTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_8 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.pushButton = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_8.addWidget(self.pushButton, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem2, 0, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_8.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.recordingTab, _fromUtf8(""))
        self.burnTab = QtGui.QWidget()
        self.burnTab.setObjectName(_fromUtf8("burnTab"))
        self.tabWidget.addTab(self.burnTab, _fromUtf8(""))
        self.settingsTab = QtGui.QWidget()
        self.settingsTab.setObjectName(_fromUtf8("settingsTab"))
        self.gridLayout_4 = QtGui.QGridLayout(self.settingsTab)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 1, 1, 1)
        self.monitorAudio = QtGui.QCheckBox(self.settingsTab)
        self.monitorAudio.setChecked(True)
        self.monitorAudio.setObjectName(_fromUtf8("monitorAudio"))
        self.gridLayout_4.addWidget(self.monitorAudio, 0, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem5, 1, 0, 1, 1)
        self.tabWidget.addTab(self.settingsTab, _fromUtf8(""))
        self.gridLayout_6.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 378, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName(_fromUtf8("menu_Edit"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName(_fromUtf8("menu_View"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_Save = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/filesave.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Save.setIcon(icon)
        self.action_Save.setObjectName(_fromUtf8("action_Save"))
        self.actionSave_As = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/filesaveas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon1)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.action_Quit = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/filequit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Quit.setIcon(icon2)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName(_fromUtf8("action_About"))
        self.action_Help = QtGui.QAction(MainWindow)
        self.action_Help.setObjectName(_fromUtf8("action_Help"))
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.actionSave_As)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_Help.addAction(self.action_About)
        self.menu_Help.addAction(self.action_Help)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Audio", None))
        self.pushButton.setText(_translate("MainWindow", "Record", None))
        self.pushButton_2.setText(_translate("MainWindow", "Stop", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recordingTab), _translate("MainWindow", "Record", None))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.recordingTab), _translate("MainWindow", "Record Audio", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.burnTab), _translate("MainWindow", "Burn", None))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.burnTab), _translate("MainWindow", "Burn a CD", None))
        self.monitorAudio.setText(_translate("MainWindow", "Monitor Audio", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), _translate("MainWindow", "Settings", None))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.settingsTab), _translate("MainWindow", "Change Settings", None))
        self.menu_File.setTitle(_translate("MainWindow", "&File", None))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit", None))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help", None))
        self.menu_View.setTitle(_translate("MainWindow", "&View", None))
        self.action_Save.setText(_translate("MainWindow", "&Save", None))
        self.action_Save.setStatusTip(_translate("MainWindow", "Save", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save &As...", None))
        self.actionSave_As.setStatusTip(_translate("MainWindow", "Save As", None))
        self.action_Quit.setText(_translate("MainWindow", "&Quit", None))
        self.action_About.setText(_translate("MainWindow", "&About", None))
        self.action_About.setStatusTip(_translate("MainWindow", "About", None))
        self.action_Help.setText(_translate("MainWindow", "&Help", None))
        self.action_Help.setStatusTip(_translate("MainWindow", "Help", None))

import resources_rc
