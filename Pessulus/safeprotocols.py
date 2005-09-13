#!/usr/bin/env python

# vim: set ts=4 sw=4 et:

#
# Copyright (C) 2005 Vincent Untz <vuntz@gnome.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301, USA
#

import gconf
import gtk

class PessulusSafeProtocols:
    (
        COLUMN_PROTOCOL,
    ) = range (1)

    def __init__ (self, treeview):
        self.notify_id = None
        self.client = None
        self.key = "/apps/epiphany/lockdown/additional_safe_protocols"
        self.safe_protocols = None

        self.liststore = gtk.ListStore (str)

        self.treeview = treeview
        self.treeview.get_selection ().set_mode (gtk.SELECTION_SINGLE)
        self.treeview.set_model (self.liststore)

        self.__create_columns ()

    def change_client (self, client):
        if self.notify_id:
            if self.client:
                self.client.notify_remove (self.notify_id)

        if not client:
            return

        self.client = client
        self.notify_id = self.client.notify_add (self.key, self.__on_notified)

        self.safe_protocols = set (self.client.get_list (self.key, gconf.VALUE_STRING))
        self.__update_model ()

    def add_protocol (self, protocol):
        if protocol in self.safe_protocols:
            return

        self.safe_protocols.add (protocol)
        self.client.set_list (self.key, gconf.VALUE_STRING, list (self.safe_protocols))

    def remove_selected (self):
        (model, iter) = self.treeview.get_selection ().get_selected ()
        if not iter or model[iter][self.COLUMN_PROTOCOL] not in self.safe_protocols:
            return
        
        self.safe_protocols.remove (model[iter][self.COLUMN_PROTOCOL])
        self.client.set_list (self.key, gconf.VALUE_STRING, list (self.safe_protocols))

    def __create_columns (self):
        column = gtk.TreeViewColumn ()
        self.treeview.append_column (column)

        cell = gtk.CellRendererText ()
        column.pack_start (cell, True)
        column.set_attributes (cell, text = self.COLUMN_PROTOCOL)

    def __on_notified (self, client, cnxn_id, entry, data):
        if entry.value and entry.value.type == gconf.VALUE_LIST:
            if entry.value.get_list () != self.safe_protocols:
                self.safe_protocols.clear ()
                for value in entry.value.get_list ():
                    if value.type == gconf.VALUE_STRING:
                        self.safe_protocols.add (value.get_string ())
                self.__update_model ()

    def __update_model (self):
        self.liststore.clear ()
        for protocol in self.safe_protocols:
            iter = self.liststore.append ()
            self.liststore.set (iter, self.COLUMN_PROTOCOL, protocol)
