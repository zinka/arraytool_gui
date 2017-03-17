#! /usr/bin/env python

# Author: Srinivasa Rao Zinka (srinivas . zinka [at] gmail . com)
# Copyright (c) 2017 Srinivasa Rao Zinka
# License: New BSD License.

import sys
import os
from PySide import QtCore, QtGui
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import logging
import set_restore as sr
import arraytool

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class QtHandler(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self)
    def emit(self, record):
        record = self.format(record)
        if record: XStream.stdout().write('%s\n'%record)
        # originally: XStream.stdout().write("{}\n".format(record))

logger = logging.getLogger(__name__)
handler = QtHandler()
handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

class XStream(QtCore.QObject):
    _stdout = None
    _stderr = None
    messageWritten = QtCore.Signal(str)
    def flush( self ):
        pass
    def fileno( self ):
        return -1
    def write( self, msg ):
        if ( not self.signalsBlocked() ):
            self.messageWritten.emit(unicode(msg))
    @staticmethod
    def stdout():
        if ( not XStream._stdout ):
            XStream._stdout = XStream()
            sys.stdout = XStream._stdout
        return XStream._stdout
    @staticmethod
    def stderr():
        if ( not XStream._stderr ):
            XStream._stderr = XStream()
            sys.stderr = XStream._stderr
        return XStream._stderr

class ExampleApp(QtGui.QMainWindow, arraytool.Ui_MainWindow):
    def __init__(self):

        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.showMaximized()

        # Settings icons for posix systems
        if(os.name == 'posix'):
            self.action_New.setIcon(QtGui.QIcon.fromTheme("window-new"))
            self.action_Open.setIcon(QtGui.QIcon.fromTheme("document-open"))
            self.action_Save.setIcon(QtGui.QIcon.fromTheme("document-save"))
            self.actionSave_As.setIcon(QtGui.QIcon.fromTheme("document-save-as"))
            self.action_Quit.setIcon(QtGui.QIcon.fromTheme("application-exit"))
            self.action_Preferences.setIcon(QtGui.QIcon.fromTheme("document-properties"))
            self.actionArraytool_Help.setIcon(QtGui.QIcon.fromTheme("help-contents"))
            self.actionRun.setIcon(QtGui.QIcon.fromTheme("system-run"))
            self.actionClear_Data.setIcon(QtGui.QIcon.fromTheme("edit-clear"))
            self.actionAbout.setIcon(QtGui.QIcon.fromTheme("help-about"))

        # Restoring UI settings
        self.settings = QtCore.QSettings(
            'settings.ini', QtCore.QSettings.IniFormat)
        sr.guirestore(self)

        # Adjusting splitter geometry
        screenShape = QtGui.QDesktopWidget().screenGeometry()
        self.splitter.setSizes(
            [0.5 * screenShape.width(), 0.5 * screenShape.width()])

        # Validating input data
        self.linefreq.setValidator(QtGui.QDoubleValidator(0, 0, 2))
        self.linea.setValidator(QtGui.QDoubleValidator(0, 0, 2))
        self.lineb.setValidator(QtGui.QDoubleValidator(0, 0, 2))
        self.linegamma.setValidator(QtGui.QDoubleValidator(0, 0, 2))
        self.linescant.setValidator(QtGui.QDoubleValidator(0, 0, 2))
        self.linescanp.setValidator(QtGui.QDoubleValidator(0, 0, 2))
        self.linescanx.setValidator(QtGui.QDoubleValidator(0, 0, 2))
        self.linescany.setValidator(QtGui.QDoubleValidator(0, 0, 2))
        self.linenoeX.setValidator(QtGui.QIntValidator(0, 10e6))
        self.linebwX.setValidator(QtGui.QDoubleValidator(0, 0, 2))
        self.lineslrX.setValidator(QtGui.QDoubleValidator(0, 0, 2))
        self.linembar.setValidator(QtGui.QIntValidator(0, 10e6))
        self.linenoeY.setValidator(QtGui.QIntValidator(0, 10e6))
        self.linebwY.setValidator(QtGui.QDoubleValidator(0, 0, 2))
        self.lineslrY.setValidator(QtGui.QDoubleValidator(0, 0, 2))
        self.linenbar.setValidator(QtGui.QIntValidator(0, 10e6))
        self.linenoeR.setValidator(QtGui.QIntValidator(0, 10e6))
        self.linebwR.setValidator(QtGui.QDoubleValidator(0, 0, 2))
        self.lineslrR.setValidator(QtGui.QDoubleValidator(0, 0, 2))
        self.linepbar.setValidator(QtGui.QIntValidator(0, 10e6))
        self.linescanfreq.setValidator(QtGui.QDoubleValidator(0, 0, 2))
        self.lineabits.setValidator(QtGui.QIntValidator(0, 10e6))
        self.linepbits.setValidator(QtGui.QIntValidator(0, 10e6))
        self.linedblimit.setValidator(
            QtGui.QDoubleValidator(0, 0, 2))  # positive

        # writting the log data
        self.textLog1 = QtGui.QTextBrowser()
        self.textLog1.setObjectName(_fromUtf8("textLog"))
        self.verticalLayout_13.addWidget(self.textLog1)
        XStream.stdout().messageWritten.connect( self.textLog1.insertPlainText )
        XStream.stderr().messageWritten.connect( self.textLog1.insertPlainText )
        self.pushplotspec.clicked.connect(self.test)

    def closeEvent(self, event):
        result = QtGui.QMessageBox.question(self,
                                            "Confirm Exit...",
                                            "Are you sure you want to exit ?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        event.ignore()

        if result == QtGui.QMessageBox.Yes:
            sr.guisave(self)  # Saving UI settings
            event.accept()

    def test( self ):
        self.tabWidget.setCurrentIndex(3)
        logger.debug('debug message')
        logger.info('info message')
        logger.warning('warning message')
        logger.error('error message')

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()                 # We set the form to be our ExampleApp (arraytool)
    form.show()                         # Show the form
    sys.exit(app.exec_())               # and execute the app

if __name__ == '__main__':
    main()

# ==============================================================================
# Notes section
# ==============================================================================

# TODO try to insert a Mayavi figure into the GUI ... then rid of Matplotlib for 3d plots
# TODO Make 3dplots tab as contour plot tab and plot all 3D plots as seperate mlab windows
# TODO write seperate windows (e.g., preferences, plot specs, etc) and call backs for various actions such as new file, save file, etc.
# TODO save a backup .ini file and check whether this file is matching with the new file or not then ask for confirmation to save the new file
# TODO try to provide status tips as well for all the widgets
