#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Main entry point for the FrontEnd of the application.
PySide and QtWebKit.
"""

__pyver__ = ['2.7.4']
__created__ = ['3.3.2012']
__authors__ = ['Toby <codenamekt@gmail.com>']
__copyright__ = ['GNU GPL v3 <http://www.gnu.org/licenses/gpl.html>']
__shortdoc__ = 'Package initialization.'

import os
import sys
from PySide import QtGui
from PySide.QtWebKit import QWebSettings
from ui.mainwindow import Ui_MainWindow

LOCAL_FILE = os.path.realpath(__file__)
LOCAL_DIR = os.path.dirname(LOCAL_FILE)


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def load_preview_from_local(self, abs_path, index):
        """
        Loads a file into the previewer tab.
        :rtype : boolean

        :param abs_path
        :type abs_path: str
        Path to file to load in preview tab.

        :param index: filename
        :type index: str
        Filename to open in preview tab.
        """
        f = open(os.path.join(abs_path, index), 'r')
        html = f.read()
        f.close()
        self.ui.browser.settings().setAttribute(QWebSettings.LocalContentCanAccessRemoteUrls, True)
        self.ui.browser.setHtml(html)

        return True

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    abs_index_path = os.path.join(LOCAL_DIR, "site")
    main.load_preview_from_local(abs_path=abs_index_path, index="index.html")
    main.show()
    sys.exit(app.exec_())
