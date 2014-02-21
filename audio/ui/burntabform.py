#!/usr/bin/env python
# coding=utf-8

from PyQt4 import QtGui, QtCore

from audio.ui.burntab import Ui_burnTab


class BurnTab(QtGui.QWidget, Ui_burnTab):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        super(BurnTab, self).__init__(parent, f)

        self.setupUi(self)