# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jonathanspringer/projects/audio/audio_program/audio/ui/burntab.ui'
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

class Ui_burnTab(object):
    def setupUi(self, burnTab):
        burnTab.setObjectName(_fromUtf8("burnTab"))
        burnTab.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(burnTab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.retranslateUi(burnTab)
        QtCore.QMetaObject.connectSlotsByName(burnTab)

    def retranslateUi(self, burnTab):
        burnTab.setWindowTitle(_translate("burnTab", "Form", None))


class burnTab(QtGui.QWidget, Ui_burnTab):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QWidget.__init__(self, parent, f)

        self.setupUi(self)

