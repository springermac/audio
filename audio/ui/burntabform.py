#!/usr/bin/env python
# coding=utf-8

from PyQt5 import QtWidgets

from audio.ui.burntab import Ui_burnTab
from audio.core.registry import Registry


class BurnTab(QtWidgets.QWidget, Ui_burnTab):
    def __init__(self, parent=None):
        super(BurnTab, self).__init__(parent)

        self.setupUi(self)

        Registry().register('burn_tab', self)
