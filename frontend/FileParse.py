#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
class FileParse
"""

__pyver__ = ['2.7.7', '2.7.9']
__created__ = ['3.8.2015']
__authors__ = ['Toby <codenamekt@gmail.com>']
__copyright__ = ['GNU GPL v3 <http://www.gnu.org/licenses/gpl.html>']
__shortdoc__ = 'frontend'

import os

LOCAL_FILE = os.path.realpath(__file__)
LOCAL_DIR = os.path.dirname(LOCAL_FILE)


class FileParse(object):
    def __init__(self, abs_file_path):
        self.file_path = abs_file_path
        self.data = self.read()

    def read(self, abs_file_path=None):
        """
        Returns data from reading file.
        Will reread file already set in file_path if no args.

        :param abs_file_path
        :type abs_file_path: str
        :rtype : str
        """
        if abs_file_path:
            self.file_path = abs_file_path
        else:
            try:
                with open(self.file_path, 'r') as f:
                    data = f.read()
                    f.close()
            except (OSError, IOError) as e:
                # Todo: I/O error dialog
                # "I/O error({0}): {1}".format(e.errno, e.strerror)
                raise NotImplementedError("Change to dialog")

        return data
