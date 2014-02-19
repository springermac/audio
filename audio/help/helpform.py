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

from PyQt4 import QtCore, QtGui


class HelpForm(QtGui.QDialog):
    def __init__(self, page, parent=None):
        """

        :param page:
        :param parent:
        """
        super(HelpForm, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setAttribute(QtCore.Qt.WA_GroupLeader)

        backaction = QtGui.QAction(QtGui.QIcon(":/back.png"), "&Back", self)
        backaction.setShortcut(QtGui.QKeySequence.Back)
        homeaction = QtGui.QAction(QtGui.QIcon(":/home.png"), "&Home", self)
        homeaction.setShortcut("Home")
        self.pagelabel = QtGui.QLabel()

        toolbar = QtGui.QToolBar()
        toolbar.addAction(backaction)
        toolbar.addAction(homeaction)
        toolbar.addWidget(self.pagelabel)
        self.textbrowser = QtGui.QTextBrowser()

        layout = QtGui.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.textbrowser, 1)
        self.setLayout(layout)

        self.connect(backaction, QtCore.SIGNAL("triggered()"),
                     self.textbrowser, QtCore.SLOT("backward()"))
        self.connect(homeaction, QtCore.SIGNAL("triggered()"),
                     self.textbrowser, QtCore.SLOT("home()"))
        self.connect(self.textbrowser, QtCore.SIGNAL("sourceChanged(QUrl)"),
                     self.updatepagetitle)

        self.textbrowser.setSearchPaths([":/help/helpfiles"])
        self.textbrowser.setSource(QtCore.QUrl(page))
        self.resize(400, 600)
        self.setWindowTitle("{0} Help".format(
            QtGui.QApplication.applicationName()))

    def updatepagetitle(self):
        self.pagelabel.setText(self.textbrowser.documentTitle())


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    form = HelpForm("index.html")
    form.show()
    app.exec_()
