#!/usr/bin/env python
# coding=utf-8

import os
import sys

os.putenv("GST_DEBUG_DUMP_DOT_DIR", ".")

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib

Gst.init(None)

Gst.debug_set_default_threshold(4)
# Gst.debug_set_threshold_for_name('ringbuffer', 0)
# Gst.debug_set_threshold_for_name('wavenc', 7)
# Gst.debug_set_threshold_for_name('osxaudio', 7)
Gst.debug_set_active(True)

from PyQt5 import QtCore

from audio.core import Registry, Settings, Utils
from audio.player.level import Level
from audio.player.recorder import Recorder
from audio.player.spectrum import Spectrum


class Pipeline(QtCore.QThread):
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
        self.pipeline = Gst.Pipeline('audiopipeline')
        self.audiosrc = Gst.ElementFactory.make("autoaudiosrc", "audiosrc")
        self.captureratecap = Gst.Caps.new_any()

        self.captureratefilter = Gst.ElementFactory.make("capsfilter", "captureratefilter")
        self.captureratefilter.set_property("caps", self.captureratecap)

        self.audioconvert = Gst.ElementFactory.make("audioconvert", "audioconvert")

        self.audioresample = Gst.ElementFactory.make("audioresample", "audioresample")

        self.audiotee = Gst.ElementFactory.make("tee", "tee")

        self.spectrum = Spectrum()

        self.level = Level()

        self.recorder = Recorder()

        if not (self.pipeline and self.audiosrc and self.captureratefilter and self.audioconvert and self.audioresample
                and self.level and self.recorder):
            print("Not all elements could be loaded", sys.stderr)
            exit(-1)

        self.pipeline.add(self.audiosrc)
        self.pipeline.add(self.captureratefilter)
        self.pipeline.add(self.audioconvert)
        self.pipeline.add(self.audioresample)
        self.pipeline.add(self.audiotee)
        self.pipeline.add(self.spectrum.bin)
        self.pipeline.add(self.level.bin)
        self.pipeline.add(self.recorder.outer_bin)

        if not (self.audiosrc.link(self.captureratefilter), self.captureratefilter.link(self.audioconvert),
                self.audioconvert.link(self.audioresample), self.audioresample.link(self.audiotee),
                self.audiotee.link(self.spectrum.bin), self.audiotee.link(self.level.bin),
                self.audiotee.link(self.recorder.outer_bin)):
            print("Elements could not be linked", sys.stderr)
            exit(-1)

        self.pipeline.set_state(Gst.State.PLAYING)
        self.pipelineactive = True

        self.bus = self.pipeline.get_bus()
        self.bus.add_signal_watch()
        self.bus.connect('message', self.on_message)

        # Gst.debug_bin_to_dot_file(self.pipeline, Gst.DebugGraphDetails.ALL, "pipeline")

        Registry().register('pipeline', self)

    def run(self):
        self.loop.run()

    def on_message(self, bus, message):
        """

        :param bus:
        :param message:
        """
        t = message.type
        if t == Gst.MessageType.EOS:
            self.recorder.outer_bin.set_state(Gst.State.NULL)
            self.pipelineactive = True
            self.recording = False
        elif t == Gst.MessageType.ERROR:
            self.pipeline.set_state(Gst.State.NULL)
            self.pipelineactive = False
            self.recording = False
        elif message.src == self.level.level:
            self.level.update(message.get_structure())
        elif message.src == self.spectrum.spectrum_element:
            self.spectrum.message.emit(message)

    def get_current_sample_rate(self):
        return self.audiosrc.get_static_pad('src').get_current_caps().get_structure(0).get_value('rate')

    def get_capable_sample_rates(self):
        monitor = Gst.DeviceMonitor()
        monitor.add_filter('Audio/Source')
        devices = monitor.get_devices()
        for device in devices:
            print(device.get_name())
            print(device.get_display_name())
            print(device.get_caps())
            # print(device.props.device_id)
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
        self.spectrum.spectrum_widget.close()
