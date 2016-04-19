# -*- coding: utf-8 -*-

# Copyright (C) 2015-2016 Alexey Naumov <rocketbuzzz@gmail.com>
#
# This file is part of rnetwork.
#
# rnetwork is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, os

sys.path.append(os.path.abspath("../../../rhelpers"))
sys.path.append(os.path.abspath("../../../rnetwork"))

from PyQt4.QtCore import SIGNAL, Qt, QObject, QByteArray, QTime, QSettings
from PyQt4.QtNetwork import QHostAddress
from PyQt4.QtGui import QDialog, QIcon

from rnetwork.tcp import TcpServer
from rhelpers.utils import stringToBytes, bytesToString, History
from .ui_Dialog import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)

        self.setupUi(self)
        self.__initialize()

    def __initialize(self):
        self.setWindowIcon(QIcon("./server/icons/server.svg"))

        self.__tcpServer = TcpServer()
        self.__tcpServer.onConnected = self.onConnected
        self.__tcpServer.onDisconnected = self.onDisconnected
        self.__tcpServer.onError = self.onError
        self.__tcpServer.onRead = self.onRead

        self.pushButtonStartStop.clicked.connect(self.onPushButtonStartStopClicked)
        self.pushButtonSend.clicked.connect(self.onPushButtonSendClicked)
        self.checkBoxRawText.stateChanged.connect(self.onCheckBoxRawTextStateChanged)
        self.listWidgetClients.itemClicked.connect(self.onListWidgetClientsItemClicked)
        QObject.connect(self.lineEditData, SIGNAL("keyPressed"), self.__keyPressed)

        self.__history = History()
        self.__loadSettings()

    def __keyPressed(self, key):
        if key in [Qt.Key_Enter, Qt.Key_Return]:
            self.pushButtonSend.click()

        if Qt.Key_Up == key:
            previous = self.__history.previous()
            if previous:
                self.lineEditData.setText(previous)

        if Qt.Key_Down == key:
            next = self.__history.next()
            if next:
                self.lineEditData.setText(next)

    def __postText(self, text):
        if self.checkBoxTimestamp.isChecked():
            time = QTime.currentTime().toString()
            self.textEditTraffic.append("%s - %s" % (time, text))
        else:
            self.textEditTraffic.append(text)

    def __saveSettings(self):
        settings = QSettings("Rocket Labs", "tdbgs")
        settings.setValue("port", self.spinBoxPort.value())
        settings.setValue("format", self.comboBoxFormat.currentIndex())
        settings.setValue("leadingZeroes", self.checkBoxLeadingZeroes.isChecked())
        settings.setValue("timestamp", self.checkBoxTimestamp.isChecked())
        settings.setValue("rawText", self.checkBoxRawText.isChecked())

    def __loadSettings(self):
        settings = QSettings("Rocket Labs", "tdbgs")
        self.spinBoxPort.setValue(settings.value("port", 80).toInt()[0])
        self.comboBoxFormat.setCurrentIndex(settings.value("format", 0).toInt()[0])
        self.checkBoxLeadingZeroes.setChecked(settings.value("leadingZeroes", False).toBool())
        self.checkBoxTimestamp.setChecked(settings.value("timestamp", False).toBool())
        self.checkBoxRawText.setChecked(settings.value("rawText", False).toBool())

    def closeEvent(self, event):
        self.__tcpServer.close()
        self.__saveSettings()
        super(Dialog, self).closeEvent(event)

    def onConnected(self, descriptor):
        self.listWidgetClients.addItem(str(descriptor))

    def onDisconnected(self, descriptor):
        searchString = str(descriptor)
        matchFlags = Qt.MatchExactly
        items = self.listWidgetClients.findItems(searchString, matchFlags)
        for item in items:
            row = self.listWidgetClients.row(item)
            self.listWidgetClients.takeItem(row)

    def onError(self, descriptor, error):
        self.__postText("E[%s#%s]: %s." % (error.code, descriptor, error.description))

    def onRead(self, descriptor, data):
        if self.checkBoxRawText.isChecked():
            dataFormat = "S"
            text = str(data)

        else:
            INDEX_BASE = {0: 2, 1: 8, 2: 10, 3: 16}
            index = self.comboBoxFormat.currentIndex()
            base = INDEX_BASE.get(index, None)
            if not base:
                self.__postText("E[?]: Invalid base of a number.")

            data = [ord(item) for item in data]
            text = bytesToString(data, base, self.checkBoxLeadingZeroes.isChecked())

            INDEX_FORMAT = {0: "B", 1: "O", 2: "D", 3: "H"}
            dataFormat = INDEX_FORMAT.get(index, None)
            if not dataFormat:
                self.__postText("E[?]: Invalid data format.")

        self.__postText("R[%s:%s#%s]: %s" % (dataFormat, len(data), descriptor, text))

    def onCheckBoxRawTextStateChanged(self, state):
        if state == Qt.Checked:
            self.labelFormat.setEnabled(False)
            self.comboBoxFormat.setEnabled(False)
            self.checkBoxLeadingZeroes.setEnabled(False)
        else:
            self.labelFormat.setEnabled(True)
            self.comboBoxFormat.setEnabled(True)
            self.checkBoxLeadingZeroes.setEnabled(True)

    def onListWidgetClientsItemClicked(self):
        item = self.listWidgetClients.currentItem()
        descriptor = int(item.text())
        socket = self.__tcpServer.socket(descriptor)
        if socket:
            self.lineEditPeerAddress.setText(socket.peerAddress().toString())

    def onPushButtonStartStopClicked(self):
        if self.__tcpServer.isListening():
            self.__tcpServer.close()
            self.pushButtonStartStop.setText("Start")
            self.textEditTraffic.setEnabled(False)
            self.lineEditData.setEnabled(False)
            self.pushButtonSend.setEnabled(False)
            self.listWidgetClients.clear()
        else:
            port = self.spinBoxPort.value()
            self.__tcpServer.listen(QHostAddress.Any, port)
            self.pushButtonStartStop.setText("Stop")
            self.textEditTraffic.setEnabled(True)
            self.lineEditData.setEnabled(True)
            self.pushButtonSend.setEnabled(True)

    def onPushButtonSendClicked(self):
        selectedSockets = self.listWidgetClients.selectedItems()
        if 0 == len(selectedSockets):
            self.__postText("E[?#?]: No socket(s) selected.")
            return

        text = self.lineEditData.text().simplified()
        if text.isEmpty():
            return

        data = QByteArray()

        if self.checkBoxRawText.isChecked():
            dataFormat = "S"
            data = text.toLocal8Bit()

        else:
            INDEX_BASE = {0: 2, 1: 8, 2: 10, 3: 16}
            index = self.comboBoxFormat.currentIndex()
            base = INDEX_BASE.get(index, None)
            if not base:
                self.__postText("E[?]: Invalid base of a number.")

            try:
                values = stringToBytes(str(text), base)
            except ValueError as error:
                self.__postText("E[?]: Incorrect input: <%s>." % error)

            for value in values:
                data.append(chr(value))

            INDEX_FORMAT = {0: "B", 1: "O", 2: "D", 3: "H"}
            dataFormat = INDEX_FORMAT.get(index, None)
            if not dataFormat:
                self.__postText("E[?]: Invalid data format.")

        for item in selectedSockets:
            descriptor = int(item.text())
            self.__postText("T[%s:%s#%s]: %s" % (dataFormat, len(data), descriptor, text))
            self.__tcpServer.write(descriptor, data)

        self.__history.add(self.lineEditData.text())
        self.lineEditData.clear()