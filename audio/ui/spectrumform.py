from PyQt5 import Qt, QtGui, QtWidgets

from audio.ui.spectrum import Ui_Spectrum


class SpectrumForm(QtWidgets.QWidget, Ui_Spectrum):
    def __init__(self, threshold):
        super(SpectrumForm, self).__init__()

        self.setupUi(self)
        self.bars_number = 1
        self.bars = list()
        self.threshold = threshold
        self.bar_color = list()
        self.black = QtGui.QColor(Qt.Qt.black)

        self.setMinimumSize(240, 320)

        self.show()

    def set_bands(self, bands):
        self.bars_number = bands

    def set_bars(self, values, bands):
        # print(values)
        self.bars_number = bands
        self.bars = values
        self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.draw_bars(painter)
        painter.end()

    def draw_bars(self, painter):
        size = self.size()
        width = size.width()
        height = size.height()

        bar_width = int(width / self.bars_number)

        painter.setPen(self.black)
        painter.setBrush(self.black)
        painter.drawRect(0, 0, width, height)
        gradient = QtGui.QLinearGradient(0, 0, width, height)
        gradient.setColorAt(0, Qt.Qt.blue)
        gradient.setColorAt(1, Qt.Qt.red)
        painter.setBrush(gradient)
        for bar, value in enumerate(self.bars):
            bar_height = ((value - self.threshold) * height) / (0 - self.threshold)
            # print(bar, value, pct, bar_height)
            painter.drawRect(
                bar * bar_width,
                height - bar_height,
                bar_width,
                bar_height)
