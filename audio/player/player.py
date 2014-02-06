#!/usr/bin/env python
# coding=utf-8

import os

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
        self.audio_player.pause()


class Player():
    def __init__(self):
        self.filepath = "/Users/jonathanspringer/Music/3-1.wav"

        self.player = gst.element_factory_make("playbin2", None)
        self.player.set_property("volume", 1)
        bus = self.player.get_bus()
        bus.add_signal_watch()
        bus.enable_sync_message_emission()
        bus.connect('message', self.on_message)
        self.audio_player = PlayerThread(self)
        self.audio_player.start()

    def play(self):
        if os.path.isfile(self.filepath):
            self.playmode = True
            self.player.set_property("uri", "file://" + self.filepath)
            self.player.set_state(gst.STATE_PLAYING)

    def pause(self):
        self.player.set_state(gst.STATE_PAUSED)

    def stop(self):
        self.player.set_state(gst.STATE_NULL)

    def on_message(self, bus, message):
        """

        :param bus:
        :param message:
        """
        print(1)
        t = message.type
        if t == gst.MESSAGE_EOS:
            self.player.set_state(gst.STATE_NULL)
            self.playmode = False
        elif t == gst.MESSAGE_ERROR:
            self.player.set_state(gst.STATE_NULL)
            err, debug = message.parse_error()
            print "Error: %s" % err, debug
            self.playmode = False
