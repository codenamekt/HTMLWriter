#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Package initialization.
'''

__pyver__ = ['3.2.3']
__created__ = ['6.7.2012']
__authors__ = ['vital-fadeev <http://VFadeev.ru>',
               'Toby <codenamekt@gmail.com>']
__copyright__ = ['GNU GPL v3 <http://www.gnu.org/licenses/gpl.html>']
__shortdoc__ = 'Package initialization.'


def main(value):
    """
    Return 'value'.
    >>> main(1)
    1
    >>> main(2)
    2
    >>> main(3)
    3
    """
    return value

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
