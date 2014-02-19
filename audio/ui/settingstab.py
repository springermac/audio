# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jonathanspringer/projects/audio/audio_program/audio/ui/settingstab.ui'
#
# Created: Wed Feb 19 12:58:31 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_settingsTab(object):
    def setupUi(self, settingsTab):
        settingsTab.setObjectName(_fromUtf8("settingsTab"))
        settingsTab.resize(128, 54)
        self.gridLayout = QtGui.QGridLayout(settingsTab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.monitorAudio = QtGui.QCheckBox(settingsTab)
        self.monitorAudio.setObjectName(_fromUtf8("monitorAudio"))
        self.gridLayout.addWidget(self.monitorAudio, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)

        self.retranslateUi(settingsTab)
        QtCore.QMetaObject.connectSlotsByName(settingsTab)

    def retranslateUi(self, settingsTab):
        settingsTab.setWindowTitle(_translate("settingsTab", "Form", None))
        self.monitorAudio.setText(_translate("settingsTab", "Monitor Audio", None))


class settingsTab(QtGui.QWidget, Ui_settingsTab):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QWidget.__init__(self, parent, f)

        self.setupUi(self)

