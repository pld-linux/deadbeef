Summary:	Ultimate Music Player
Name:		deadbeef
Version:	0.5.1
Release:	0.1
License:	GPL v2 and LGPL v2.1
Group:		X11/Applications/Multimedia
Source0:	http://downloads.sourceforge.net/deadbeef/%{name}-%{version}.tar.bz2
# Source0-md5:	be8359d1bd9cf7679cf2ca748996e726
Patch0:		lm-missing-symbols.patch
URL:		http://deadbeef.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	curl-devel
BuildRequires:	dbus-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	gtk+2-devel >= 2.12
BuildRequires:	libcddb-devel
BuildRequires:	libcdio-devel
BuildRequires:	libmad-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	pulseaudio-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define dblibdir %{_libdir}/%{name}

%description
DeaDBeeF (as in 0xDEADBEEF) is an audio player for GNU/Linux systems
with X11 (though now it also runs in plain console without X, in
FreeBSD, and in OpenSolaris).

%package plugin-alsa
Summary:	Alsa plugin
Group:		X11/Applications/Multimedia

%description plugin-alsa
Alsa plugin.

%package plugin-gtkui
Summary:	GTKui plugin
Group:		X11/Applications/Multimedia

%description plugin-gtkui
GTKui plugin.

%package plugin-mad
Summary:	Mad plugin
Group:		X11/Applications/Multimedia

%description plugin-mad
Mad plugin.

%prep
%setup -q
%patch0 -p1

%build
%{__automake}
%configure \
	--enable-gtkui \
	--docdir=%{_docdir}/%{name}-%{version}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

#remove *.la *.a libraries and deadbeef.h
rm -f $RPM_BUILD_ROOT%{_libdir}/deadbeef/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/deadbeef/*.la
rm -f $RPM_BUILD_ROOT%{_includedir}/deadbeef/deadbeef.h

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README about.txt help.txt
%dir %{dblibdir}
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/deadbeef.png
%{_iconsdir}/hicolor/*/apps/deadbeef.svg
%{_datadir}/deadbeef
%dir %{_libdir}/deadbeef
%attr(755,root,root)%{_libdir}/deadbeef/*.so
%attr(755,root,root)%{_libdir}/deadbeef/*.so.0
%attr(755,root,root)%{_libdir}/deadbeef/*.so.0.0.0

%files plugin-alsa
%defattr(644,root,root,755)
%{dblibdir}/alsa.*so*

%files plugin-gtkui
%defattr(644,root,root,755)
%{dblibdir}/gtkui.*so*

%files plugin-mad
%defattr(644,root,root,755)
%{dblibdir}/mpgmad.*so*
