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
import gconf

from config import *

def get_client (mandatory):
    if mandatory:
        engine = gconf.engine_get_for_address (GCONF_MANDATORY_SOURCE)
        return gconf.client_get_for_engine (engine)
    else:
        return gconf.client_get_default ()

def can_edit_mandatory ():
    try:
        engine = gconf.engine_get_for_address (GCONF_MANDATORY_SOURCE)
    except gobject.GError:
        return False

    if engine == None:
        return False

    try:
        #entry = engine.get_entry ("/apps/gconf-editor/can_edit_source",
        #                          None,
        #                          False)
        #gconf_engine_get_entry() is not wrapped. Ugly workaround:
        client = gconf.client_get_for_engine (engine)
        entry = client.get_entry ("/apps/gconf-editor/can_edit_source", "",
                                  False)
    except gobject.GError:
        return False

    if entry != None:
        return entry.get_is_writable ()

    return False
