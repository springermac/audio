#!/usr/bin/env python
# coding=utf-8

import os
import re
import sys
import time
import datetime

import gobject

gobject.threads_init()
import pygst

pygst.require('0.10')
import gst

from PyQt4 import QtCore

from audio.core import Registry, Settings, Utils

if getattr(sys, 'frozen', False):
    basedir = sys._MEIPASS
else:
    basedir = os.path.dirname(__file__)


class Recorder(QtCore.QThread):
    updatemeter = QtCore.pyqtSignal(gst.Message)

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.loop = gobject.MainLoop()
        self.filepath = None
        self.pipelineactive = False
        self.recording = False
        self.srcrate = "44100"
        self.recordrate = None

        self.settings = Settings()
        self.utils = Utils()

        self.pipeline = gst.Pipeline("Recording Pipeline")

        if sys.platform == 'darwin':
            self.audiosrc = gst.element_factory_make("osxaudiosrc", "audiosrc")
            self.srcratecap = gst.Caps("audio/x-raw-float, rate=" + self.srcrate)

        elif os.name == 'nt':
            self.audiosrc = gst.element_factory_make("dshowaudiosrc", "audiosrc")
            self.srcratecap = gst.caps_new_any()

        else:
            self.audiosrc = gst.element_factory_make("autoaudiosrc", "audiosrc")
            self.srcratecap = gst.caps_new_any()

        self.srcratefilter = gst.element_factory_make("capsfilter", "srcratefilter")
        self.srcratefilter.set_property("caps", self.srcratecap)

        self.audioconvert = gst.element_factory_make("audioconvert", "audioconvert")

        self.audioresample = gst.element_factory_make("audioresample", "audioresample")

        self.level = gst.element_factory_make("level", "level")

        self.valve = gst.element_factory_make("valve", "valve")

        self.recordingratecap = gst.caps_new_any()
        self.recordingratefilter = gst.element_factory_make("capsfilter", "recordingratefilter")
        self.recordingratefilter.set_property("caps", self.recordingratecap)

        self.sink = gst.Bin("Sink")

        self.wavenc = gst.element_factory_make("wavenc", "wavenc")
        self.filesink = gst.element_factory_make("filesink", "filesink")

        self.sink.add_many(self.wavenc, self.filesink)

        gst.element_link_many(self.wavenc, self.filesink)

        self.sinkpad = self.wavenc.get_static_pad("sink")
        self.sinkghostpad = gst.GhostPad("sink", self.sinkpad)
        self.sinkghostpad.set_active(True)
        self.sink.add_pad(self.sinkghostpad)

        if not (self.pipeline and self.audiosrc and self.audioconvert and self.level and self.valve and
                self.srcratecap and self.srcratefilter):
            print("Not all elements could be loaded", sys.stderr)
            exit(-1)

        self.pipeline.add(self.audiosrc, self.srcratefilter, self.audioconvert, self.audioresample, self.level,
                          self.valve, self.sink)

        if not gst.element_link_many(self.audiosrc, self.srcratefilter, self.audioconvert, self.audioresample,
                                     self.level, self.valve, self.sink):
            print("Elements could not be linked", sys.stderr)
            exit(-1)

        self.valve.set_property("drop", True)

        self.load()

        self.pipeline.set_state(gst.STATE_PLAYING)

        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect('message', self.on_message)

        Registry().register('recorder', self)

    def run(self):
        self.loop.run()

    def record(self):
        self.sink.set_state(gst.STATE_PLAYING)
        self.valve.set_property("drop", False)
        self.pipelineactive = True
        self.recording = True

    def pause(self):
        self.valve.set_property("drop", True)
        self.sink.set_state(gst.STATE_PAUSED)
        self.recording = False

    def stop(self):
        self.valve.set_property("drop", True)
        self.sink.send_event(gst.event_new_eos())
        self.sink.set_state(gst.STATE_NULL)
        self.recording = False

    def on_message(self, bus, message):
        """

        :param bus:
        :param message:
        """
        t = message.type
        if t == gst.MESSAGE_EOS:
            print("EOS")
            self.pipeline.set_state(gst.STATE_NULL)
            self.pipelineactive = False
            self.recording = False
        elif t == gst.MESSAGE_ERROR:
            self.pipeline.set_state(gst.STATE_NULL)
            err, debug = message.parse_error()
            print("Error: %s" % err, debug)
            self.pipelineactive = False
            self.recording = False
        elif message.src == self.level:
            self.updatemeter.emit(message)

    def load(self):
        now = datetime.datetime.now()
        date = re.sub(r'/', '-', now.strftime(self.settings.value("RecordingFilename")))

        if not self.pipelineactive:
            self.recordrate = self.settings.value("RecordingSampleRate")
            self.recordingratecap = gst.Caps("audio/x-raw-int, rate=" + self.recordrate)
            self.recordingratefilter.set_property("caps", self.recordingratecap)
            self.filepath = os.path.join(self.settings.value("RecordingDirectory"), self.utils.clean_name(date))
            self.filesink.set_property("location", self.filepath)
        else:
            pass

    def stop_loop(self):
        self.pipeline.send_event(gst.event_new_eos())
        self.pipeline.set_state(gst.STATE_NULL)
        self.loop.quit()
