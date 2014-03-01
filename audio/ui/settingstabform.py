#!/usr/bin/env python
# coding=utf-8

from PyQt4 import QtGui, QtCore

from audio.ui.settingstab import Ui_settingsTab
from audio.player.recorder import Recorder


class SettingsTab(QtGui.QWidget, Ui_settingsTab):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        super(SettingsTab, self).__init__(parent, f)

        self.setupUi(self)

        self.recorder = Recorder()

        self.saveSettings.clicked.connect(self.savesettings)

    def savesettings(self):
        settings = QtCore.QSettings()
        settings.setValue("MonitorCheckBox", QtCore.QVariant(self.monitorAudio.isChecked()))
        settings.setValue("RecordingSampleRate", QtCore.QVariant(self.recordingSampleRate.currentText()))
        self.recorder.load()
