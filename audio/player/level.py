import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib

from PyQt5 import QtCore

from audio.core import Settings, Registry


class Level(QtCore.QObject):
    updatemeter = QtCore.pyqtSignal(object, object, object)
    reset = QtCore.pyqtSignal()

    def __init__(self):
        super(Level, self).__init__()
        self.settings = Settings()

        self.bin = Gst.Bin('levelbin')

        self.levelqueue = Gst.ElementFactory.make("queue", "levelqueue")

        self.level = Gst.ElementFactory.make("level", "level")
        self.level.set_property("interval", 50000000)

        self.levelsink = Gst.ElementFactory.make("fakesink", "levelsink")

        self.bin.add(self.levelqueue)
        self.bin.add(self.level)
        self.bin.add(self.levelsink)

        self.levelqueue.link(self.level)
        self.level.link(self.levelsink)

        self.scopesinkpad = self.levelqueue.get_static_pad("sink")
        self.scopesinkghostpad = Gst.GhostPad.new("sink", self.scopesinkpad)
        self.scopesinkghostpad.set_active(True)
        self.bin.add_pad(self.scopesinkghostpad)

        Registry().register('level', self)

    def update(self, message):
        """

        :param message:
        """
        if message.get_value('rms') and self.settings.value("MonitorCheckBox"):
            self.updatemeter.emit(message.get_value('rms')[0], message.get_value('peak')[0],
                                  message.get_value('decay')[0])
        else:
            self.reset.emit()
