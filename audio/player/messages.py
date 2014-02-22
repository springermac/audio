#!/usr/bin/env python
# coding=utf-8

import time

import gst

from PyQt4 import QtCore

from audio.player.recorder import Recorder


class Message(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)
        self.recorder = Recorder()
        self.bus = self.recorder.bus

    def run(self):
        while True:
            self.bus.poll(gst.MESSAGE_ANY, 1)
            time.sleep(0.01)
