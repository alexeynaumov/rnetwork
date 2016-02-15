# -*- coding: utf-8 -*-

# Copyright (C) 2015 Alexey Naumov <rocketbuzzz@gmail.com>
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

from PyQt4.QtCore import QObject
from PyQt4.QtNetwork import QUdpSocket, QHostAddress


class UdpSocket(QObject):
    def __init__(self, parent=None):
        QObject.__init__(self, parent)
        self.__socket = QUdpSocket(self)
        self.__socket.readyRead.connect(self.__onReadyRead)
        self.__port = None
        self.__on_read = None

    def __onReadyRead(self):
        if not self.__on_read:
            return

        while self.__socket.hasPendingDatagrams():
            size = self.__socket.pendingDatagramSize()
            data, host, port = self.__socket.readDatagram(size)

            self.__on_read(data, host, port)

    def bind(self):
        if not isinstance(self.__port, int):
            raise Exception("Error setting port value.")

        self.__socket.bind(QHostAddress.Broadcast, self.port)

    def write(self, data, host, port):
        self.__socket.writeDatagram(data, host, port)
        print self.__socket.state()

    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port):
        self.__port = port

    @property
    def onRead(self):
        return self.__on_read

    @onRead.setter
    def onRead(self, callback):
        self.__on_read = callback