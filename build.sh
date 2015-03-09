#!/bin/bash
# Todo: Also add minification scripts.
rm frontend/ui/mainwindow.py
pyside-uic -o frontend/ui/mainwindow.py frontend/resources/mainwindow.ui
rm frontend/ui/file_new.py
pyside-uic -o frontend/ui/file_new.py frontend/resources/file_new.ui
rm frontend/ui/file_open.py
pyside-uic -o frontend/ui/file_open.py frontend/resources/file_open.ui