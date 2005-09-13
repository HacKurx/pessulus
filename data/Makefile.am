gladedir   = $(pkgdatadir)/glade
glade_DATA = pessulus.glade

desktopdir = $(datadir)/applications
desktop_in_files = pessulus.desktop.in 
desktop_DATA = $(desktop_in_files:.desktop.in=.desktop)

@INTLTOOL_DESKTOP_RULE@

EXTRA_DIST =			\
	$(desktop_in_files)	\
	$(glade_DATA)

CLEANFILES =			\
	$(desktop_DATA)
