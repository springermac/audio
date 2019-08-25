#!/usr/bin/env python
# coding=utf-8
# Copyright (c) 2008 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 2 of the License, or
# version 3 of the License, or (at your option) any later version. It is
# provided for educational purposes and is distributed in the hope that
# it will be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See
# the GNU General Public License for more details.

from PyQt5 import QtCore, QtGui, QtWidgets


class HelpForm(QtWidgets.QDialog):
    def __init__(self, page, parent=None):
        """

        :param page:
        :param parent:
        """
        super(HelpForm, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setAttribute(QtCore.Qt.WA_GroupLeader)

        backaction = QtWidgets.QAction(QtGui.QIcon(":/back.png"), "&Back", self)
        backaction.setShortcut(QtGui.QKeySequence.Back)
        homeaction = QtWidgets.QAction(QtGui.QIcon(":/home.png"), "&Home", self)
        homeaction.setShortcut("Home")
        self.pagelabel = QtWidgets.QLabel()

        toolbar = QtWidgets.QToolBar()
        toolbar.addAction(backaction)
        toolbar.addAction(homeaction)
        toolbar.addWidget(self.pagelabel)
        self.textbrowser = QtWidgets.QTextBrowser()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.textbrowser, 1)
        self.setLayout(layout)

        backaction.triggered.connect(self.textbrowser.backward)
        homeaction.triggered.connect(self.textbrowser.home)
        self.textbrowser.sourceChanged.connect(self.updatepagetitle)

        self.textbrowser.setSearchPaths([":/help/helpfiles"])
        self.textbrowser.setSource(QtCore.QUrl(page))
        self.resize(400, 600)
        self.setWindowTitle("{0} Help".format(
            QtWidgets.QApplication.applicationName()))

    def updatepagetitle(self):
        self.pagelabel.setText(self.textbrowser.documentTitle())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    form = HelpForm("index.html")
    form.show()
    app.exec_()
