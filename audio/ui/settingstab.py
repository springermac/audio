# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jonathanspringer/projects/audio/audio_program/audio/resources/settingstab.ui'
#
#
#
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

class Ui_settingsTab(object):
    def setupUi(self, settingsTab):
        settingsTab.setObjectName(_fromUtf8("settingsTab"))
        settingsTab.resize(215, 191)
        self.gridLayout = QtGui.QGridLayout(settingsTab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.saveSettings = QtGui.QPushButton(settingsTab)
        self.saveSettings.setAutoDefault(False)
        self.saveSettings.setDefault(True)
        self.saveSettings.setObjectName(_fromUtf8("saveSettings"))
        self.gridLayout.addWidget(self.saveSettings, 5, 2, 1, 1)
        self.browseOutputDirectory = QtGui.QPushButton(settingsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browseOutputDirectory.sizePolicy().hasHeightForWidth())
        self.browseOutputDirectory.setSizePolicy(sizePolicy)
        self.browseOutputDirectory.setMinimumSize(QtCore.QSize(25, 25))
        self.browseOutputDirectory.setMaximumSize(QtCore.QSize(25, 25))
        self.browseOutputDirectory.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/fileopen.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browseOutputDirectory.setIcon(icon)
        self.browseOutputDirectory.setIconSize(QtCore.QSize(16, 16))
        self.browseOutputDirectory.setObjectName(_fromUtf8("browseOutputDirectory"))
        self.gridLayout.addWidget(self.browseOutputDirectory, 2, 1, 1, 1)
        self.monitorAudio = QtGui.QCheckBox(settingsTab)
        self.monitorAudio.setChecked(True)
        self.monitorAudio.setObjectName(_fromUtf8("monitorAudio"))
        self.gridLayout.addWidget(self.monitorAudio, 0, 0, 1, 1)
        self.outputLocation = QtGui.QLineEdit(settingsTab)
        self.outputLocation.setMaximumSize(QtCore.QSize(600, 16777215))
        self.outputLocation.setObjectName(_fromUtf8("outputLocation"))
        self.gridLayout.addWidget(self.outputLocation, 2, 0, 1, 1)
        self.outputFileName = QtGui.QLineEdit(settingsTab)
        self.outputFileName.setMaximumSize(QtCore.QSize(600, 16777215))
        self.outputFileName.setObjectName(_fromUtf8("outputFileName"))
        self.gridLayout.addWidget(self.outputFileName, 3, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(0, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        self.recordingSampleRate = QtGui.QComboBox(settingsTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recordingSampleRate.sizePolicy().hasHeightForWidth())
        self.recordingSampleRate.setSizePolicy(sizePolicy)
        self.recordingSampleRate.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.recordingSampleRate.setObjectName(_fromUtf8("recordingSampleRate"))
        self.recordingSampleRate.addItem(_fromUtf8(""))
        self.recordingSampleRate.setItemText(0, _fromUtf8("44100"))
        self.recordingSampleRate.addItem(_fromUtf8(""))
        self.recordingSampleRate.setItemText(1, _fromUtf8("48000"))
        self.recordingSampleRate.addItem(_fromUtf8(""))
        self.recordingSampleRate.setItemText(2, _fromUtf8("96000"))
        self.gridLayout.addWidget(self.recordingSampleRate, 1, 0, 1, 2)

        self.retranslateUi(settingsTab)
        QtCore.QMetaObject.connectSlotsByName(settingsTab)

    def retranslateUi(self, settingsTab):
        settingsTab.setWindowTitle(_translate("settingsTab", "Form", None))
        self.saveSettings.setText(_translate("settingsTab", "Save", None))
        self.monitorAudio.setText(_translate("settingsTab", "Monitor Audio", None))

import resources_rc
