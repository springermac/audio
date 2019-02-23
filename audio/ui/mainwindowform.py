#!/usr/bin/env python
# coding=utf-8

import platform

from PyQt5 import QtGui, QtCore, QtWidgets

from audio.ui.mainwindow import Ui_MainWindow
from audio.help.helpform import HelpForm
from audio.core import Registry, Settings
from audio.player.pipeline import Pipeline

__version__ = "1.0.0"


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.dirty = False
        self.filename = None
        self.image = None

        # self.pipeline = Pipeline()

        self.setupUi(self)
        self.statusbar.showMessage("Ready", 5000)
        self.action_About.triggered.connect(self.helpabout)
        self.action_Save.setShortcut(QtGui.QKeySequence.Save)
        self.actionSave_As.setShortcut(QtGui.QKeySequence.SaveAs)
        self.action_Quit.triggered.connect(self.close)
        self.action_Quit.setShortcut(QtGui.QKeySequence.Quit)
        self.action_Help.triggered.connect(self.helphelp)
        self.action_Help.setShortcut(QtGui.QKeySequence.HelpContents)

        Registry().register('main_window', self)

        self.settingstab = Registry().get('settings_tab')

        self.loadsettings()
        # self.pipeline.start()

    def closeEvent(self, event):
        """

        :param event:
        """
        if self.oktocontinue():
            # self.pipeline.stop_loop()
            self.savesettings()
        else:
            event.ignore()

    def oktocontinue(self):
        """


        :return:
        """
        if self.dirty:
            reply = QtWidgets.QMessageBox.question(self, "Image Changer - Unsaved Changes", "Save unsaved changes?",
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No |
                                                   QtWidgets.QMessageBox.Cancel)
            if reply == QtWidgets.QMessageBox.Cancel:
                return False
            elif reply == QtWidgets.QMessageBox.Yes:
                return self.filesave()
        return True

    def savesettings(self):
        settings = Settings()

        filename = self.filename
        settings.setValue("LastFile", filename)
        settings.setValue("MainWindow/Geometry", self.saveGeometry())
        settings.setValue("MainWindow/State", self.saveState())

        self.settingstab.savesettings()

    def loadsettings(self):
        settings = Settings()

        self.restoreGeometry(settings.value("MainWindow/Geometry"))
        self.restoreState(settings.value("MainWindow/State"))

        self.settingstab.loadsettings()

    def helpabout(self):
        QtWidgets.QMessageBox.about(self, "About Image Changer",
                                    """<b>Image Changer</b> v {0}
                                    <p>Copyright &copy; 2008 Qtrac Ltd.
                                    All rights reserved.
                                    <p>This application can be used to perform
                                    simple image manipulations.
                                    <p>Python {1} - Qt {2} - PyQt {3} on {4}""".format(__version__,
                                                                                       platform.python_version(),
                                                                                       QtCore.QT_VERSION_STR,
                                                                                       QtCore.PYQT_VERSION_STR,
                                                                                       platform.system()))

    def helphelp(self):
        form = HelpForm("index.html", self)
        form.show()
