# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created: Sun Nov 29 15:46:38 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(224, 98)
        Dialog.setMinimumSize(QtCore.QSize(224, 98))
        Dialog.setMaximumSize(QtCore.QSize(224, 98))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButtonClient = QtGui.QPushButton(Dialog)
        self.pushButtonClient.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButtonClient.setMaximumSize(QtCore.QSize(100, 80))
        self.pushButtonClient.setAutoDefault(False)
        self.pushButtonClient.setObjectName(_fromUtf8("pushButtonClient"))
        self.gridLayout.addWidget(self.pushButtonClient, 0, 0, 1, 1)
        self.pushButtonServer = QtGui.QPushButton(Dialog)
        self.pushButtonServer.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButtonServer.setMaximumSize(QtCore.QSize(100, 80))
        self.pushButtonServer.setAutoDefault(False)
        self.pushButtonServer.setObjectName(_fromUtf8("pushButtonServer"))
        self.gridLayout.addWidget(self.pushButtonServer, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButtonClient.setText(_translate("Dialog", "Client", None))
        self.pushButtonServer.setText(_translate("Dialog", "Server", None))

