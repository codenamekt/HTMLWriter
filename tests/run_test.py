#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
##########
Main Tests
##########

You should run this through the makefile in the main folder
'''

__pyver__ = ['3.2.3']
__created__ = ['6.7.2012']
__authors__ = ['vital-fadeev <http://VFadeev.ru>',
               'Toby <codenamekt@gmail.com>']
__copyright__ = ['GNU GPL v3 <http://www.gnu.org/licenses/gpl.html>']
__shortdoc__ = 'Main entry point for tests.'

import unittest

from my_program.run import main


class Test(unittest.TestCase):
    """Unit tests for main()"""

    def test_main(self):
        """Test result"""
        value = True
        result = main(value)
        self.assertEqual(value, result)

    #def test_doctest(self):
        #import doctest
        #import my_program.utils
        #doctest.testmod(my_program.utils)


if __name__ == "__main__":
    unittest.main()
