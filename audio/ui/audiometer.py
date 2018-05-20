# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jonathanspringer/projects/audio/audio/resources/audiometer.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AudioMeter(object):
    def setupUi(self, AudioMeter):
        AudioMeter.setObjectName("AudioMeter")
        AudioMeter.resize(400, 300)

        self.retranslateUi(AudioMeter)
        QtCore.QMetaObject.connectSlotsByName(AudioMeter)

    def retranslateUi(self, AudioMeter):
        _translate = QtCore.QCoreApplication.translate
        AudioMeter.setWindowTitle(_translate("AudioMeter", "Form"))

