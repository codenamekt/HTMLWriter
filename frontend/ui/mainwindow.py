# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend/resources/mainwindow.ui'
#
# Created: Sun Mar 08 21:38:33 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 1, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.edit_tab = QtGui.QWidget()
        self.edit_tab.setObjectName("edit_tab")
        self.editor = QtWebKit.QWebView(self.edit_tab)
        self.editor.setGeometry(QtCore.QRect(0, 0, 781, 531))
        self.editor.setObjectName("editor")
        self.tabWidget.addTab(self.edit_tab, "")
        self.preview_tab = QtGui.QWidget()
        self.preview_tab.setObjectName("preview_tab")
        self.previewer = QtWebKit.QWebView(self.preview_tab)
        self.previewer.setGeometry(QtCore.QRect(0, 0, 781, 531))
        self.previewer.setObjectName("previewer")
        self.tabWidget.addTab(self.preview_tab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionRecent = QtGui.QAction(MainWindow)
        self.actionRecent.setObjectName("actionRecent")
        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionRecent)
        self.menuView.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_tab.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>This</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.edit_tab), QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.preview_tab), QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent.setText(QtGui.QApplication.translate("MainWindow", "Recent...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

from PySide import QtWebKit
