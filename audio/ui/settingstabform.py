#!/usr/bin/env python
# coding=utf-8

import os

from PyQt4 import QtGui, QtCore

from audio.ui.settingstab import Ui_settingsTab
from audio.core import Registry, Settings, Utils


class SettingsTab(QtGui.QWidget, Ui_settingsTab):
    __sample_rate__ = [
        8000,
        11025,
        22050,
        32000,
        44100,
        48000,
        96000
    ]

    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        super(SettingsTab, self).__init__(parent, f)

        self.setupUi(self)

        self.recorder = Registry().get('recorder')
        self.settings = Settings()
        self.utils = Utils()

        self.saveSettings.clicked.connect(self.savesettings)
        self.browseRecordingDirectory.clicked.connect(self.loaddirectory)
        self.resetRecordingDirectory.clicked.connect(self.reset)
        self.resetRecordingFilename.clicked.connect(self.reset)
        self.recordingFilename.textEdited.connect(self.check_line_edit)

        self.check_line_edit(self.settings.value("RecordingFilename"))

        Registry().register('settings_tab', self)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            self.saveSettings.click()
        else:
            event.ignore()

    def savesettings(self):
        self.settings.setValue("MonitorCheckBox", self.monitorAudio.isChecked())
        self.settings.setValue("RecordingSampleRate", self.recordingSampleRate.currentText())
        self.settings.setValue("RecordingDirectory", self.recordingDirectory.text())
        self.settings.setValue("RecordingFilename", self.recordingFilename.text())

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

    def check_line_edit(self, char):
        if self.utils.clean_name(char, check=True):
            self.saveSettings.setEnabled(True)
            self.recordingFilename.setStyleSheet("")
        else:
            self.saveSettings.setEnabled(False)
            self.recordingFilename.setStyleSheet("QLineEdit { background: red }")

    def loadsettings(self):
        self.monitorAudio.setChecked(self.settings.value("MonitorCheckBox"))
        caps = self.recorder.audioconvert.get_static_pad('src').query_caps(None)
        string = caps.get_structure(1)
        for sample_rate in SettingsTab.__sample_rate__:
            if sample_rate <= string.get_value('rate'):
                self.recordingSampleRate.addItem(str(sample_rate))
        samplerateindex = self.recordingSampleRate.findText(self.settings.value("RecordingSampleRate"))
        self.recordingSampleRate.setCurrentIndex(samplerateindex)
        self.recordingDirectory.setText(self.settings.value("RecordingDirectory"))
        self.recordingFilename.setText(self.settings.value("RecordingFilename"))
