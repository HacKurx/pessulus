AC_PREREQ(2.53)
AC_INIT([pessulus], [0.8],
        [http://bugzilla.gnome.org/enter_bug.cgi?product=pessulus])
AC_CONFIG_SRCDIR(pessulus.in)
AM_INIT_AUTOMAKE([1.7])
AM_MAINTAINER_MODE

dnl make sure we keep ACLOCAL_FLAGS around for maintainer builds to work
AC_SUBST(ACLOCAL_AMFLAGS, "$ACLOCAL_FLAGS")

PKG_CHECK_MODULES(PESSULUS,
		  pygtk-2.0 >= 2.6.0		\
		  gnome-python-2.0 >= 2.6.0)

ALL_LINGUAS="bg ca cs de el en_CA es et fi fr gl gu hu lt mk nb nl pt_BR ja ko pa sk sq sr sr@Latn sv th vi zh_CN zh_HK zh_TW"
GETTEXT_PACKAGE=pessulus
AC_SUBST(GETTEXT_PACKAGE)
AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE, "$GETTEXT_PACKAGE", [Gettext package])
AM_GLIB_GNU_GETTEXT
AC_PROG_INTLTOOL
AM_PATH_PYTHON
AC_PATH_PROG(GCONFTOOL, gconftool-2)

dnl Get the GConf defaults source, and sed it to make the mandatory source.
GCONF_DEFAULTS_SOURCE=`gconftool-2 --get-default-source`
GCONF_MANDATORY_SOURCE=`echo $GCONF_DEFAULTS_SOURCE | sed -e s/gconf.xml.defaults/gconf.xml.mandatory/`
AC_ARG_WITH(gconf-mandatory-source,
  AC_HELP_STRING([--with-gconf-mandatory-source],
                 [The GConf source of the mandatory values]),
  GCONF_MANDATORY_SOURCE="$withval",)
AC_DEFINE_UNQUOTED(GCONF_MANDATORY_SOURCE, "$GCONF_MANDATORY_SOURCE", [GConf mandatory source])
AC_MSG_RESULT([Using config source $GCONF_MANDATORY_SOURCE for mandatory values])
AC_SUBST(GCONF_MANDATORY_SOURCE)

AC_CONFIG_FILES([
Makefile
data/Makefile
po/Makefile.in
Pessulus/Makefile
])

AC_OUTPUT([
data/pessulus.desktop.in
])
