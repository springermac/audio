#!/usr/bin/env python
# coding=utf-8

import os
import sys

import gst

from PyQt4 import QtCore

from .meter import Meter


class Recorder(object):
    def __init__(self):
        super(Recorder, self).__init__()
        self.filepath = "/Users/jonathanspringer/projects/audio/output.wav"
        self.playmode = False
        self.meter = Meter()

        if sys.platform == 'darwin':
            self.pipeline = gst.Pipeline("Recording Pipeline")
            self.osxaudiosrc = gst.element_factory_make("osxaudiosrc", "audiosrc")
            self.audioconvert = gst.element_factory_make("audioconvert", "audioconvert")
            self.level = gst.element_factory_make("level", "level")
            self.wavenc = gst.element_factory_make("wavenc", "wavenc")
            self.filesink = gst.element_factory_make("filesink", "filesink")
            self.pipeline.add(self.osxaudiosrc, self.audioconvert, self.level, self.wavenc, self.filesink)
            gst.element_link_many(self.osxaudiosrc, self.audioconvert, self.level, self.wavenc, self.filesink)

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
            print "Error: %s" % err, debug
            self.playmode = False
        elif message.src == self.level:
            self.meter.update(message)

    def load_file(self):
        if os.path.isfile(self.filepath):
            self.filesink.set_property("location", self.filepath)
