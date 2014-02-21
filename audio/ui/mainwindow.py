# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jonathanspringer/projects/audio/audio_program/audio/resources/mainwindow.ui'
#
# Created: Fri Feb 21 02:32:34 2014
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
        MainWindow.resize(240, 240)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_6 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.recordingTab = RecordingTab()
        self.recordingTab.setObjectName(_fromUtf8("recordingTab"))
        self.tabWidget.addTab(self.recordingTab, _fromUtf8(""))
        self.burnTab = BurnTab()
        self.burnTab.setObjectName(_fromUtf8("burnTab"))
        self.tabWidget.addTab(self.burnTab, _fromUtf8(""))
        self.settingsTab = SettingsTab()
        self.settingsTab.setObjectName(_fromUtf8("settingsTab"))
        self.tabWidget.addTab(self.settingsTab, _fromUtf8(""))
        self.gridLayout_6.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 240, 22))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recordingTab), _translate("MainWindow", "Record", None))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.recordingTab), _translate("MainWindow", "Record Audio", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.burnTab), _translate("MainWindow", "Burn", None))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.burnTab), _translate("MainWindow", "Burn a CD", None))
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

from settingstabform import SettingsTab
from recordingtabform import RecordingTab
from burntabform import BurnTab
import resources_rc
