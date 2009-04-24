gladedir   = $(pkgdatadir)/glade
glade_DATA = pessulus.glade

desktopdir = $(datadir)/applications
desktop_in_files = pessulus.desktop.in 
desktop_DATA = $(desktop_in_files:.desktop.in=.desktop)

@INTLTOOL_DESKTOP_RULE@

EXTRA_DIST =			\
	$(desktop_in_files)	\
	$(glade_DATA) \
	pessulus-16.png pessulus-22.png \
	pessulus-24.png pessulus-32.png \
	pessulus-48.png pessulus.svg

DISTCLEANFILES = $(applications_DATA)

gtk_update_icon_cache = gtk-update-icon-cache -f -t $(datadir)/icons/hicolor

install-icons:			
	for size in 16x16 22x22 24x24 32x32 48x48 scalable; do mkdir --parents $(DESTDIR)/$(datadir)/icons/hicolor/$$size/apps; done

	install -m 644 $(srcdir)/pessulus-16.png $(DESTDIR)/$(datadir)/icons/hicolor/16x16/apps/pessulus.png 
	install -m 644 $(srcdir)/pessulus-22.png $(DESTDIR)/$(datadir)/icons/hicolor/22x22/apps/pessulus.png 
	install -m 644 $(srcdir)/pessulus-24.png $(DESTDIR)/$(datadir)/icons/hicolor/24x24/apps/pessulus.png 
	install -m 644 $(srcdir)/pessulus-32.png $(DESTDIR)/$(datadir)/icons/hicolor/32x32/apps/pessulus.png 
	install -m 644 $(srcdir)/pessulus-48.png $(DESTDIR)/$(datadir)/icons/hicolor/48x48/apps/pessulus.png 
	install -m 644 $(srcdir)/pessulus.svg $(DESTDIR)/$(datadir)/icons/hicolor/scalable/apps/pessulus.svg 

install-data-hook:
	@-if test -z "$(DESTDIR)"; then \
	        echo "Updating Gtk icon cache."; \
	        $(gtk_update_icon_cache); \
	else \
	        echo "*** Icon cache not updated.  After install, run this:"; \
	        echo "***   $(gtk_update_icon_cache)"; \
	fi

install-data-local: install-icons

uninstall-icons:
	rm -f $(DESTDIR)/$(datadir)/icons/hicolor/16x16/apps/pessulus.png
	rm -f $(DESTDIR)/$(datadir)/icons/hicolor/22x22/apps/pessulus.png
	rm -f $(DESTDIR)/$(datadir)/icons/hicolor/24x24/apps/pessulus.png
	rm -f $(DESTDIR)/$(datadir)/icons/hicolor/32x32/apps/pessulus.png
	rm -f $(DESTDIR)/$(datadir)/icons/hicolor/48x48/apps/pessulus.png
	rm -f $(DESTDIR)/$(datadir)/icons/hicolor/scalable/apps/pessulus.svg

uninstall-local: uninstall-icons

CLEANFILES =			\
	$(desktop_DATA)

-include $(top_srcdir)/git.mk
