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

from PyQt4.QtNetwork import QTcpSocket, QTcpServer


class TcpError(object):
    '''
    TCP/IP error description class.
    '''
    
    SocketError = dict()  # key(int) - error code, value(str) - error description
    SocketError[255] = "Socket was not found"  # add new socket errors here

    def __init__(self, code=None, description=None):
        '''
        :param code: (int), error code
        :param description: (str), error description
        :return: None
        '''

        if code in TcpError.SocketError.keys():
            self.code = code
            self.description = TcpError.SocketError[self.code]

        else:
            self.code = code
            self.description = description


class TcpClient(QTcpSocket):
    '''
    TCP/IP client class.

    Usage:
        1: initialization:
            self.tcpClient = TcpClient()
            self.tcpClient.onConnected = onConnected
            self.tcpClient.onDisconnected = onDisconnected
            self.tcpClient.onError = onError
            self.tcpClient.onRead = onRead

            self.tcpClient.connectToHost(host(str), port(int))

        2: onConnected() callback:
            Connection to the server has been established stuff.

        3: onDisconnected() callback:
            Connection to the server has been closed stuff.

        4: onError(error(TcpError)) callback:
            Check error.code and error.description to figure out what happened.

        5: onRead(data(QByteArray)) callback:
            Process incoming data.

        6: write data:
            self.tcpClient.write(data(QByteArray)) -> int
                Writes data and returns the number of bytes that were actually written, or -1 if an error occurred.

        7: check connection state:
            ???
    '''

    def __init__(self):
        QTcpSocket.__init__(self)

        # Callbacks
        self.__on_connected = None
        self.__on_disconnected = None
        self.__on_error = None
        self.__on_read = None

        # Signals and slots connections
        self.connected.connect(self.__onConnected)
        self.disconnected.connect(self.__onDisconnected)
        self.error.connect(self.__onError)
        self.readyRead.connect(self.__onReadyRead)

    # Slots
    def __onConnected(self):
        '''
        The slot is called when connection to the specified host has been successfully established.
        :return: None
        '''
    
        if self.__on_connected:
            self.__on_connected()

    def __onDisconnected(self):
        '''
        The slot is called when the connection to the host is closed.
        :return: None
        '''
        
        if self.__on_disconnected:
            self.__on_disconnected()

    def __onError(self, error):
        '''
        The slot is called when an error occurs. The error code and description are defined and passed to __on_error
        callback.
        :param error: (PyQt4.QtNetwork.SocketError) error code
        :return: None
        '''
        
        if self.__on_error:
            tcpError = TcpError()
            tcpError.code = error
            tcpError.description = self.errorString().toLocal8Bit().data()
            self.__on_error(tcpError)

    def __onReadyRead(self):
        '''
        The slot is called every time new data is available for reading.
        :return: None
        '''

        if self.__on_read:
            self.__on_read(self.readAll())

    # Setters
    def __connected(self, callback):
        self.__on_connected = callback

    def __disconnected(self, callback):
        self.__on_disconnected = callback

    def __error(self, callback):
        self.__on_error = callback

    def __read(self, callback):
        self.__on_read = callback

    # Properties
    onConnected = property(fset=__connected)
    onDisconnected = property(fset=__disconnected)
    onError = property(fset=__error)
    onRead = property(fset=__read)


