SUBDIRS = Pessulus data po

ACLOCAL_AMFLAGS = -I m4 ${ACLOCAL_FLAGS}

bin_SCRIPTS = pessulus

pessulus: pessulus.in Makefile
	$(AM_V_GEN)sed -e s!\@pythondir\@!@pythondir@! -e s!\@PYTHON\@!@PYTHON@! < $< > $@
	$(AM_V_at)chmod a+x $@

EXTRA_DIST =			\
	HACKING			\
	MAINTAINERS		\
	pessulus.in

CLEANFILES =		\
	pessulus

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
	$(srcdir)/configure

-include $(top_srcdir)/git.mk
