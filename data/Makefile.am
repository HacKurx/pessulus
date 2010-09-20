uidir = $(pkgdatadir)/ui
ui_DATA = pessulus.ui

desktopdir = $(datadir)/applications
desktop_in_files = pessulus.desktop.in
desktop_DATA = $(desktop_in_files:.desktop.in=.desktop)

@INTLTOOL_DESKTOP_RULE@

gtk_update_icon_cache = gtk-update-icon-cache -f -t $(datadir)/icons/hicolor

install-data-local: install-icons
uninstall-local: uninstall-icons

install-data-hook: update-icon-cache
uninstall-hook: update-icon-cache

install-icons:			
	for size in 16x16 22x22 24x24 32x32 48x48 scalable; do mkdir --parents $(DESTDIR)/$(datadir)/icons/hicolor/$$size/apps; done

	$(INSTALL_DATA) $(srcdir)/pessulus-16.png $(DESTDIR)/$(datadir)/icons/hicolor/16x16/apps/pessulus.png
	$(INSTALL_DATA) $(srcdir)/pessulus-22.png $(DESTDIR)/$(datadir)/icons/hicolor/22x22/apps/pessulus.png
	$(INSTALL_DATA) $(srcdir)/pessulus-24.png $(DESTDIR)/$(datadir)/icons/hicolor/24x24/apps/pessulus.png
	$(INSTALL_DATA) $(srcdir)/pessulus-32.png $(DESTDIR)/$(datadir)/icons/hicolor/32x32/apps/pessulus.png
	$(INSTALL_DATA) $(srcdir)/pessulus-48.png $(DESTDIR)/$(datadir)/icons/hicolor/48x48/apps/pessulus.png
	$(INSTALL_DATA) $(srcdir)/pessulus.svg $(DESTDIR)/$(datadir)/icons/hicolor/scalable/apps/pessulus.svg

uninstall-icons:
	rm -f $(DESTDIR)/$(datadir)/icons/hicolor/16x16/apps/pessulus.png
	rm -f $(DESTDIR)/$(datadir)/icons/hicolor/22x22/apps/pessulus.png
	rm -f $(DESTDIR)/$(datadir)/icons/hicolor/24x24/apps/pessulus.png
	rm -f $(DESTDIR)/$(datadir)/icons/hicolor/32x32/apps/pessulus.png
	rm -f $(DESTDIR)/$(datadir)/icons/hicolor/48x48/apps/pessulus.png
	rm -f $(DESTDIR)/$(datadir)/icons/hicolor/scalable/apps/pessulus.svg

update-icon-cache:
	@-if test -z "$(DESTDIR)"; then \
		echo "Updating Gtk icon cache."; \
		$(gtk_update_icon_cache); \
	else \
		echo "*** Icon cache not updated. After (un)install, run this:"; \
		echo "***   $(gtk_update_icon_cache)"; \
	fi

EXTRA_DIST =				\
	$(desktop_in_files)		\
	$(ui_DATA)			\
	pessulus-16.png pessulus-22.png \
	pessulus-24.png pessulus-32.png \
	pessulus-48.png pessulus.svg

CLEANFILES =			\
	$(desktop_DATA)

-include $(top_srcdir)/git.mk
