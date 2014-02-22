#!/usr/bin/env python
# coding=utf-8

import os
import sys
import shutil
import glob
import re

from PyQt4 import QtGui
from PyQt4.uic import compileUiDir

if getattr(sys, 'frozen', False):
    basedir = sys._MEIPASS
else:
    basedir = os.path.dirname(__file__)
    compileUiDir(os.path.join(basedir, 'audio', 'resources'))
    for file_ in glob.glob(os.path.join(basedir, 'audio', 'resources', '*.py')):
        infile = open(file_)
        outfile = open(os.path.join(basedir, 'audio', 'ui', os.path.basename(file_)), 'w')
        for i in infile:
            n = re.sub(r'(#\s*Created:.*)', '#', i)
            a = re.sub(r'(#\s*by:.*)', '#', n)
            outfile.write(a)
        infile.close()
        outfile.close()
        if os.path.exists(file_):
            os.remove(file_)

from audio.ui.mainwindowform import MainWindow

__version__ = "1.0.0"


#     def updatestatus(self, message):
#         """
#
#         :param message:
#         """
#         self.statusBar().showMessage(message, 5000)
#         self.listWidget.addItem(message)
#         if self.filename is not None:
#             self.setWindowTitle("Image Changer - {0}[*]".format(
#                 os.path.basename(self.filename)))
#         elif not self.image.isNull():
#             self.setWindowTitle("Image Changer - Unnamed[*]")
#         else:
#             self.setWindowTitle("Image Changer[*]")
#         self.setWindowModified(self.dirty)
#
#     def loadfile(self, fname=None):
#         """
#
#         :param fname:
#         :return:
#         """
#         if fname is None:
#             action = self.sender()
#             if isinstance(action, QtGui.QAction):
#                 fname = unicode(action.data().toString())
#                 if not self.oktocontinue():
#                     return
#             else:
#                 return
#         if fname:
#             self.filename = None
#             image = QtGui.QImage(fname)
#             if image.isNull():
#                 message = "Failed to read {0}".format(fname)
#             else:
#                 self.addRecentFile(fname)
#                 self.image = QtGui.QImage()
#                 self.image = image
#                 self.filename = fname
#                 self.showImage()
#                 self.dirty = False
#                 self.sizeLabel.setText("{0} x {1}".format(image.width(), image.height()))
#                 message = "Loaded {0}".format(os.path.basename(fname))
#             self.updatestatus(message)
#
#     def filesave(self):
#         """
#
#
#         :return:
#         """
#         if self.image.isNull():
#             return True
#         if self.filename is None:
#             return self.filesaveas()
#         else:
#             if self.image.save(self.filename, None):
#                 self.updatestatus("Saved as {0}".format(self.filename))
#                 self.dirty = False
#                 return True
#             else:
#                 self.updatestatus("Failed to save {0}".format(self.filename))
#                 return False
#
#     def filesaveas(self):
#         """
#
#
#         :return:
#         """
#         if self.image.isNull():
#             return True
#         fname = self.filename if self.filename is not None else "."
#         formats = (["*.{0}".format(unicode(format).lower())
#                     for format in QtGui.QImageWriter.supportedImageFormats()])
#         fname = unicode(QtGui.QFileDialog.getSaveFileName(self,
#                                                           "Image Changer - Save Image", fname,
#                                                           "Image files ({0})".format(" ".join(formats))))
#         if fname:
#             if "." not in fname:
#                 fname += ".png"
#             self.addRecentFile(fname)
#             self.filename = fname
#             return self.filesave()
#         return False
#


def main():
    app = QtGui.QApplication(sys.argv)
    app.setOrganizationName("springermac")
    app.setApplicationName("Audio")
    app.setWindowIcon(QtGui.QIcon(":/icon.png"))
    form = MainWindow()
    form.show()
    app.exec_()


main()
