#!/usr/bin/env python
# coding=utf-8

import os
import sys

import pygst

pygst.require('0.10')
import gst

from PyQt4 import QtCore

class RecorderThread(QtCore.QThread):
    def __init__(self, recorder):
        super(RecorderThread, self).__init__(None)
        self.audio_recorder = recorder

    def run(self):
        self.audio_recorder.load_file()


class Recorder():
    def __init__(self):
        self.filepath = "/Users/jonathanspringer/projects/audio/output.wav"
        self.playmode = False

        if sys.platform == 'darwin':
            self.pipeline = gst.Pipeline("Recording Pipeline")
            self.osxaudiosrc = gst.element_factory_make("osxaudiosrc", "audiosrc")
            self.audioconvert = gst.element_factory_make("audioconvert", "audioconvert")
            self.wavenc = gst.element_factory_make("wavenc", "wavenc")
            self.filesink = gst.element_factory_make("filesink", "filesink")
            self.pipeline.add(self.osxaudiosrc, self.audioconvert, self.wavenc, self.filesink)
            gst.element_link_many(self.osxaudiosrc, self.audioconvert, self.wavenc, self.filesink)

        bus = self.pipeline.get_bus()
        bus.add_signal_watch()
        bus.connect('message', self.on_message)

        self.audio_recorder = RecorderThread(self)
        self.audio_recorder.start()

    def record(self):
        self.pipeline.set_state(gst.STATE_PLAYING)
        self.playmode = True

    def pause(self):
        self.pipeline.set_state(gst.STATE_PAUSED)
        self.playmode = False

    def stop(self):
        self.pipeline.send_event(gst.event_new_eos())
        self.pipeline.set_state(gst.STATE_READY)
        self.playmode = False

    def on_message(self, bus, message):
        """

        :param bus:
        :param message:
        """
        print(1)
        t = message.type
        if t == gst.MESSAGE_EOS:
            self.pipeline.set_state(gst.STATE_NULL)
            self.playmode = False
        elif t == gst.MESSAGE_ERROR:
            self.pipeline.set_state(gst.STATE_NULL)
            err, debug = message.parse_error()
            print "Error: %s" % err, debug
            self.playmode = False

    def load_file(self):
        if os.path.isfile(self.filepath):
            self.filesink.set_property("location", self.filepath)
