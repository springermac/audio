#!/usr/bin/env python
# coding=utf-8

import sys

from PyQt5 import QtGui, QtCore, QtWidgets

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
    QProgressBar {{
        background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:0.1
        rgba(255, 0, 0, 255), stop:0.11 rgba(255, 255, 0, 255), stop:0.4 rgba(255, 255, 0, 255), stop:0.41
        rgba(0, 255, 0, 255), stop:1 rgba(0, 255, 0, 255));
        border: 0px;
    }}

    QProgressBar::chunk {{
        background: {0};
    }}
""".format('rgb(90%, 90%, 90%)' if sys.platform == 'darwin' else 'pallet(window)')

MIN_DB = -96
MAX_DB = 0


class AudioMeter(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(AudioMeter, self).__init__(parent)
        self.rms_percent = 0.0
        self.peak_percent = 0.0
        self.decay_percent = 0.0
        self.level_color_low = QtGui.QColor(QtCore.Qt.green)
        self.level_color_med = QtGui.QColor(QtCore.Qt.yellow)
        self.level_color_high = QtGui.QColor(QtCore.Qt.red)
        self.peak_color = QtGui.QColor(QtCore.Qt.yellow)

        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        self.setMinimumWidth(30)

    def reset(self):
        self.rms_percent = 0.0
        self.peak_percent = 0.0
        self.decay_percent = 0.0

        self.update()

    def level_changed(self, rms_level, peak_level, decay_level):
        self.rms_percent = self.iec_scale(rms_level)
        self.peak_percent = self.iec_scale(peak_level)
        self.decay_percent = self.iec_scale(decay_level)

        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.fillRect(self.rect(), QtGui.QPalette().color(QtGui.QPalette.Background))
        bar = self.rect()

        rms_peak = bar.bottom() - int(bar.height() * (self.rms_percent / 100))
        rms_low = bar.bottom() - int(bar.height() * (75.0 / 100))
        rms_med = bar.bottom() - int(bar.height() * (97.5 / 100))

        # bar.setTop(self.peak_hold_level)
        # bar.setBottom(bar.top() + 5)
        # painter.fillRect(bar, self.rms_color)
        # bar.setBottom(self.rect().bottom())

        # bar.setTop(self.peak_percent)
        # painter.fillRect(bar, self.peak_color)

        if self.rms_percent > 0:
            if self.rms_percent <= 75:
                bar.setTop(rms_peak)
                painter.fillRect(bar, self.level_color_low)
            elif 75 < self.rms_percent <= 97.5:
                bar.setTop(rms_low)
                painter.fillRect(bar, self.level_color_low)
                bar.setBottom(rms_low)
                bar.setTop(rms_peak)
                painter.fillRect(bar, self.level_color_med)
            else:
                bar.setTop(rms_low)
                painter.fillRect(bar, self.level_color_low)
                bar.setBottom(rms_low)
                bar.setTop(rms_med)
                painter.fillRect(bar, self.level_color_med)
                bar.setBottom(rms_med)
                bar.setTop(rms_peak)
                painter.fillRect(bar, self.level_color_high)

        painter.end()

    def iec_scale(self, db):
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


class RecordingTab(QtWidgets.QWidget, Ui_recordingTab):
    def __init__(self, parent=None):
        super(RecordingTab, self).__init__(parent)

        self.recorder = Recorder()
        self.settings = Settings()
        self.audio_meter = AudioMeter(self)

        self.setupUi(self)
        self.gridLayout.addWidget(self.audio_meter, 0, 1)

        self.recorder.updatemeter.connect(self.update)

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

    def update(self, message):
        """

        :param message:
        """
        if message.get_value('rms') and self.settings.value("MonitorCheckBox"):
            self.audio_meter.level_changed(message.get_value('rms')[0], message.get_value('peak')[0],
                                           message.get_value('decay')[0])
        else:
            self.audio_meter.reset()
