#!/usr/bin/env python
# coding=utf-8

from PyQt4 import QtGui, QtCore

from audio.ui.settingstab import Ui_settingsTab


class SettingsTab(QtGui.QWidget, Ui_settingsTab):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        super(SettingsTab, self).__init__(parent, f)

        self.setupUi(self)

        self.monitorAudio.clicked.connect(self.savesettings)

    def loadsettings(self):
        print(1)
        settings = QtCore.QSettings()
        print(settings.value("MonitorCheckBox").toBool())
        print(self.monitorAudio.isChecked())
        self.monitorAudio.setChecked(settings.value("MonitorCheckBox").toBool())
        print(self.monitorAudio.isChecked())

    def savesettings(self):
        print(2)
        settings = QtCore.QSettings()
        print(settings.value("MonitorCheckBox").toBool())
        print(self.monitorAudio.isChecked())
        settings.setValue("MonitorCheckBox", QtCore.QVariant(self.monitorAudio.isChecked()))
        print(self.monitorAudio.isChecked())
