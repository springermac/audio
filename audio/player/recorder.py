#!/usr/bin/env python
# coding=utf-8

import os
import sys

import pygst
pygst.require('0.10')
import gst

from PyQt4 import QtCore


class Recorder(QtCore.QObject):
    updatemeter = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Recorder, self).__init__(parent)
        self.filepath = (os.path.join(os.path.dirname(__file__), 'output.wav'))
        self.playmode = False

        if sys.platform == 'darwin':
            self.pipeline = gst.Pipeline("Recording Pipeline")
            self.osxaudiosrc = gst.element_factory_make("osxaudiosrc", "audiosrc")
            self.audioconvert = gst.element_factory_make("audioconvert", "audioconvert")
            self.level = gst.element_factory_make("level", "level")
            self.wavenc = gst.element_factory_make("wavenc", "wavenc")
            self.filesink = gst.element_factory_make("filesink", "filesink")
            if not (self.pipeline and self.osxaudiosrc and self.audioconvert and self.level and self.wavenc and
                    self.filesink):
                print("Not all elements could be loaded", sys.stderr)
                exit(-1)

            self.pipeline.add(self.osxaudiosrc, self.audioconvert, self.level, self.wavenc, self.filesink)
            if not gst.element_link_many(self.osxaudiosrc, self.audioconvert, self.level, self.wavenc, self.filesink):
                print("Elements could not be linked", sys.stderr)
                exit(-1)
        else:
            self.pipeline = gst.Pipeline("Recording Pipeline")
            self.audiosrc = gst.element_factory_make("autoaudiosrc", "audiosrc")
            self.audioconvert = gst.element_factory_make("audioconvert", "audioconvert")
            self.level = gst.element_factory_make("level", "level")
            self.wavenc = gst.element_factory_make("wavenc", "wavenc")
            self.filesink = gst.element_factory_make("filesink", "filesink")
            if not (self.pipeline and self.audiosrc and self.audioconvert and self.level and self.wavenc and
                    self.filesink):
                print("Not all elements could be loaded", sys.stderr)

            self.pipeline.add(self.audiosrc, self.audioconvert, self.level, self.wavenc, self.filesink)
            if not gst.element_link_many(self.audiosrc, self.audioconvert, self.level, self.wavenc, self.filesink):
                print("Elements could not be linked", sys.stderr)
                exit(-1)

        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect('message', self.on_message)

    def record(self):
        self.pipeline.set_state(gst.STATE_PLAYING)
        self.playmode = True

    def pause(self):
        self.pipeline.set_state(gst.STATE_PAUSED)
        self.playmode = False

    def stop(self):
        self.pipeline.send_event(gst.event_new_eos())
        self.pipeline.set_state(gst.STATE_NULL)
        self.playmode = False

    def on_message(self, bus, message):
        """

        :param bus:
        :param message:
        """
        t = message.type
        if t == gst.MESSAGE_EOS:
            self.pipeline.set_state(gst.STATE_NULL)
            self.playmode = False
        elif t == gst.MESSAGE_ERROR:
            self.pipeline.set_state(gst.STATE_NULL)
            err, debug = message.parse_error()
            print("Error: %s" % err, debug)
            self.playmode = False
        elif message.src == self.level:
            self.updatemeter.emit(message)

    def load_file(self):
        self.filesink.set_property("location", self.filepath)
