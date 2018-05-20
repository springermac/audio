#!/usr/bin/env python
# coding=utf-8

import os
import re
import sys
import datetime

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib

Gst.init(None)

from PyQt5 import QtCore, QtWidgets, QtGui

from audio.core import Registry, Settings, Utils


class Recorder(QtCore.QThread):
    updatemeter = QtCore.pyqtSignal(object)
    __sample_rates__ = [
        8000,
        11025,
        22050,
        32000,
        44100,
        48000,
        96000
    ]

    def __init__(self):
        QtCore.QThread.__init__(self)
        self.loop = GLib.MainLoop.new(None, False)
        self.filepath = None
        self.pipelineactive = False
        self.recording = False
        self.paused = False
        self.recordrate = None

        self.settings = Settings()
        self.utils = Utils()
        self.pipeline = Gst.Pipeline()
        self.audiosrc = Gst.ElementFactory.make("autoaudiosrc", "audiosrc")
        self.captureratecap = Gst.Caps.new_any()

        self.captureratefilter = Gst.ElementFactory.make("capsfilter", "captureratefilter")
        self.captureratefilter.set_property("caps", self.captureratecap)

        self.audioconvert = Gst.ElementFactory.make("audioconvert", "audioconvert")

        self.audioresample = Gst.ElementFactory.make("audioresample", "audioresample")

        self.level = Gst.ElementFactory.make("level", "level")
        self.level.set_property("interval", 50000000)

        self.recordingratecap = Gst.Caps.new_any()
        self.recordingratefilter = Gst.ElementFactory.make("capsfilter", "recordingratefilter")
        self.recordingratefilter.set_property("caps", self.recordingratecap)

        self.levelvalve = Gst.ElementFactory.make("valve", "valve")

        self.audiosink = Gst.Bin()

        self.audiorate = Gst.ElementFactory.make("audiorate", "audiorate")
        self.audiorate.set_property("skip-to-first", True)
        self.wavenc = Gst.ElementFactory.make("wavenc", "wavenc")
        self.filesink = Gst.ElementFactory.make("filesink", "filesink")

        unavailable_elements = []
        for element in [self.audiosink, self.captureratefilter, self.audiorate, self.recordingratefilter, self.wavenc,
                        self.filesink]:
            if not element:
                unavailable_elements.append(element)
        if len(unavailable_elements) >= 1:
            print("Elements could not be loaded: {0}".format(unavailable_elements), sys.stderr)
            exit(-1)

        self.audiosink.add(self.audiorate)
        self.audiosink.add(self.recordingratefilter)
        self.audiosink.add(self.wavenc)
        self.audiorate.link(self.recordingratefilter)
        self.recordingratefilter.link(self.wavenc)

        self.audiosinkpad = self.audiorate.get_static_pad("sink")
        self.audiosinkghostpad = Gst.GhostPad.new("sink", self.audiosinkpad)
        self.audiosinkghostpad.set_active(True)
        self.audiosink.add_pad(self.audiosinkghostpad)

        if not (self.pipeline and self.audiosrc and self.audioconvert and self.audioresample
                and self.level and self.recordingratefilter and self.levelvalve):
            print("Not all elements could be loaded", sys.stderr)
            exit(-1)

        self.pipeline.add(self.audiosrc)
        self.pipeline.add(self.captureratefilter)
        self.pipeline.add(self.audioconvert)
        self.pipeline.add(self.audioresample)
        self.pipeline.add(self.level)
        self.pipeline.add(self.levelvalve)
        self.pipeline.add(self.audiosink)

        if not (self.audiosrc.link(self.audioconvert),
                self.audioconvert.link(self.audioresample), self.audioresample.link(self.level),
                self.level.link(self.levelvalve), self.levelvalve.link(self.audiosink)):
            print("Elements could not be linked", sys.stderr)
            exit(-1)

        self.levelvalve.set_property("drop", True)

        self.pipeline.set_state(Gst.State.PLAYING)
        self.pipelineactive = True
        self.recording = False

        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect('message', self.on_message)

        Registry().register('recorder', self)

    def run(self):
        self.loop.run()

    def record(self):
        if not self.recording:
            self.load()
            self.audiosink.add(self.filesink)
            self.wavenc.link(self.filesink)
            self.audiosink.set_state(Gst.State.PLAYING)
            self.levelvalve.set_property("drop", False)
            self.recording = True
        else:
            if self.paused:
                self.audiosink.set_state(Gst.State.PLAYING)
                self.levelvalve.set_property("drop", False)
                time = Gst.Segment()
                Gst.Segment.init(time, Gst.Format.TIME)
                time.start = self.levelvalve.clock.get_time()
                self.levelvalve.send_event(Gst.Event.new_segment(time))
                self.paused = False
            else:
                pass

    def pause(self):
        if not self.paused:
            self.levelvalve.set_property("drop", True)
            self.audiosink.set_state(Gst.State.PAUSED)
            self.paused = True
        else:
            pass

    def stop(self):
        if self.recording:
            self.audiosink.set_state(Gst.State.PLAYING)
            self.levelvalve.set_property("drop", True)
            self.audiosink.send_event(Gst.Event.new_eos())
            self.audiosink.set_state(Gst.State.NULL)
            self.wavenc.unlink(self.filesink)
            self.audiosink.remove(self.filesink)
            self.recording = False
            self.paused = False
        else:
            pass

    def on_message(self, bus, message):
        """

        :param bus:
        :param message:
        """
        t = message.type
        if t == Gst.MessageType.EOS:
            self.audiosink.set_state(Gst.State.NULL)
            self.pipelineactive = True
            self.recording = False
        elif t == Gst.MessageType.ERROR:
            self.pipeline.set_state(Gst.State.NULL)
            self.pipelineactive = False
            self.recording = False
        elif message.src == self.level:
            self.updatemeter.emit(message.get_structure())

    def load(self):
        now = datetime.datetime.now()
        date = re.sub(r'/', '-', now.strftime(self.settings.value("RecordingFilename")))

        if not self.recording:
            self.recordrate = self.settings.value("RecordingSampleRate")
            self.recordingratecap = Gst.caps_from_string("audio/x-raw, rate=" + self.recordrate)
            self.recordingratefilter.set_property("caps", self.recordingratecap)
            self.filepath = os.path.join(self.settings.value("RecordingDirectory"), self.utils.clean_name(date))
            self.filesink.set_property("location", self.filepath)
        else:
            pass

    def get_current_sample_rate(self):
        return self.audiosrc.get_static_pad('src').get_current_caps().get_structure(0).get_value('rate')

    def get_capable_sample_rates(self):
        caps = self.audiosrc.get_static_pad('src').get_allowed_caps()
        print(self.audiosrc.children)
        print(caps.to_string())
        current_rate = self.get_current_sample_rate()
        available_rates = set()
        for cap in caps:
            rate = cap.get_value('rate')
            if type(rate) == int:
                available_rates.add(rate)
        if len(available_rates) <= 1:
            available_rates.update(self.__sample_rates__)
        sample_rates = []
        for rate in available_rates:
            if rate <= current_rate:
                sample_rates.append(rate)
        sample_rates.sort()
        return sample_rates

    def stop_loop(self):
        self.pipeline.send_event(Gst.Event.new_eos())
        self.pipeline.set_state(Gst.State.NULL)
        self.loop.quit()
