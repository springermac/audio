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

        self.audioconvert = Gst.ElementFactory.make("audioconvert", "audioconvert")

        self.audioresample = Gst.ElementFactory.make("audioresample", "audioresample")

        self.level = Gst.ElementFactory.make("level", "level")
        self.level.set_property("interval", 50000000)

        self.recordingratecap = Gst.Caps.new_any()
        self.recordingratefilter = Gst.ElementFactory.make("capsfilter", "recordingratefilter")
        self.recordingratefilter.set_property("caps", self.recordingratecap)

        self.valve = Gst.ElementFactory.make("valve", "valve")

        self.sink = Gst.Bin()

        self.audiorate = Gst.ElementFactory.make("audiorate", "audiorate")
        self.audiorate.set_property("skip-to-first", True)
        self.wavenc = Gst.ElementFactory.make("wavenc", "wavenc")
        self.filesink = Gst.ElementFactory.make("filesink", "filesink")

        if not (self.sink and self.audiorate and self.wavenc and self.filesink):
            print("Not all elements could be loaded", sys.stderr)
            exit(-1)

        self.sink.add(self.audiorate)
        self.sink.add(self.wavenc)
        self.audiorate.link(self.wavenc)

        self.sinkpad = self.audiorate.get_static_pad("sink")
        self.sinkghostpad = Gst.GhostPad.new("sink", self.sinkpad)
        self.sinkghostpad.set_active(True)
        self.sink.add_pad(self.sinkghostpad)

        if not (self.pipeline and self.audiosrc and self.audioconvert and self.audioresample
                and self.level and self.recordingratefilter and self.valve):
            print("Not all elements could be loaded", sys.stderr)
            exit(-1)

        self.pipeline.add(self.audiosrc)
        self.pipeline.add(self.audioconvert)
        self.pipeline.add(self.audioresample)
        self.pipeline.add(self.level)
        self.pipeline.add(self.recordingratefilter)
        self.pipeline.add(self.valve)
        self.pipeline.add(self.sink)

        if not (self.audiosrc.link(self.audioconvert),
                self.audioconvert.link(self.audioresample), self.audioresample.link(self.level),
                self.level.link(self.recordingratefilter), self.recordingratefilter.link(self.valve),
                self.valve.link(self.sink)):
            print("Elements could not be linked", sys.stderr)
            exit(-1)

        self.valve.set_property("drop", True)

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
            self.sink.add(self.filesink)
            self.wavenc.link(self.filesink)
            self.sink.set_state(Gst.State.PLAYING)
            self.valve.set_property("drop", False)
            self.recording = True
        else:
            if self.paused:
                self.sink.set_state(Gst.State.PLAYING)
                self.valve.set_property("drop", False)
                time = Gst.Segment()
                Gst.Segment.init(time, Gst.Format.TIME)
                time.start = self.valve.clock.get_time()
                self.valve.send_event(Gst.Event.new_segment(time))
                self.paused = False
            else:
                pass

    def pause(self):
        if not self.paused:
            self.valve.set_property("drop", True)
            self.sink.set_state(Gst.State.PAUSED)
            self.paused = True
        else:
            pass

    def stop(self):
        if self.recording:
            self.sink.set_state(Gst.State.PLAYING)
            self.valve.set_property("drop", True)
            self.sink.send_event(Gst.Event.new_eos())
            self.sink.set_state(Gst.State.NULL)
            self.wavenc.unlink(self.filesink)
            self.sink.remove(self.filesink)
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
            self.sink.set_state(Gst.State.NULL)
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
