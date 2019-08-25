#!/usr/bin/env python
# coding=utf-8

from PyQt5 import QtCore, QtWidgets

from audio.ui.recordingtab import Ui_recordingTab
from audio.core import Registry, Settings

RECORDING_STYLE = """
    QPushButton {
        background-color: red;
    }
    QPushButton:pressed {
        background-color: red;
    }
"""


class RecordingTab(QtWidgets.QWidget, Ui_recordingTab):
    def __init__(self, parent=None):
        super(RecordingTab, self).__init__(parent)

        self.recorder = Registry().get('recorder')
        self.settings = Settings()

        self.setupUi(self)

        Registry().register('recording_tab', self)

    @QtCore.pyqtSlot()
    def on_recordButton_clicked(self):
        if not self.recordButton.isChecked():
            self.recordButton.setText("Resume\n Recording")
            self.recordButton.setStyleSheet(RECORDING_STYLE)
            self.recorder.pause()
        elif self.recordButton.isChecked():
            self.recordButton.setText("Pause")
            self.recordButton.setStyleSheet(RECORDING_STYLE)
            self.recorder.record()

    @QtCore.pyqtSlot()
    def on_stopButton_clicked(self):
        self.recordButton.setStyleSheet("")
        self.recordButton.setChecked(False)
        self.recordButton.setText("Record")
        self.recorder.stop()
