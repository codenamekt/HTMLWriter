#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
Main
"""

__pyver__ = ['2.7.7', '2.7.9']
__created__ = ['3.3.2015']
__authors__ = ['Toby <codenamekt@gmail.com>']
__copyright__ = ['GNU GPL v3 <http://www.gnu.org/licenses/gpl.html>']
__shortdoc__ = 'frontend'

import os
import sys
from PySide import QtGui
from MainWindow import MainWindow

LOCAL_FILE = os.path.realpath(__file__)
LOCAL_DIR = os.path.dirname(LOCAL_FILE)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main = MainWindow()
    # Todo: Handle files that are relative instead of absolute. (Maybe show cwd in dialog)
    abs_preview_index_path = os.path.join(LOCAL_DIR, "preview", "index.html")
    main.load_preview(abs_file_path=abs_preview_index_path)
    main.show()
    sys.exit(app.exec_())
