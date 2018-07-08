#!/usr/bin/env python
# coding=utf-8

from PyQt5 import QtCore


class Settings(QtCore.QSettings):
    __default_settings__ = {
        'LastFile': None,
        'RecentFiles': None,
        'MainWindow/Geometry': QtCore.QByteArray(),
        'MainWindow/State': QtCore.QByteArray(),
        'MonitorCheckBox': True,
        'RecordingSampleRate': '44100',
        'RecordingDirectory': str(QtCore.QStandardPaths.standardLocations(QtCore.QStandardPaths.MusicLocation)),
        'RecordingFilename': '%x.wav'
    }

    def __init__(self):
        super(Settings, self).__init__()

    def value(self, key):
        default_value = Settings.__default_settings__[key]
        setting = super(Settings, self).value(key, default_value, type(default_value))
        return setting

    def get_default(self, key):
        return Settings.__default_settings__[key]
