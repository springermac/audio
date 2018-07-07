import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib
from PyQt5 import QtCore

from audio.ui.spectrumform import SpectrumForm

BANDS = 700


class Spectrum(QtCore.QObject):
    message = QtCore.pyqtSignal(object)

    def __init__(self):
        super(Spectrum, self).__init__()
        self.sample_rate = 0
        self.threshold = -80

        self.bin = Gst.Bin('spectrumbin')

        self.audioqueue = Gst.ElementFactory.make("queue", "spectrumqueue")

        self.spectrum_element = Gst.ElementFactory.make("spectrum", "spectrum")

        self.spectrum_element.set_property('bands', BANDS)
        self.spectrum_element.set_property('interval', 50000000)
        self.spectrum_element.set_property('threshold', self.threshold)
        self.spectrum_element.set_property('post-messages', True)
        self.spectrum_element.set_property('message-magnitude', True)

        self.spectrumsink = Gst.ElementFactory.make("fakesink", "spectrumsink")

        self.bin.add(self.audioqueue)
        self.bin.add(self.spectrum_element)
        self.bin.add(self.spectrumsink)

        self.audioqueue.link(self.spectrum_element)
        self.spectrum_element.link(self.spectrumsink)

        self.scopesinkpad = self.audioqueue.get_static_pad("sink")
        self.scopesinkghostpad = Gst.GhostPad.new("sink", self.scopesinkpad)
        self.scopesinkghostpad.set_active(True)
        self.bin.add_pad(self.scopesinkghostpad)

        self.spectrum_widget = SpectrumForm(self.threshold)
        # self.spectrum_widget.set_bands(BANDS)

        self.message.connect(self.message_handler)

    def message_handler(self, message):
        bands = BANDS
        if self.sample_rate == 0:
            self.sample_rate = self.spectrum_element.get_static_pad('src').get_current_caps().get_structure(0).get_value('rate')
        half_sample = self.sample_rate / 2
        quarter_sample = self.sample_rate / 4
        struct = message.get_structure()
        magnitude = struct.get_value("magnitude")
        if magnitude:
            bars = list()
            for i, x in enumerate(magnitude):
                freq = (half_sample * i + quarter_sample) / BANDS
                if freq > 8000:
                    bands -= 1
                    pass
                bars.append(x)
                # print(x, pct)
            # print(bars)
            self.spectrum_widget.set_bars(bars, bands)
