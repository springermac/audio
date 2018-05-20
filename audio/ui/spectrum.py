# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jonathanspringer/projects/audio/audio/resources/spectrum.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Spectrum(object):
    def setupUi(self, Spectrum):
        Spectrum.setObjectName("Spectrum")
        Spectrum.resize(400, 300)

        self.retranslateUi(Spectrum)
        QtCore.QMetaObject.connectSlotsByName(Spectrum)

    def retranslateUi(self, Spectrum):
        _translate = QtCore.QCoreApplication.translate
        Spectrum.setWindowTitle(_translate("Spectrum", "Spectrum"))

