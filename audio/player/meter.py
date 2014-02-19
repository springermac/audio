#!/usr/bin/env python
# coding=utf-8

import math

from PyQt4 import QtCore

METER_STYLE = """
    QProgressBar {
        border: 0px;
        background-color: rgb(97%, 97%, 97%);
        background-image: url(:/images/meter.png);
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


class Meter(QtCore.QObject):
    def __init__(self):
        super(Meter, self).__init__()
        self.settings = QtCore.QSettings()

    def update(self, message):
        """

        :param message:
        """
        if message and self.settings.value("MonitorCheckBox").toBool():
            #get the structure of the message
            struc = message.structure
            #if the structure message is rms
            if struc.has_field("rms"):
                print("meter")
                rms = struc["rms"]
                #get the values of rms in a list
                rms0 = abs(float(rms[0]))
                #compute for rms to decibels
                rmsdb = 10 * math.log(rms0 / 32768)
                #compute for progress bar
                vlrms = (rmsdb-MIN_DB) * 100 / (MAX_DB-MIN_DB)
                #emit the signal to the qt progress bar
                vlrms_inverted = ((abs(vlrms) / 100.0) * -100.0) + 100.0
                self.emit(QtCore.SIGNAL("setmeterlevel"), vlrms_inverted)
