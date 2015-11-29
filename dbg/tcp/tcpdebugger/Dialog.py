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

from PyQt4.QtCore import Qt
from PyQt4.QtGui import QDialog

from dbg.tcp.client.Dialog import Dialog as RTcpClient
from dbg.tcp.server.Dialog import Dialog as RTcpServer
from dbg.tcp.tcpdebugger.ui_Dialog import Ui_Dialog


class TcpDebugger(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent, Qt.SplashScreen)

        self.setupUi(self)

        self.pushButtonClient.clicked.connect(self.pushButtonClientClicked)
        self.pushButtonServer.clicked.connect(self.pushButtonServerClicked)

    def pushButtonClientClicked(self):
        self.dialog = RTcpClient()
        self.dialog.show()
        self.hide()

    def pushButtonServerClicked(self):
        self.dialog = RTcpServer()
        self.dialog.show()
        self.hide()