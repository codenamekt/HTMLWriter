#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

setup(
    name='HTMLWriter',
    version='0.0.1',
    author='Tobias Stevenson',
    author_email='codenamekt@gmail.com',
    url='http://www.HTMLWriter.org',
    download_url='http://www.HTMLWriter.org/files/',
    description='Short description of HTMLWriter...',
    long_description='Long description of HTMLWriter...',
    
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.txt', '*.rst'],
        'HTMLWriter': ['data/*.html', 'data/*.css'],
    },
    exclude_package_data={'': ['README.rst']},
    
    scripts=['HTMLWriter/frontend/main.py'],
    
    keywords='python tools utils internet www',
    license='GPL',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2',
                 ('License :: OSI Approved :: GNU Library or Lesser',
                  ' General Public License (LGPL)'),
                 ('License :: OSI Approved :: GNU Affero General Public ',
                  'License v3'),
                 'Topic :: Internet',
                 'Topic :: Internet :: WWW/HTTP'],
    
    setup_requires=[],
    install_requires=['setuptools']
)
