# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created: Sat Dec  5 02:42:57 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from rhelpers.widgets import LineEdit

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
        Dialog.resize(900, 600)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.textEditTraffic = QtGui.QTextEdit(Dialog)
        self.textEditTraffic.setEnabled(False)
        self.textEditTraffic.setObjectName(_fromUtf8("textEditTraffic"))
        self.verticalLayout_2.addWidget(self.textEditTraffic)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineEditData = LineEdit(Dialog)
        self.lineEditData.setEnabled(False)
        self.lineEditData.setObjectName(_fromUtf8("lineEditData"))
        self.horizontalLayout.addWidget(self.lineEditData)
        self.pushButtonSend = QtGui.QPushButton(Dialog)
        self.pushButtonSend.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonSend.setFont(font)
        self.pushButtonSend.setAutoDefault(False)
        self.pushButtonSend.setObjectName(_fromUtf8("pushButtonSend"))
        self.horizontalLayout.addWidget(self.pushButtonSend)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 11, 1)
        self.labelHost = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelHost.setFont(font)
        self.labelHost.setObjectName(_fromUtf8("labelHost"))
        self.gridLayout.addWidget(self.labelHost, 0, 1, 1, 1)
        self.lineEditHost = QtGui.QLineEdit(Dialog)
        self.lineEditHost.setMinimumSize(QtCore.QSize(160, 0))
        self.lineEditHost.setMaximumSize(QtCore.QSize(160, 16777215))
        self.lineEditHost.setObjectName(_fromUtf8("lineEditHost"))
        self.gridLayout.addWidget(self.lineEditHost, 1, 1, 1, 1)
        self.labelPort = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPort.setFont(font)
        self.labelPort.setObjectName(_fromUtf8("labelPort"))
        self.gridLayout.addWidget(self.labelPort, 2, 1, 1, 1)
        self.spinBoxPort = QtGui.QSpinBox(Dialog)
        self.spinBoxPort.setMinimumSize(QtCore.QSize(160, 0))
        self.spinBoxPort.setMaximumSize(QtCore.QSize(160, 16777215))
        self.spinBoxPort.setMinimum(1)
        self.spinBoxPort.setMaximum(65535)
        self.spinBoxPort.setProperty("value", 80)
        self.spinBoxPort.setObjectName(_fromUtf8("spinBoxPort"))
        self.gridLayout.addWidget(self.spinBoxPort, 3, 1, 1, 1)
        self.pushButtonConnectDisconnect = QtGui.QPushButton(Dialog)
        self.pushButtonConnectDisconnect.setMinimumSize(QtCore.QSize(160, 0))
        self.pushButtonConnectDisconnect.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonConnectDisconnect.setFont(font)
        self.pushButtonConnectDisconnect.setAutoDefault(False)
        self.pushButtonConnectDisconnect.setFlat(False)
        self.pushButtonConnectDisconnect.setObjectName(_fromUtf8("pushButtonConnectDisconnect"))
        self.gridLayout.addWidget(self.pushButtonConnectDisconnect, 4, 1, 1, 1)
        self.labelFormat = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelFormat.setFont(font)
        self.labelFormat.setObjectName(_fromUtf8("labelFormat"))
        self.gridLayout.addWidget(self.labelFormat, 5, 1, 1, 1)
        self.comboBoxFormat = QtGui.QComboBox(Dialog)
        self.comboBoxFormat.setMinimumSize(QtCore.QSize(160, 0))
        self.comboBoxFormat.setMaximumSize(QtCore.QSize(160, 16777215))
        self.comboBoxFormat.setObjectName(_fromUtf8("comboBoxFormat"))
        self.comboBoxFormat.addItem(_fromUtf8(""))
        self.comboBoxFormat.addItem(_fromUtf8(""))
        self.comboBoxFormat.addItem(_fromUtf8(""))
        self.comboBoxFormat.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBoxFormat, 6, 1, 1, 1)
        self.checkBoxLeadingZeroes = QtGui.QCheckBox(Dialog)
        self.checkBoxLeadingZeroes.setObjectName(_fromUtf8("checkBoxLeadingZeroes"))
        self.gridLayout.addWidget(self.checkBoxLeadingZeroes, 7, 1, 1, 1)
        self.checkBoxRawText = QtGui.QCheckBox(Dialog)
        self.checkBoxRawText.setObjectName(_fromUtf8("checkBoxRawText"))
        self.gridLayout.addWidget(self.checkBoxRawText, 8, 1, 1, 1)
        self.checkBoxTimestamp = QtGui.QCheckBox(Dialog)
        self.checkBoxTimestamp.setObjectName(_fromUtf8("checkBoxTimestamp"))
        self.gridLayout.addWidget(self.checkBoxTimestamp, 9, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(17, 237, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 10, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.comboBoxFormat.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEditHost, self.spinBoxPort)
        Dialog.setTabOrder(self.spinBoxPort, self.pushButtonConnectDisconnect)
        Dialog.setTabOrder(self.pushButtonConnectDisconnect, self.lineEditData)
        Dialog.setTabOrder(self.lineEditData, self.pushButtonSend)
        Dialog.setTabOrder(self.pushButtonSend, self.comboBoxFormat)
        Dialog.setTabOrder(self.comboBoxFormat, self.checkBoxTimestamp)
        Dialog.setTabOrder(self.checkBoxTimestamp, self.textEditTraffic)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "TCP debugger (client) - 1.1.1", None))
        self.pushButtonSend.setText(_translate("Dialog", "Send", None))
        self.labelHost.setText(_translate("Dialog", "Host:", None))
        self.lineEditHost.setText(_translate("Dialog", "localhost", None))
        self.labelPort.setText(_translate("Dialog", "Port:", None))
        self.pushButtonConnectDisconnect.setText(_translate("Dialog", "Connect", None))
        self.labelFormat.setText(_translate("Dialog", "Format:", None))
        self.comboBoxFormat.setItemText(0, _translate("Dialog", "Bin", None))
        self.comboBoxFormat.setItemText(1, _translate("Dialog", "Oct", None))
        self.comboBoxFormat.setItemText(2, _translate("Dialog", "Dec", None))
        self.comboBoxFormat.setItemText(3, _translate("Dialog", "Hex", None))
        self.checkBoxLeadingZeroes.setText(_translate("Dialog", "Leading zeroes", None))
        self.checkBoxRawText.setText(_translate("Dialog", "Raw text", None))
        self.checkBoxTimestamp.setText(_translate("Dialog", "Timestamp", None))

