import math

import numpy as np
from PyQt5 import Qt, QtGui, QtWidgets, QtChart, QtCore

from audio.ui.spectrum import Ui_Spectrum


def series_to_polyline(xdata, ydata):
    """Convert series data to QPolygon(F) polyline

    This code is derived from PythonQwt's function named
    `qwt.plot_curve.series_to_polyline`"""
    size = len(xdata)
    polyline = QtGui.QPolygonF(size)
    pointer = polyline.data()
    dtype, tinfo = np.float, np.finfo
    pointer.setsize(2 * polyline.size() * tinfo(dtype).dtype.itemsize)
    memory = np.frombuffer(pointer, dtype)
    memory[:(size - 1) * 2 + 1:2] = xdata
    memory[1:(size - 1) * 2 + 2:2] = ydata
    return polyline


class SpectrumForm(QtChart.QChartView, Ui_Spectrum):
    def __init__(self, threshold):
        super(SpectrumForm, self).__init__()

        self.setupUi(self)
        self.chart = QtChart.QChart()
        self.chart.legend().hide()
        self.setChart(self.chart)
        self.bars_number = 1
        self.bars = list()
        self.threshold = threshold
        self.bar_color = list()
        self.black = QtGui.QColor(Qt.Qt.black)
        self.curve = QtChart.QLineSeries()
        self.add_data(self.curve, color=Qt.Qt.red)

        self.setMinimumSize(240, 320)

        self.show()

    def add_data(self, curve, color=None):
        pen = curve.pen()
        if color is not None:
            pen.setColor(color)
        pen.setWidthF(.1)
        curve.setPen(pen)
        curve.setUseOpenGL(True)
        curve.append(series_to_polyline(np.linspace(0, 30000), np.linspace(self.threshold, 0)))
        xaxis = QtChart.QLogValueAxis()
        xaxis.setMinorTickCount(10)
        xaxis.setRange(0, 30000)
        yaxis = QtChart.QValueAxis()
        yaxis.setRange(self.threshold, 0)
        self.chart.addSeries(curve)
        self.chart.addAxis(xaxis, Qt.Qt.AlignBottom)
        self.chart.setAxisY(yaxis)
        curve.attachAxis(xaxis)

    def set_bands(self, bands):
        self.bars_number = bands

    def set_bars(self, values, freqs):
        self.bars_number = freqs
        self.bars = values
        self.curve.replace(series_to_polyline(self.bars_number, self.bars))
