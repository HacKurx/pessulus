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

try:
    set
except:
    from sets import Set as set

import simpleeditabletreeview

class PessulusSafeProtocols:
    def __init__ (self, treeview, addbutton, editbutton, removebutton):
        self.notify_id = None
        self.client = None
        self.key = "/apps/epiphany/lockdown/additional_safe_protocols"
        self.safe_protocols = None
        self.sensitive = True

        self.simpleeditabletreeview = simpleeditabletreeview.PessulusSimpleEditableTreeview (treeview, addbutton, editbutton, removebutton)
        self.simpleeditabletreeview.connect ("changed",
                                             self.__on_treeview_changed)

    def change_client (self, client):
        if self.notify_id:
            if self.client:
                self.client.notify_remove (self.notify_id)

        if not client:
            return

        self.client = client
        self.notify_id = self.client.notify_add (self.key, self.__on_notified)

        self.safe_protocols = set (self.client.get_list (self.key,
                                                         gconf.VALUE_STRING))
        self.__update_simpleeditabletreeview ()

    def set_sensitive (self, sensitive):
        self.sensitive = sensitive
        self.__update_sensitivity ()

    def __on_notified (self, client, cnxn_id, entry, data):
        if entry.value and entry.value.type == gconf.VALUE_LIST:
            gconf_set = set ()
            for value in entry.value.get_list ():
                if value.type == gconf.VALUE_STRING:
                    gconf_set.add (value.get_string ())

            if gconf_set != self.safe_protocols:
                self.safe_protocols = gconf_set
                self.__update_simpleeditabletreeview ()

    def __on_treeview_changed (self, simpleeditabletreeview, new_set):
        if new_set != self.safe_protocols:
            self.safe_protocols = new_set.copy ()
            self.client.set_list (self.key, gconf.VALUE_STRING,
                                  list (self.safe_protocols))

    def __update_sensitivity (self):
        if self.client:
            sensitive = self.sensitive and self.client.key_is_writable (self.key)
        else:
            sensitive = self.sensitive

        self.simpleeditabletreeview.set_sensitive (sensitive)

    def __update_simpleeditabletreeview (self):
        self.__update_sensitivity ()
        self.simpleeditabletreeview.update_set (self.safe_protocols)
