AC_PREREQ(2.53)
AC_INIT([pessulus], [2.30.5],
        [http://bugzilla.gnome.org/enter_bug.cgi?product=pessulus])
AC_CONFIG_SRCDIR(pessulus.in)
AM_INIT_AUTOMAKE([1.9 foreign no-dist-gzip dist-bzip2])
m4_ifdef([AM_SILENT_RULES], [AM_SILENT_RULES([yes])])
AC_CONFIG_MACRO_DIR([m4])

AM_MAINTAINER_MODE

PKG_CHECK_MODULES([PESSULUS], [pygtk-2.0 >= 2.13.0])

GETTEXT_PACKAGE=pessulus
AC_SUBST(GETTEXT_PACKAGE)
AC_DEFINE_UNQUOTED(GETTEXT_PACKAGE, "$GETTEXT_PACKAGE", [Gettext package])
AM_GLIB_GNU_GETTEXT
IT_PROG_INTLTOOL([0.40.0])
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

dnl ---------------------------------------------------------------------------
dnl - Show summary
dnl ---------------------------------------------------------------------------

echo "
              pessulus $VERSION
              `echo pessulus $VERSION | sed "s/./=/g"`

        prefix:                             ${prefix}
        exec_prefix:                        ${exec_prefix}
        libdir:                             ${libdir}
        bindir:                             ${bindir}
        sbindir:                            ${sbindir}
        sysconfdir:                         ${sysconfdir}
        localstatedir:                      ${localstatedir}
        datadir:                            ${datadir}
        source code location:               ${srcdir}
        Maintainer mode:                    ${USE_MAINTAINER_MODE}

        GConf source for mandatory values:  ${GCONF_MANDATORY_SOURCE}

Those python modules are optional runtime dependencies:
 bugbuddy (from gnome-python-desktop)
"
