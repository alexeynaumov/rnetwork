# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created: Sun Nov 29 15:25:02 2015
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
        self.listWidgetClients = QtGui.QListWidget(Dialog)
        self.listWidgetClients.setMinimumSize(QtCore.QSize(160, 80))
        self.listWidgetClients.setMaximumSize(QtCore.QSize(160, 16777215))
        self.listWidgetClients.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidgetClients.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidgetClients.setObjectName(_fromUtf8("listWidgetClients"))
        self.gridLayout.addWidget(self.listWidgetClients, 4, 1, 1, 1)
        self.spinBoxPort = QtGui.QSpinBox(Dialog)
        self.spinBoxPort.setMinimumSize(QtCore.QSize(160, 27))
        self.spinBoxPort.setMaximumSize(QtCore.QSize(160, 27))
        self.spinBoxPort.setMinimum(1)
        self.spinBoxPort.setMaximum(65535)
        self.spinBoxPort.setProperty("value", 80)
        self.spinBoxPort.setObjectName(_fromUtf8("spinBoxPort"))
        self.gridLayout.addWidget(self.spinBoxPort, 1, 1, 1, 1)
        self.checkBoxRawText = QtGui.QCheckBox(Dialog)
        self.checkBoxRawText.setObjectName(_fromUtf8("checkBoxRawText"))
        self.gridLayout.addWidget(self.checkBoxRawText, 10, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textEditTraffic = QtGui.QTextEdit(Dialog)
        self.textEditTraffic.setEnabled(False)
        self.textEditTraffic.setObjectName(_fromUtf8("textEditTraffic"))
        self.verticalLayout.addWidget(self.textEditTraffic)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
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
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 12, 1)
        self.labelClients = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelClients.setFont(font)
        self.labelClients.setObjectName(_fromUtf8("labelClients"))
        self.gridLayout.addWidget(self.labelClients, 3, 1, 1, 1)
        self.labelFormat = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelFormat.setFont(font)
        self.labelFormat.setObjectName(_fromUtf8("labelFormat"))
        self.gridLayout.addWidget(self.labelFormat, 7, 1, 1, 1)
        self.comboBoxFormat = QtGui.QComboBox(Dialog)
        self.comboBoxFormat.setMinimumSize(QtCore.QSize(160, 0))
        self.comboBoxFormat.setMaximumSize(QtCore.QSize(160, 16777215))
        self.comboBoxFormat.setObjectName(_fromUtf8("comboBoxFormat"))
        self.comboBoxFormat.addItem(_fromUtf8(""))
        self.comboBoxFormat.addItem(_fromUtf8(""))
        self.comboBoxFormat.addItem(_fromUtf8(""))
        self.comboBoxFormat.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBoxFormat, 8, 1, 1, 1)
        self.labelPort = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPort.setFont(font)
        self.labelPort.setObjectName(_fromUtf8("labelPort"))
        self.gridLayout.addWidget(self.labelPort, 0, 1, 1, 1)
        self.checkBoxLeadingZeroes = QtGui.QCheckBox(Dialog)
        self.checkBoxLeadingZeroes.setObjectName(_fromUtf8("checkBoxLeadingZeroes"))
        self.gridLayout.addWidget(self.checkBoxLeadingZeroes, 9, 1, 1, 1)
        self.checkBoxTimestamp = QtGui.QCheckBox(Dialog)
        self.checkBoxTimestamp.setObjectName(_fromUtf8("checkBoxTimestamp"))
        self.gridLayout.addWidget(self.checkBoxTimestamp, 11, 1, 1, 1)
        self.pushButtonStartStop = QtGui.QPushButton(Dialog)
        self.pushButtonStartStop.setMinimumSize(QtCore.QSize(160, 0))
        self.pushButtonStartStop.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonStartStop.setFont(font)
        self.pushButtonStartStop.setAutoDefault(False)
        self.pushButtonStartStop.setObjectName(_fromUtf8("pushButtonStartStop"))
        self.gridLayout.addWidget(self.pushButtonStartStop, 2, 1, 1, 1)
        self.labelPeerAddress = QtGui.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelPeerAddress.setFont(font)
        self.labelPeerAddress.setObjectName(_fromUtf8("labelPeerAddress"))
        self.gridLayout.addWidget(self.labelPeerAddress, 5, 1, 1, 1)
        self.lineEditPeerAddress = QtGui.QLineEdit(Dialog)
        self.lineEditPeerAddress.setMinimumSize(QtCore.QSize(160, 0))
        self.lineEditPeerAddress.setMaximumSize(QtCore.QSize(160, 16777215))
        self.lineEditPeerAddress.setReadOnly(True)
        self.lineEditPeerAddress.setObjectName(_fromUtf8("lineEditPeerAddress"))
        self.gridLayout.addWidget(self.lineEditPeerAddress, 6, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.pushButtonStartStop, self.lineEditData)
        Dialog.setTabOrder(self.lineEditData, self.pushButtonSend)
        Dialog.setTabOrder(self.pushButtonSend, self.spinBoxPort)
        Dialog.setTabOrder(self.spinBoxPort, self.comboBoxFormat)
        Dialog.setTabOrder(self.comboBoxFormat, self.checkBoxLeadingZeroes)
        Dialog.setTabOrder(self.checkBoxLeadingZeroes, self.checkBoxRawText)
        Dialog.setTabOrder(self.checkBoxRawText, self.checkBoxTimestamp)
        Dialog.setTabOrder(self.checkBoxTimestamp, self.textEditTraffic)
        Dialog.setTabOrder(self.textEditTraffic, self.listWidgetClients)
        Dialog.setTabOrder(self.listWidgetClients, self.lineEditPeerAddress)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "TCP debugger (server) - 1.1.1", None))
        self.checkBoxRawText.setText(_translate("Dialog", "Raw text", None))
        self.pushButtonSend.setText(_translate("Dialog", "Send", None))
        self.labelClients.setText(_translate("Dialog", "Clients:", None))
        self.labelFormat.setText(_translate("Dialog", "Format:", None))
        self.comboBoxFormat.setItemText(0, _translate("Dialog", "Bin", None))
        self.comboBoxFormat.setItemText(1, _translate("Dialog", "Oct", None))
        self.comboBoxFormat.setItemText(2, _translate("Dialog", "Dec", None))
        self.comboBoxFormat.setItemText(3, _translate("Dialog", "Hex", None))
        self.labelPort.setText(_translate("Dialog", "Port:", None))
        self.checkBoxLeadingZeroes.setText(_translate("Dialog", "Leading zeroes", None))
        self.checkBoxTimestamp.setText(_translate("Dialog", "Timestamp", None))
        self.pushButtonStartStop.setText(_translate("Dialog", "Start", None))
        self.labelPeerAddress.setText(_translate("Dialog", "Peer address:", None))