class TcpServer(QTcpServer):
    '''
    TCP/IP server class.

    Usage:
        1: Create and initialization a new instance:
            self.tcpServer = TcpServer()
            self.tcpServer.onConnected = self.onConnected
            self.tcpServer.onDisconnected = self.onDisconnected
            self.tcpServer.onError = self.onError
            self.tcpServer.onRead = self.onRead

        2: onConnected(descriptor(int)) callback:
            A client has successfully established a connection tho the server stuff.

        3: onDisconnected(descriptor(int)) callback:
            A client closed the connection tho the server stuff.

        4: onError(descriptor(int), error(TcpError)) callback:
            Check descriptor, error.code and error.description to figure out what happened.

        5: onRead(descriptor(int), data(QByteArray)) callback:
            Process incoming data from the socket with the given descriptor.

        6: start the server:
           self.tcpServer.listen(address(QHostAddress), port(int))

        7: write data:
            self.tcpClient.write(descriptor(int), data(QByteArray)) -> int
                Writes data to the socket with the given descriptor and returns the number of bytes that were actually written, or -1 if an error occurred.

        8: close the server:
            self.tcpServer.close()
    '''

    def __init__(self, parent=None):
        QTcpServer.__init__(self, parent)

        self.__clients = dict()  # All active clients

        # Callbacks
        self.__on_connected = None
        self.__on_disconnected = None
        self.__on_error = None
        self.__on_read = None

        # Signals and slots connections
        self.newConnection.connect(self.__onNewConnection)

    # Slots
    def __onNewConnection(self):
        '''
        The slot is called every time a new connection to a client is available. The client's socket and its descriptor
        are defined, and then the descriptor is passed to __onConnected callback.
        :return: None
        '''

        socket = self.nextPendingConnection()
        socket.disconnected.connect(self.__onDisconnected)
        socket.error.connect(self.__onError)
        socket.readyRead.connect(self.__onReadyRead)
        descriptor = socket.socketDescriptor()
        self.__clients[descriptor] = socket
        self.__onConnected(descriptor)

    def __onConnected(self, descriptor):
        '''
        The slot is called when a new connection to a client with the given descriptor has been successfully
        established.
        :param descriptor: (int), client's descriptor
        :return: None
        '''

        if self.__on_connected:
            self.__on_connected(descriptor)

    def __onDisconnected(self):
        '''
        The slot is called when the connection to a client is closed. The client's socket and its descriptor are
        defined, and then the descriptor is passed to __on_disconnected callback.
        :return: None
        '''
        if self.__on_disconnected:
            socket = self.sender()
            descriptor = socket.socketDescriptor()
            del self.__clients[descriptor]
            self.__on_disconnected(descriptor)

    def __onError(self, error):
        '''
        The slot is called when an error occurs. The socket's descriptor as long as error code and its description are
        defined and passed to __on_error callback.
        :param error:
        :return: None
        '''

        if self.__on_error:
            socket = self.sender()
            descriptor = socket.socketDescriptor()

            tcpError = TcpError()
            tcpError.code = error
            tcpError.description = socket.errorString().toLocal8Bit().data()

            self.__on_error(descriptor, tcpError)

    def __onReadyRead(self):
        '''
        The slot is called every time new data is available for reading. The socket's descriptor and new data are passed
        to __on_read callback.
        :return: None
        '''
        if self.__on_read:
            socket = self.sender()
            descriptor = socket.socketDescriptor()
            data = socket.readAll()
            self.__on_read(descriptor, data)

    # Setters
    def __connected(self, callback):
        self.__on_connected = callback

    def __disconnected(self, callback):
        self.__on_disconnected = callback

    def __error(self, callback):
        self.__on_error = callback

    def __read(self, callback):
        self.__on_read = callback

    # Methods
    def socket(self, descriptor):
        '''
        Return socket with the given descriptor or None if it is not found.
        :param descriptor: (int), socket descriptor
        :return: socket (QTcpSocket) or None
        '''

        return self.__clients.get(descriptor, None)

    def descriptors(self):
        '''
        Return all sockets' descriptors available.
        :return list of int:
        '''

        return sorted(self.__clients.keys())

    def write(self, descriptor, data):
        '''
        Write data to the client's socket with the given descriptor.
        :param descriptor: (int), client's socket descriptor
        :param data: (QByteArray), data to be written
        :return: (int), the number of bytes that were actually written, or -1 if an error occurred
        '''

        socket = self.socket(descriptor)
        if socket:
            return socket.write(data)
        else:
            tcpError = TcpError(255)  # "Socket was not found" error
            self.__on_error(descriptor, tcpError)
            return -1

    def disconnect(self, descriptor):
        '''
        Disconnect the client socket with the given descriptor.
        :param descriptor: (int), client's socket descriptor
        :return: None
        '''

        socket = self.socket(descriptor)
        if socket:
            socket.close()
        else:
            tcpError = TcpError(255)  # "Socket was not found" error
            self.__on_error(descriptor, tcpError)

    def close(self):
        '''
        Close the server.
        :return: None
        '''
        for socket in self.__clients.values():
            socket.close()

        super(TcpServer, self).close()

    # Properties
    onConnected = property(fset=__connected)
    onDisconnected = property(fset=__disconnected)
    onError = property(fset=__error)
    onRead = property(fset=__read)