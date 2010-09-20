appdir = $(pythondir)/Pessulus

app_PYTHON = 			\
	__init__.py		\
	disabledapplets.py	\
	icons.py		\
	globalvar.py		\
	lockdownappliergconf.py	\
	lockdownapplier.py	\
	lockdownbutton.py	\
	lockdowncheckbutton.py	\
	main.py			\
	maindialog.py		\
	safeprotocols.py	\
	simpleeditabletreeview.py

nodist_app_PYTHON = config.py

config.py: config.py.in Makefile
	$(AM_V_GEN)sed								\
		-e s!\@LOCALEDIR\@!$(datadir)/locale!			\
		-e s!\@DATADIR\@!$(datadir)!				\
		-e s!\@BUILDERDIR\@!$(pkgdatadir)/ui!			\
		-e s!\@GCONF_MANDATORY_SOURCE\@!@GCONF_MANDATORY_SOURCE@!	\
		-e s!\@PACKAGE_NAME\@!$(PACKAGE_NAME)!			\
		-e s!\@PACKAGE_VERSION\@!$(PACKAGE_VERSION)!		\
		< $< > $@

EXTRA_DIST = config.py.in

CLEANFILES = config.py

-include $(top_srcdir)/git.mk
