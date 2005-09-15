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

import gobject
import gtk
import gconf
import sys

class PessulusGconfCheckbutton:
    def __init__ (self, checkbutton, key):
        self.notify_id = None
        self.client = None
        self.key = key
        self.checkbutton = checkbutton

        self.tooltips = gtk.Tooltips ()

        checkbutton.connect ("toggled", self.__on_toggled)
        checkbutton.connect ("destroy", self.__on_destroyed)

    def set_tooltip (self):
        if not self.client:
            return

        try:
            schema = self.client.get_schema ("/schemas" + self.key)
            if schema:
                self.tooltips.set_tip (self.checkbutton, schema.get_long_desc ())
        except gobject.GError:
            print >> sys.stderr, "Warning: Could not get schema for %s" % self.key

    def change_client (self, client):
        if self.notify_id:
            if self.client:
                self.client.notify_remove (self.notify_id)

        oldclient = self.client
        self.client = client
        if not self.client:
            return

        self.notify_id = self.client.notify_add (self.key, self.__on_notified)
        self.__update_toggle ()

        if oldclient == None:
            self.set_tooltip ()

    def __update_toggle (self):
        self.checkbutton.set_active (self.client.get_bool (self.key))
        self.checkbutton.set_sensitive (self.client.key_is_writable (self.key))

    def __on_notified (self, client, cnxn_id, entry, data):
        if entry.value and entry.value.type == gconf.VALUE_BOOL:
            if entry.value.get_bool () != self.checkbutton.get_active ():
                self.__update_toggle ()

    def __on_toggled (self, checkbutton):
        if self.client and self.client.key_is_writable (self.key):
            self.client.set_bool (self.key, self.checkbutton.get_active ())

    def __on_destroyed (self, checkbutton):
        if self.notify_id:
            if self.client:
                self.client.notify_remove (self.notify_id)
            self.notify_id = None

        if self.client:
            self.client = None
