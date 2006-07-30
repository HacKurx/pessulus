NULL =

SUBDIRS = data po Pessulus

bin_SCRIPTS = pessulus

pessulus: pessulus.in Makefile
	sed -e s!\@pyexecdir\@!@pyexecdir@! -e s!\@PYTHON\@!@PYTHON@! < $< > $@
	chmod a+x $@

EXTRA_DIST =			\
	HACKING			\
	MAINTAINERS		\
	pessulus.in		\
	intltool-extract.in	\
	intltool-merge.in	\
	intltool-update.in	\
	$(NULL)

CLEANFILES =		\
	pessulus

DISTCLEANFILES =		\
        intltool-extract	\
        intltool-merge		\
        intltool-update		\
	$(NULL)
