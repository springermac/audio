#!/usr/bin/env python
# coding=utf-8

import math

from PyQt4 import QtGui, QtCore

from audio.ui.recordingtab import Ui_recordingTab
from audio.core import Registry, Settings
from audio.player.recorder import Recorder

RECORDING_STYLE = """
    QPushButton {
        background-color: red;
    }
    QPushButton:pressed {
        background-color: red;
    }
"""

METER_STYLE = """
    QProgressBar {
        border: 0px;
        background-color: rgb(97%, 97%, 97%);
        background-image: url(:/meter.png);
        background-repeat: repeat-x;
    }

    QProgressBar::chunk {
         background: rgb(90%, 90%, 90%);
         height: 10px;
         margin-bottom: 1px;
    }
"""

MIN_DB = -45
MAX_DB = 0


class RecordingTab(QtGui.QWidget, Ui_recordingTab):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        super(RecordingTab, self).__init__(parent, f)

        self.recorder = Recorder()
        self.settings = Settings()

        self.setupUi(self)
        self.audioMeter.setStyleSheet(METER_STYLE)

        self.pushButton.clicked.connect(self.on_button_clicked)
        self.pushButton_2.clicked.connect(self.on_button_2_clicked)

        self.recorder.updatemeter.connect(self.update)

        Registry().register('recording_tab', self)

    def on_button_clicked(self):
        if not self.pushButton.isChecked():
            self.pushButton.setText("Resume\n Recording")
            self.pushButton.setStyleSheet(RECORDING_STYLE)
            self.recorder.pause()
        elif self.pushButton.isChecked():
            self.pushButton.setText("Pause")
            self.pushButton.setStyleSheet(RECORDING_STYLE)
            self.recorder.record()

    def on_button_2_clicked(self):
        self.pushButton.setStyleSheet("")
        self.pushButton.setChecked(False)
        self.pushButton.setText("Record")
        self.recorder.stop()

    def update(self, rms):
        """

        :param rms:
        """
        if rms and self.settings.value("MonitorCheckBox"):
            #get the values of rms in a list
            rms0 = abs(float(rms[0]))
            #compute for rms to decibels
            rmsdb = 10 * math.log(rms0 / 32768)
            #compute for progress bar
            vlrms = (rmsdb - MIN_DB) * 100 / (MAX_DB - MIN_DB)
            #emit the signal to the qt progress bar
            vlrms_inverted = ((abs(vlrms) / 100.0) * -100.0) + 100.0
            self.audioMeter.setValue(int(vlrms_inverted))
        else:
            self.audioMeter.setValue(100)

    def iec_scale(self, db):
        pct = 0.0

        if db < -70.0:
            pct = 0.0
        elif db < -60.0:
            pct = (db + 70.0) * 0.25
        elif db < -50.0:
            pct = (db + 60.0) * 0.5 + 2.5
        elif db < -40.0:
            pct = (db + 50.0) * 0.75 + 7.5
        elif db < -30.0:
            pct = (db + 40.0) * 1.5 + 15.0
        elif db < -20.0:
            pct = (db + 30.0) * 2.0 + 30.0
        elif db < 0.0:
            pct = (db + 20.0) * 2.5 + 50.0
        else:
            pct = 100.0

        return pct
