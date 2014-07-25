#!/usr/bin/env python
# coding=utf-8

from PyQt4 import QtCore, QtGui


class Settings(QtCore.QSettings):
    __default_settings__ = {
        'LastFile': None,
        'RecentFiles': None,
        'MainWindow/Geometry': QtCore.QByteArray(),
        'MainWindow/State': QtCore.QByteArray(),
        'MonitorCheckBox': True,
        'RecordingSampleRate': '44100',
        'RecordingDirectory': str(QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.MusicLocation)),
        'RecordingFilename': '%x.wav'
    }

    def __init__(self):
        super(Settings, self).__init__()

    def value(self, key):
        default_value = Settings.__default_settings__[key]
        setting = super(Settings, self).value(key, default_value, type(default_value))
        return setting

    def getDefault(self, key):
        return Settings.__default_settings__[key]
