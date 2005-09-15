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

import os.path
import gobject
import gtk
import gtk.glade
import gconf

from config import *

import disabledapplets
import gconfutils
import gconfcheckbutton
import safeprotocols

gconfdirs = [
"/desktop/gnome/lockdown",
"/apps/epiphany/lockdown",
"/apps/panel/global"
]

checkbuttons = {
    "/desktop/gnome/lockdown/disable_command_line": "checkbuttonDisableCommandLine",
    "/desktop/gnome/lockdown/disable_printing": "checkbuttonDisablePrinting",
    "/desktop/gnome/lockdown/disable_print_setup": "checkbuttonDisablePrintSetup",
    "/desktop/gnome/lockdown/disable_save_to_disk": "checkbuttonDisableSaveToDisk",

    "/apps/panel/global/locked_down": "checkbuttonPanelLockedDown",
    "/apps/panel/global/disable_force_quit": "checkbuttonDisableForceQuit",
    "/apps/panel/global/disable_lock_screen": "checkbuttonDisableLockScreen",
    "/apps/panel/global/disable_log_out": "checkbuttonDisableLogOut",

    "/apps/epiphany/lockdown/disable_arbitrary_url": "checkbuttonDisableArbitraryURL",
    "/apps/epiphany/lockdown/disable_bookmark_editing": "checkbuttonDisableBookmarkEditing",
    "/apps/epiphany/lockdown/disable_history": "checkbuttonDisableHistory",
    "/apps/epiphany/lockdown/disable_javascript_chrome": "checkbuttonDisableJavascriptChrome",
    "/apps/epiphany/lockdown/disable_toolbar_editing": "checkbuttonDisableToolbarEditing",
    "/apps/epiphany/lockdown/fullscreen": "checkbuttonFullscreen",
    "/apps/epiphany/lockdown/hide_menubar": "checkbuttonHideMenubar",
    "/apps/epiphany/lockdown/disable_unsafe_protocols": "checkbuttonDisableUnsafeProtocols"
}

class PessulusMainDialog:
    def __init__ (self):
        self.glade_file = os.path.join (GLADEDIR, "pessulus.glade")
        self.xml = gtk.glade.XML (self.glade_file, "dialogEditor", PACKAGE)

        self.gconfcheckbuttons = []
        for key, name in checkbuttons.iteritems ():
            self.gconfcheckbuttons.append (
                gconfcheckbutton.PessulusGconfCheckbutton (
                    self.xml.get_widget (name), key))

        treeview = self.xml.get_widget ("treeviewDisabledApplets")
        self.disabledapplets = disabledapplets.PessulusDisabledApplets (treeview)

        self.__init_safeprotocols ()

        can_edit_mandatory = self.__init_mandatory ()
        self.client = None
        self.__change_client (gconfutils.get_client (can_edit_mandatory))

        self.xml.get_widget ("helpbutton").set_sensitive (False)

        self.window = self.xml.get_widget ("dialogEditor")
        self.window.connect ("response", self.__on_dialog_response)
        self.window.connect ("destroy", self.__on_dialog_destroy)
        self.window.show ()

    def __init_safeprotocols (self):
        checkbutton = self.xml.get_widget ("checkbuttonDisableUnsafeProtocols")
        hbox = self.xml.get_widget ("hboxSafeProtocols")

        treeview = self.xml.get_widget ("treeviewSafeProtocols")
        addbutton = self.xml.get_widget ("buttonSafeProtocolAdd")
        editbutton = self.xml.get_widget ("buttonSafeProtocolEdit")
        removebutton = self.xml.get_widget ("buttonSafeProtocolRemove")

        self.safeprotocols = safeprotocols.PessulusSafeProtocols (treeview,
                                                                  addbutton,
                                                                  editbutton,
                                                                  removebutton)

        checkbutton.connect ("toggled", self.__on_unsafeprotocols_toggled, hbox)
        self.__on_unsafeprotocols_toggled (checkbutton, hbox)

    def __init_mandatory (self):
        can_edit_mandatory = gconfutils.can_edit_mandatory ()
        if can_edit_mandatory:
            administrator = self.xml.get_widget ("hboxSystemAdministrator")
            administrator.hide ()

        mandatory = self.xml.get_widget ("checkbuttonUseMandatorySettings")
        mandatory.set_sensitive (can_edit_mandatory)
        mandatory.set_active (can_edit_mandatory)
        mandatory.connect ("toggled", self.__on_mandatory_toggled)

        return can_edit_mandatory

    def __on_dialog_response (self, dialog, response_id):
        if dialog == self.window and response_id == gtk.RESPONSE_HELP:
            return
        
        dialog.hide ()
        dialog.destroy ()

    def __on_dialog_destroy (self, dialog):
        self.__change_client (None)
        gtk.main_quit ()

    def __on_unsafeprotocols_toggled (self, checkbutton, hbox):
        sensitive = checkbutton.get_active ()
        hbox.set_sensitive (sensitive)
        self.safeprotocols.set_sensitive (sensitive)

    def __on_mandatory_toggled (self, checkbutton):
        try:
            client = gconfutils.get_client (checkbutton.get_active ())
        except gobject.GError:
            if checkbutton.get_active ():
                primary_text = _("Can not configure the mandatory settings")
                secondary_text = _("You might not have the rights to configure the mandatory settings.")
            else:
                primary_text = _("Can not configure the regular settings")
                secondary_text = _("As this should never happen, we advise you to close the lockdown editor and start again.")

            dialog = gtk.MessageDialog (self.window,
                                        gtk.DIALOG_MODAL|gtk.DIALOG_DESTROY_WITH_PARENT,
                                        gtk.MESSAGE_ERROR,
                                        gtk.BUTTONS_OK,
                                        primary_text)
            dialog.set_title ("")
            dialog.format_secondary_text (secondary_text)
            dialog.connect ("response", self.__on_dialog_response)
            dialog.run ()
            return
        
        self.__change_client (client)

    def __change_client (self, newclient):
        if self.client:
            for gconfdir in gconfdirs:
                self.client.remove_dir (gconfdir)

        self.client = newclient

        if self.client:
            for gconfdir in gconfdirs:
                self.client.add_dir (gconfdir, gconf.CLIENT_PRELOAD_NONE)

        for gconfcheckbutton in self.gconfcheckbuttons:
            gconfcheckbutton.change_client (self.client)

        self.disabledapplets.change_client (self.client)
        self.safeprotocols.change_client (self.client)
