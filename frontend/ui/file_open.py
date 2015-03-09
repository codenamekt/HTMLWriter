# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend/resources/file_open.ui'
#
# Created: Sun Mar 08 21:38:34 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 117)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 70, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 331, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(30, 40, 341, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Filename", None, QtGui.QApplication.UnicodeUTF8))

