#!/usr/bin/env python
# coding=utf-8

import os

from PyQt4 import QtGui, QtCore

from audio.ui.settingstab import Ui_settingsTab
from audio.core import Registry, Settings


class SettingsTab(QtGui.QWidget, Ui_settingsTab):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        super(SettingsTab, self).__init__(parent, f)

        self.setupUi(self)

        self.recorder = Registry().get('recorder')

        self.saveSettings.clicked.connect(self.savesettings)
        self.browseRecordingDirectory.clicked.connect(self.loaddirectory)
        self.resetRecordingDirectory.clicked.connect(self.reset)
        self.resetRecordingFilename.clicked.connect(self.reset)

        Registry().register('settings_tab', self)

    def savesettings(self):
        settings = Settings()
        settings.setValue("MonitorCheckBox", QtCore.QVariant(self.monitorAudio.isChecked()))
        settings.setValue("RecordingSampleRate", QtCore.QVariant(self.recordingSampleRate.currentText()))
        settings.setValue("RecordingDirectory", QtCore.QVariant(self.recordingDirectory.text()))
        settings.setValue("RecordingFilename", QtCore.QVariant(self.recordingFilename.text()))
        self.recorder.load()

    def loaddirectory(self):
        oldrecordingdirector = str(self.recordingDirectory.text())
        newrecordingdirectory = str(QtGui.QFileDialog.getExistingDirectory(self, 'Set Directory', oldrecordingdirector,
                                                                           QtGui.QFileDialog.ShowDirsOnly))
        if newrecordingdirectory:
            newrecordingdirectory = os.path.normpath(newrecordingdirectory)
            if oldrecordingdirector.lower() == newrecordingdirectory.lower():
                return
        else:
            return

        self.recordingDirectory.setText(newrecordingdirectory)

    def reset(self):
        settings = Settings()
        button = self.sender().objectName()
        if button == 'resetRecordingDirectory':
            default_setting = settings.getDefault('RecordingDirectory')
            self.recordingDirectory.setText(default_setting)
        elif button == 'resetRecordingFilename':
            default_setting = settings.getDefault('RecordingFilename')
            self.recordingFilename.setText(default_setting)
