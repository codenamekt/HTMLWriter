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
__shortdoc__ = 'frontend'

import os
import sys
from PySide import QtGui
from PySide.QtWebKit import QWebSettings
from ui.mainwindow import Ui_MainWindow

LOCAL_FILE = os.path.realpath(__file__)
LOCAL_DIR = os.path.dirname(LOCAL_FILE)


class FileParse:
    # Todo: Read write from monogdb
    def __init__(self, abs_path, index):
        self.file_path = os.path.join(abs_path, index)
        self.data = self.refresh()

    def read(self):
        """
        Returns data from reading file.
        :rtype : str
        """
        with open(self.file_path, 'r') as f:
            data = f.read()
            f.close()

        return data


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Setting to allow local file.
        self.ui.browser.settings().setAttribute(QWebSettings.LocalContentCanAccessRemoteUrls, True)
        self.local_file = None

    def load_local_file(self, abs_path=None, index=None):
        """
        Loads a file into the previewer tab.
        :type self: MainWindow
        :rtype : boolean

        :param abs_path
        :type abs_path: str
        Path to file to load in preview tab.

        :param index: filename
        :type index: str
        Filename to open in preview tab.
        """
        if abs_path and index:
            self.local_file = FileParse(abs_path, index)
        elif self.local_file:
            pass
        else:
            # Todo: Change to warning dialog
            raise NotImplementedError("Change to dialog")

        self.ui.browser.setHtml(self.local_file.data)

        return True

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    abs_index_path = os.path.join(LOCAL_DIR, "site")
    main.load_local_file(abs_path=abs_index_path, index="index.html")
    main.show()
    sys.exit(app.exec_())
