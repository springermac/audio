#!/usr/bin/env python
# coding=utf-8

from PyQt4 import QtCore, QtGui


class Settings(QtCore.QSettings):
    __default_settings__ = {
        'LastFile': None,
        'RecentFiles': None,
        'MainWindow/Geometry': None,
        'MainWindow/State': None,
        'MonitorCheckBox': True,
        'RecordingSampleRate': '44100',
        'RecordingDirectory': str(QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.MusicLocation)),
        'RecordingFilename': '%x.wav'
    }

    def __init__(self):
        super(Settings, self).__init__()

    def value(self, key):
        default_value = Settings.__default_settings__[key]
        setting = super(Settings, self).value(key, default_value)
        return self._convert_value(setting, default_value)

    def _convert_value(self, setting, default_value):
        if isinstance(default_value, bool):
            return setting.toBool()
        if isinstance(default_value, int):
            return int(setting.toInt()[0])
        if isinstance(default_value, str):
            return str(setting.toString())
        return setting

    def getDefault(self, key):
        return Settings.__default_settings__[key]