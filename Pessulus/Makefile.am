appdir = $(pyexecdir)/Pessulus

app_PYTHON = 			\
	__init__.py		\
	disabledapplets.py	\
	gconfcheckbutton.py	\
	gconfutils.py		\
	icons.py		\
	main.py			\
	maindialog.py		\
	safeprotocols.py	\
	simpleeditabletreeview.py

nodist_app_PYTHON = config.py

CLEANFILES = config.py
EXTRA_DIST = config.py.in

all-local: config.py

config.py: config.py.in Makefile
	sed								\
		-e s!\@LOCALEDIR\@!$(datadir)/locale!			\
		-e s!\@DATADIR\@!$(datadir)!				\
		-e s!\@GLADEDIR\@!$(pkgdatadir)/glade!			\
		-e s!\@GCONF_MANDATORY_SOURCE\@!@GCONF_MANDATORY_SOURCE@!	\
		-e s!\@PACKAGE_NAME\@!$(PACKAGE_NAME)!			\
		-e s!\@PACKAGE_VERSION\@!$(PACKAGE_VERSION)!		\
		< $< > $@
