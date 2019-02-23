from PyQt5 import QtWidgets, QtGui, QtCore

from audio.core import Registry
from audio.ui.audiometer import Ui_AudioMeter


class AudioMeterForm(QtWidgets.QWidget, Ui_AudioMeter):
    def __init__(self, parent=None):
        super(AudioMeterForm, self).__init__(parent)
        self.setupUi(self)

        self.level = Registry().get('level')

        self.range = -50
        self.rms_percent = 0.0
        self.peak_percent = 0.0
        self.decay_percent = 0.0
        self.level_color_low = QtGui.QColor(QtCore.Qt.green)
        self.level_color_med = QtGui.QColor(QtCore.Qt.yellow)
        self.level_color_high = QtGui.QColor(QtCore.Qt.red)
        self.peak_color = QtGui.QColor(QtCore.Qt.black)

        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        self.setMinimumWidth(30)

        # self.level.updatemeter.connect(self.level_changed)
        # self.level.reset.connect(self.reset)

    def reset(self):
        self.rms_percent = 0.0
        self.peak_percent = 0.0
        self.decay_percent = 0.0

        self.update()

    def level_changed(self, rms_level, peak_level, decay_level):
        self.rms_percent = self.iec_scale(rms_level, self.range)
        self.peak_percent = self.iec_scale(peak_level, self.range)
        self.decay_percent = self.iec_scale(decay_level, self.range)

        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.fillRect(self.rect(), QtGui.QPalette().color(QtGui.QPalette.Background))
        peak_bar = self.rect()
        decay_bar = self.rect()

        decay = decay_bar.bottom() - int(decay_bar.height() * (self.decay_percent / 100))
        rms_high = peak_bar.bottom() - int(peak_bar.height() * (self.rms_percent / 100))
        rms_low = peak_bar.bottom() - int(peak_bar.height() * (75.0 / 100))
        rms_med = peak_bar.bottom() - int(peak_bar.height() * (97.5 / 100))

        # bar.setTop(self.peak_hold_level)
        # bar.setBottom(bar.top() + 5)
        # painter.fillRect(bar, self.rms_color)
        # bar.setBottom(self.rect().bottom())

        if self.rms_percent > 0:
            if self.rms_percent <= 75:
                peak_bar.setTop(rms_high)
                painter.fillRect(peak_bar, self.level_color_low)
            elif 75.0 < self.rms_percent <= 97.5:
                peak_bar.setTop(rms_low)
                painter.fillRect(peak_bar, self.level_color_low)
                peak_bar.setBottom(rms_low)
                peak_bar.setTop(rms_high)
                painter.fillRect(peak_bar, self.level_color_med)
            else:
                peak_bar.setTop(rms_low)
                painter.fillRect(peak_bar, self.level_color_low)
                peak_bar.setBottom(rms_low)
                peak_bar.setTop(rms_med)
                painter.fillRect(peak_bar, self.level_color_med)
                peak_bar.setBottom(rms_med)
                peak_bar.setTop(rms_high)
                painter.fillRect(peak_bar, self.level_color_high)

        decay_bar.setTop(decay + 2.5)
        decay_bar.setBottom(decay - 2.5)
        painter.fillRect(decay_bar, self.peak_color)

        painter.end()

    @staticmethod
    def iec_scale(db, range):
        old_range = (0 - range)
        new_range = (100 - 0)
        if db < 0.0:
            pct = ((db - range) * new_range) / old_range + 0
        else:
            pct = 100
        # scale = {'-70': [70.0, 60.0, 50.0, 40.0, 30.0, 20.0, 0.0],
        #          '-60': []}
        # if db < -scale[range][0]:
        #     pct = 0.0
        # elif db < -scale[range][1]:
        #     pct = (db + scale[range][0]) * 0.25
        # elif db < -scale[range][2]:
        #     pct = (db + scale[range][1]) * 0.5 + 2.5
        # elif db < -scale[range][3]:
        #     pct = (db + scale[range][2]) * 0.75 + 7.5
        # elif db < -scale[range][4]:
        #     pct = (db + scale[range][3]) * 1.5 + 15.0
        # elif db < -scale[range][5]:
        #     pct = (db + scale[range][4]) * 2.0 + 30.0
        # elif db < -scale[range][6]:
        #     pct = (db + scale[range][5]) * 2.5 + 50.0
        # else:
        #     pct = 100.0

        return pct
