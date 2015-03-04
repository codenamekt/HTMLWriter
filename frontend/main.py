#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Main entry point for the FrontEnd of the application.
QT and Webkit.
'''

__pyver__ = ['3.2.3']
__created__ = ['3.3.2012']
__authors__ = ['Toby <codenamekt@gmail.com>']
__copyright__ = ['GNU GPL v3 <http://www.gnu.org/licenses/gpl.html>']
__shortdoc__ = 'Package initialization.'

import sys
from PySide import QtGui
from mainwindow import Ui_MainWindow


class Control(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Control, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = Control()
    mySW.show()
    sys.exit(app.exec_())
