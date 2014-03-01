#!/usr/bin/env python
# coding=utf-8

import os

from PyQt4 import QtGui, QtCore

from audio.ui.settingstab import Ui_settingsTab
from audio.player.recorder import Recorder


class SettingsTab(QtGui.QWidget, Ui_settingsTab):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        super(SettingsTab, self).__init__(parent, f)

        self.setupUi(self)

        self.recorder = Recorder()

        self.saveSettings.clicked.connect(self.savesettings)
        self.browseOutputDirectory.clicked.connect(self.loaddirectory)

    def savesettings(self):
        settings = QtCore.QSettings()
        settings.setValue("MonitorCheckBox", QtCore.QVariant(self.monitorAudio.isChecked()))
        settings.setValue("RecordingSampleRate", QtCore.QVariant(self.recordingSampleRate.currentText()))
        settings.setValue("RecordingDirectory", QtCore.QVariant(self.outputLocation.text()))
        settings.setValue("RecordingFilename", QtCore.QVariant(self.outputFileName.text()))
        self.recorder.load()

    def loaddirectory(self):
        oldrecordingdirector = str(self.outputLocation.text())
        newrecordingdirectory = str(QtGui.QFileDialog.getExistingDirectory(self, 'Set Directory', oldrecordingdirector,
                                                                       QtGui.QFileDialog.ShowDirsOnly))
        if newrecordingdirectory:
            newrecordingdirectory = os.path.normpath(newrecordingdirectory)
            if oldrecordingdirector.lower() == newrecordingdirectory.lower():
                return
        else:
            return

        self.outputLocation.setText(newrecordingdirectory)
