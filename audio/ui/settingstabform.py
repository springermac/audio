#!/usr/bin/env python
# coding=utf-8

import os

from PyQt5 import QtCore, QtWidgets

from audio.ui.settingstab import Ui_settingsTab
from audio.core import Registry, Settings, Utils


class SettingsTab(QtWidgets.QWidget, Ui_settingsTab):
    def __init__(self, parent=None):
        super(SettingsTab, self).__init__(parent)

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
        newrecordingdirectory = str(QtWidgets.QFileDialog.getExistingDirectory(self, 'Set Directory',
                                                                               oldrecordingdirector,
                                                                               QtWidgets.QFileDialog.ShowDirsOnly))
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
            default_setting = settings.get_default('RecordingDirectory')
            self.recordingDirectory.setText(default_setting)
        elif button == 'resetRecordingFilename':
            default_setting = settings.get_default('RecordingFilename')
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
        sample_rates = self.recorder.get_capable_sample_rates()
        for sample_rate in sample_rates:
            self.recordingSampleRate.addItem(str(sample_rate))
        samplerateindex = self.recordingSampleRate.findText(self.settings.value("RecordingSampleRate"))
        self.recordingSampleRate.setCurrentIndex(samplerateindex)
        self.recordingDirectory.setText(self.settings.value("RecordingDirectory"))
        self.recordingFilename.setText(self.settings.value("RecordingFilename"))
