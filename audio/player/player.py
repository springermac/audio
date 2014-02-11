#!/usr/bin/env python
# coding=utf-8

import os
import sys

import pygst

pygst.require('0.10')
import gst

from PyQt4 import QtCore

class PlayerThread(QtCore.QThread):
    """

    :param player:
    """

    def __init__(self, player):
        super(PlayerThread, self).__init__(None)
        self.audio_player = player

    def run(self):
        self.audio_player.load_file()


class Player():
    def __init__(self):
        self.filepath = "/Users/jonathanspringer/projects/audio/output.wav"
        self.playmode = False

        if sys.platform == 'darwin':
            gst_command = ('osxaudiosrc ! audioconvert ! wavenc ! filesink location=%s') % self.filepath
            self.pipeline = gst.parse_launch(gst_command)

        bus = self.pipeline.get_bus()
        bus.add_signal_watch()
        bus.enable_sync_message_emission()
        bus.connect('message', self.on_message)

        self.audio_player = PlayerThread(self)
        self.audio_player.start()

    def play(self):
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
            self.sink.set_property("location", self.filepath)
