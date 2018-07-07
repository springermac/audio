#!/usr/bin/env python
# coding=utf-8

import os
import re
import sys
import datetime

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib

from PyQt5 import QtCore

from audio.core import Registry, Settings, Utils


class Recorder(QtCore.QObject):
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
        super(Recorder, self).__init__()
        self.filepath = None
        self.recording = False
        self.paused = False
        self.recordrate = None

        self.settings = Settings()
        self.utils = Utils()

        self.outer_bin = Gst.Bin('recorder_outer')

        self.recordingqueue = Gst.ElementFactory.make("queue", "recordingqueue")

        self.recordingvalve = Gst.ElementFactory.make("valve", "recordingvalve")

        self.inner_bin = Gst.Bin('recorder_inner')

        self.audiorate = Gst.ElementFactory.make("audiorate", "audiorate")
        self.audiorate.set_property("skip-to-first", True)

        self.recordingratecap = Gst.Caps.new_any()
        self.recordingratefilter = Gst.ElementFactory.make("capsfilter", "recordingratefilter")
        self.recordingratefilter.set_property("caps", self.recordingratecap)

        self.wavenc = Gst.ElementFactory.make("wavenc", "wavenc")
        self.filesink = Gst.ElementFactory.make("filesink", "filesink")

        unavailable_elements = []
        for element in [self.outer_bin, self.recordingvalve, self.audiorate, self.recordingratefilter,
                        self.wavenc, self.filesink]:
            if not element:
                unavailable_elements.append(element)
        if len(unavailable_elements) >= 1:
            print("Elements could not be loaded: {0}".format(unavailable_elements), sys.stderr)
            exit(-1)

        self.outer_bin.add(self.recordingqueue)
        self.outer_bin.add(self.recordingvalve)
        self.outer_bin.add(self.inner_bin)
        self.inner_bin.add(self.audiorate)
        self.inner_bin.add(self.recordingratefilter)
        self.inner_bin.add(self.wavenc)

        self.audiosinkpad_outer = self.recordingqueue.get_static_pad("sink")
        self.audiosinkghostpad_outer = Gst.GhostPad.new("sink", self.audiosinkpad_outer)
        self.audiosinkghostpad_outer.set_active(True)
        self.outer_bin.add_pad(self.audiosinkghostpad_outer)

        self.audiosinkpad_inner = self.audiorate.get_static_pad("sink")
        self.audiosinkghostpad_inner = Gst.GhostPad.new("sink", self.audiosinkpad_inner)
        self.audiosinkghostpad_inner.set_active(True)
        self.inner_bin.add_pad(self.audiosinkghostpad_inner)

        self.recordingqueue.link(self.recordingvalve)
        self.recordingvalve.link(self.inner_bin)
        self.audiorate.link(self.recordingratefilter)
        self.recordingratefilter.link(self.wavenc)

        self.recordingvalve.set_property("drop", True)

        Registry().register('recorder', self)

    def record(self):
        if not self.recording:
            self.load()
            self.inner_bin.add(self.filesink)
            self.wavenc.link(self.filesink)
            self.outer_bin.set_state(Gst.State.PLAYING)
            self.recordingvalve.set_property("drop", False)
            self.recording = True
            # Gst.debug_bin_to_dot_file(self.outer_bin, Gst.DebugGraphDetails.ALL, "pipeline_record")
        else:
            if self.paused:
                self.outer_bin.set_state(Gst.State.PLAYING)
                self.recordingvalve.set_property("drop", False)
                time = Gst.Segment()
                Gst.Segment.init(time, Gst.Format.TIME)
                time.start = self.recordingvalve.clock.get_time()
                self.recordingvalve.send_event(Gst.Event.new_segment(time))
                self.paused = False
            else:
                pass

    def pause(self):
        if not self.paused:
            self.recordingvalve.set_property("drop", True)
            self.outer_bin.set_state(Gst.State.PAUSED)
            self.paused = True
        else:
            pass

    def stop(self):
        if self.recording:
            self.outer_bin.set_state(Gst.State.PLAYING)
            self.recordingvalve.set_property("drop", True)
            self.inner_bin.send_event(Gst.Event.new_eos())
            self.inner_bin.set_state(Gst.State.NULL)
            self.wavenc.unlink(self.filesink)
            self.inner_bin.remove(self.filesink)
            self.recording = False
            self.paused = False
        else:
            pass

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
