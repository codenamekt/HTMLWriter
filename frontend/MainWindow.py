#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
class MainWindow
"""

__pyver__ = ['2.7.9']
__created__ = ['3.8.2015']
__authors__ = ['Toby <codenamekt@gmail.com>']
__copyright__ = ['GNU GPL v3 <http://www.gnu.org/licenses/gpl.html>']
__shortdoc__ = 'frontend'

import os
from PySide import QtGui
from FileParse import FileParse
from PySide.QtWebKit import QWebSettings
from ui.mainwindow import Ui_MainWindow

LOCAL_FILE = os.path.realpath(__file__)
LOCAL_DIR = os.path.dirname(LOCAL_FILE)


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Setting to allow local file.
        self.ui.editor.settings().setAttribute(QWebSettings.LocalContentCanAccessRemoteUrls, True)
        self.ui.previewer.settings().setAttribute(QWebSettings.LocalContentCanAccessRemoteUrls, True)

    def load_preview(self, abs_file_path):
        """
        Loads a file into the previewer tab.
        :type self: MainWindow

        :param abs_file_path
        :type abs_file_path: str
        Absolute path to file to load in preview tab.

        :rtype : boolean
        """
        # Check if absolute path.
        if not os.path.abspath(abs_file_path):
            # Todo: Change to warning dialog: Input must be absolute path.
            raise NotImplementedError("Change to dialog: Input must be absolute path.")
        # Check if file.
        if not os.path.isfile(abs_file_path):
            # Todo: Change to warning dialog: Input must be file.
            raise NotImplementedError("Change to dialog: Input must be file.")

        self.ui.previewer.setHtml(FileParse(abs_file_path=abs_file_path).data)

        return True

    def load_edit(self, abs_file_path):
        """
        Loads a file into the editor tab.
        :type self: MainWindow

        :param abs_file_path
        :type abs_file_path: str
        Absolute path to file to load in preview tab.

        :rtype : boolean
        """
        # Check if absolute path.
        if not os.path.abspath(abs_file_path):
            # Todo: Change to warning dialog: Input must be absolute path.
            raise NotImplementedError("Change to dialog: Input must be absolute path.")
        # Check if file.
        if not os.path.isfile(abs_file_path):
            # Todo: Change to warning dialog: Input must be file.
            raise NotImplementedError("Change to dialog: Input must be file.")

        self.ui.editor.setHtml(FileParse(abs_file_path=abs_file_path).data)

        return True
