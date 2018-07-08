# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jonathanspringer/projects/audio/audio/resources/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(188, 108)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.recordingTab = RecordingTab()
        self.recordingTab.setObjectName("recordingTab")
        self.tabWidget.addTab(self.recordingTab, "")
        self.burnTab = BurnTab()
        self.burnTab.setObjectName("burnTab")
        self.tabWidget.addTab(self.burnTab, "")
        self.settingsTab = SettingsTab()
        self.settingsTab.setObjectName("settingsTab")
        self.tabWidget.addTab(self.settingsTab, "")
        self.gridLayout_6.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 188, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        self.menu_View = QtWidgets.QMenu(self.menubar)
        self.menu_View.setObjectName("menu_View")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Save = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/filesave.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Save.setIcon(icon)
        self.action_Save.setObjectName("action_Save")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/filesaveas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon1)
        self.actionSave_As.setObjectName("actionSave_As")
        self.action_Quit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/filequit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Quit.setIcon(icon2)
        self.action_Quit.setObjectName("action_Quit")
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.action_Help = QtWidgets.QAction(MainWindow)
        self.action_Help.setObjectName("action_Help")
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
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Audio"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recordingTab), _translate("MainWindow", "Record"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.recordingTab), _translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Record Audio</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.burnTab), _translate("MainWindow", "Burn"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.burnTab), _translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Burn a CD</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.settingsTab), _translate("MainWindow", "Settings"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.settingsTab), _translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Change Settings</span></p></body></html>"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit"))
        self.menu_Help.setTitle(_translate("MainWindow", "&Help"))
        self.menu_View.setTitle(_translate("MainWindow", "&View"))
        self.action_Save.setText(_translate("MainWindow", "&Save"))
        self.action_Save.setStatusTip(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save &As..."))
        self.actionSave_As.setStatusTip(_translate("MainWindow", "Save As"))
        self.action_Quit.setText(_translate("MainWindow", "&Quit"))
        self.action_About.setText(_translate("MainWindow", "&About"))
        self.action_About.setStatusTip(_translate("MainWindow", "About"))
        self.action_Help.setText(_translate("MainWindow", "&Help"))
        self.action_Help.setStatusTip(_translate("MainWindow", "Help"))

from audio.ui.burntabform import BurnTab
from audio.ui.recordingtabform import RecordingTab
from audio.ui.settingstabform import SettingsTab
from . import resources_rc
