#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
##########
Main Tests
##########

You should run this through the makefile in the main folder
'''

import unittest

from tornado import testing
from tornado.web import Application
from Backend.main import MainHandler

__pyver__ = ['3.2.3']
__created__ = ['6.7.2012']
__authors__ = ['Toby <codenamekt@gmail.com>']
__copyright__ = ['GNU GPL v3 <http://www.gnu.org/licenses/gpl.html>']
__shortdoc__ = 'Main entry point for tests.'


class MyHTTPTest(testing.AsyncHTTPTestCase):
    def get_app(self):
        return Application([('/', MainHandler)])

    def test_homepage(self):
        self.http_client.fetch(self.get_url('/'), self.stop)
        response = self.wait()
        self.assertEqual("Hello, world", response.body)


if __name__ == "__main__":
    unittest.main()
