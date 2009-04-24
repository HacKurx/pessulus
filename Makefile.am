NULL =

SUBDIRS = data po Pessulus

bin_SCRIPTS = pessulus

pessulus: pessulus.in Makefile
	sed -e s!\@pythondir\@!@pythondir@! -e s!\@PYTHON\@!@PYTHON@! < $< > $@
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

MAINTAINERCLEANFILES = \
	$(srcdir)/INSTALL \
	$(srcdir)/aclocal.m4 \
	$(srcdir)/config.guess \
	$(srcdir)/config.sub \
	$(srcdir)/install-sh \
	$(srcdir)/missing \
	$(srcdir)/mkinstalldirs \
	$(srcdir)/py-compile \
	`find "$(srcdir)" -type f -name Makefile.in -print` \
	intltool-extract.in \
	intltool-merge.in \
	intltool-update.in \
	`find "$(srcdir)" -type f -name .gitignore -print`

-include $(top_srcdir)/git.mk
