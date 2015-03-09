# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frontend/resources/file_new.ui'
#
# Created: Sun Mar 08 21:38:34 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_file_new(object):
    def setupUi(self, file_new):
        file_new.setObjectName("file_new")
        file_new.resize(400, 117)
        file_new.setModal(True)
        self.buttonBox = QtGui.QDialogButtonBox(file_new)
        self.buttonBox.setGeometry(QtCore.QRect(30, 70, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(file_new)
        self.label.setGeometry(QtCore.QRect(40, 20, 331, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtGui.QLineEdit(file_new)
        self.lineEdit.setGeometry(QtCore.QRect(30, 40, 341, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(file_new)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), file_new.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), file_new.reject)
        QtCore.QMetaObject.connectSlotsByName(file_new)

    def retranslateUi(self, file_new):
        file_new.setWindowTitle(QtGui.QApplication.translate("file_new", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("file_new", "Filename", None, QtGui.QApplication.UnicodeUTF8))

