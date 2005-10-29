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

def main (args):
    import gettext
    import locale
    import sys

    import gtk
    import gtk.glade

    import maindialog
    import lockdownappliergconf
    import config

    try:
        locale.setlocale (locale.LC_ALL, "")
    except locale.Error:
        print >> sys.stderr, "Warning: unsupported locale"
    gettext.install (config.PACKAGE, config.LOCALEDIR)
    gtk.glade.bindtextdomain (config.PACKAGE, config.LOCALEDIR)

    gtk.window_set_default_icon_name ("stock_lock")

    applier = lockdownappliergconf.PessulusLockdownApplierGconf ()

    dialog = maindialog.PessulusMainDialog (applier)

    gtk.main ()

if __name__ == "__main__":
    main (None)
