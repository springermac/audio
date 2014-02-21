# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/jonathanspringer/projects/audio/audio-program/audio/resources/recordingtab.ui'
#
# Created: Fri Feb 21 03:32:52 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_recordingTab(object):
    def setupUi(self, recordingTab):
        recordingTab.setObjectName(_fromUtf8("recordingTab"))
        recordingTab.resize(327, 329)
        self.gridLayout = QtGui.QGridLayout(recordingTab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame_2 = QtGui.QFrame(recordingTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_8 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.pushButton = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_8.addWidget(self.pushButton, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_8.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 1, 1, 1)
        self.audioMeter = QtGui.QProgressBar(recordingTab)
        self.audioMeter.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.audioMeter.sizePolicy().hasHeightForWidth())
        self.audioMeter.setSizePolicy(sizePolicy)
        self.audioMeter.setMinimumSize(QtCore.QSize(40, 295))
        self.audioMeter.setProperty("value", 100)
        self.audioMeter.setTextVisible(False)
        self.audioMeter.setOrientation(QtCore.Qt.Vertical)
        self.audioMeter.setInvertedAppearance(True)
        self.audioMeter.setObjectName(_fromUtf8("audioMeter"))
        self.gridLayout.addWidget(self.audioMeter, 0, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)

        self.retranslateUi(recordingTab)
        QtCore.QMetaObject.connectSlotsByName(recordingTab)

    def retranslateUi(self, recordingTab):
        recordingTab.setWindowTitle(_translate("recordingTab", "Form", None))
        self.pushButton.setText(_translate("recordingTab", "Record", None))
        self.pushButton_2.setText(_translate("recordingTab", "Stop", None))

