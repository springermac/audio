#!/usr/bin/env python
# coding=utf-8

import platform

from PyQt4 import QtGui, QtCore

from audio.ui.mainwindow import Ui_MainWindow
from audio.help.helpform import HelpForm
from audio.core.registry import Registry

__version__ = "1.0.0"


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        super(MainWindow, self).__init__(parent, f)
        self.dirty = False
        self.filename = None
        self.image = None

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

        self.recorder = Registry().get('recorder')

        self.loadsettings()
        self.recorder.start()

    def closeEvent(self, event):
        """

        :param event:
        """
        if self.oktocontinue():
            self.recorder.stop_loop()
            self.savesettings()
        else:
            event.ignore()

    def oktocontinue(self):
        """


        :return:
        """
        if self.dirty:
            reply = QtGui.QMessageBox.question(self, "Image Changer - Unsaved Changes", "Save unsaved changes?",
                                               QtGui.QMessageBox.Yes | QtGui.QMessageBox.No | QtGui.QMessageBox.Cancel)
            if reply == QtGui.QMessageBox.Cancel:
                return False
            elif reply == QtGui.QMessageBox.Yes:
                return self.filesave()
        return True

    def savesettings(self):
        settings = QtCore.QSettings()
        filename = (QtCore.QVariant(QtCore.QString(self.filename))
                    if self.filename is not None else QtCore.QVariant())
        settings.setValue("LastFile", filename)
        recentfiles = (QtCore.QVariant(self.recentfiles)
                       if self.recentfiles else QtCore.QVariant())
        settings.setValue("RecentFiles", recentfiles)
        settings.setValue("MainWindow/Geometry", QtCore.QVariant(
            self.saveGeometry()))
        settings.setValue("MainWindow/State", QtCore.QVariant(
            self.saveState()))

    def loadsettings(self):
        settings = QtCore.QSettings()
        self.recentfiles = settings.value("RecentFiles").toStringList()
        self.restoreGeometry(settings.value("MainWindow/Geometry").toByteArray())
        self.restoreState(settings.value("MainWindow/State").toByteArray())
        self.settingsTab.monitorAudio.setChecked(settings.value("MonitorCheckBox", True).toBool())
        samplerateindex = self.settingsTab.recordingSampleRate.findText(
            settings.value("RecordingSampleRate", 44100).toString())
        self.settingsTab.recordingSampleRate.setCurrentIndex(samplerateindex)
        self.settingsTab.outputLocation.setText(
            settings.value("RecordingDirectory", QtGui.QDesktopServices.storageLocation(
                QtGui.QDesktopServices.MusicLocation)).toString())
        self.settingsTab.outputFileName.setText(settings.value("RecordingFilename", "output.wav").toString())

    def helpabout(self):
        QtGui.QMessageBox.about(self, "About Image Changer",
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
