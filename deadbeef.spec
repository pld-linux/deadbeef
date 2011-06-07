Summary:	Ultimate Music Player
Name:		deadbeef
Version:	0.5.1
Release:	1
License:	GPL v2 and LGPL v2.1
Group:		X11/Applications/Multimedia
Source0:	http://downloads.sourceforge.net/deadbeef/%{name}-%{version}.tar.bz2
# Source0-md5:	be8359d1bd9cf7679cf2ca748996e726
Patch0:		lm-missing-symbols.patch
URL:		http://deadbeef.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	automake >= 1.11
BuildRequires:	curl-devel
BuildRequires:	dbus-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2.12
BuildRequires:	imlib2-devel
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcddb-devel
BuildRequires:	libcdio-devel
BuildRequires:	libmad-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pakchois-devel
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel
BuildRequires:	wavpack-devel
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DeaDBeeF (as in 0xDEADBEEF) is an audio player for GNU/Linux systems
with X11 (though now it also runs in plain console without X, in
FreeBSD, and in OpenSolaris).

%package plugin-aac
Summary:	AAC plugin
Group:		X11/Applications/Multimedia

%description plugin-aac
AAC player.

%package plugin-alsa
Summary:	ALSA plugin
Group:		X11/Applications/Multimedia

%description plugin-alsa
ALSA output plugin.

%package plugin-artwork
Summary:	Artwork plugin
Group:		X11/Applications/Multimedia

%description plugin-artwork
Album artwork.

%package plugin-cdda
Summary:	CD Audio plugin
Group:		X11/Applications/Multimedia

%description plugin-cdda
Audio CD player.

%package plugin-ffmpeg
Summary:	FFMPEG plugin
Group:		X11/Applications/Multimedia

%description plugin-ffmpeg
FFMPEG audio player.

%package plugin-flac
Summary:	FLAC plugin
Group:		X11/Applications/Multimedia

%description plugin-flac
FLAC decoder.

%package plugin-gtkui
Summary:	GTKui plugin
Group:		X11/Applications/Multimedia

%description plugin-gtkui
Standard GTK2 user interface.

%package plugin-hotkeys
Summary:	Hotkeys plugin
Group:		X11/Applications/Multimedia

%description plugin-hotkeys
Global hotkeys support.

%package plugin-lastfm
Summary:	last.fm plugin
Group:		X11/Applications/Multimedia

%description plugin-lastfm
last.fm scrobbler.

%package plugin-mad
Summary:	Mad plugin
Group:		X11/Applications/Multimedia

%description plugin-mad
MPEG decoder.

%package plugin-notify
Summary:	Notify plugin
Group:		X11/Applications/Multimedia

%description plugin-notify
OSD notify.

%package plugin-oss
Summary:	OSS plugin
Group:		X11/Applications/Multimedia

%description plugin-oss
OSS output plugin.

%package plugin-pulse
Summary:	PulseAudio plugin
Group:		X11/Applications/Multimedia

%description plugin-pulse
PulseAudio output plugin.

%package plugin-resampler
Summary:	Resampler plugin
Group:		X11/Applications/Multimedia

%description plugin-resampler
Resampler (Secret Rabit Code).

%package plugin-sndfile
Summary:	WAV/PCM plugin
Group:		X11/Applications/Multimedia

%description plugin-sndfile
WAV/PCM/aiff player.

%package plugin-vorbis
Summary:	OggVorbis plugin
Group:		X11/Applications/Multimedia

%description plugin-vorbis
OggVorbis decoder.

%package plugin-wavpack
Summary:	WavPack plugin
Group:		X11/Applications/Multimedia

%description plugin-wavpack
WavPack decoder.

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

#remove *.la *.a libraries and *.h files
%{__rm} $RPM_BUILD_ROOT%{_libdir}/deadbeef/*.{a,la}
%{__rm} $RPM_BUILD_ROOT%{_includedir}/deadbeef/*.h

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README about.txt help.txt
%attr(755,root,root) %{_bindir}/deadbeef
%{_desktopdir}/deadbeef.desktop
%{_iconsdir}/hicolor/*/apps/deadbeef.png
%{_iconsdir}/hicolor/*/apps/deadbeef.svg
%{_datadir}/deadbeef
%dir %{_libdir}/deadbeef
%attr(755,root,root)%{_libdir}/deadbeef/adplug.so*
%attr(755,root,root)%{_libdir}/deadbeef/converter.so*
%attr(755,root,root)%{_libdir}/deadbeef/dca.so*
%attr(755,root,root)%{_libdir}/deadbeef/ffap.so*
%attr(755,root,root)%{_libdir}/deadbeef/gme.so*
%attr(755,root,root)%{_libdir}/deadbeef/m3u.so*
%attr(755,root,root)%{_libdir}/deadbeef/mms.so*
%attr(755,root,root)%{_libdir}/deadbeef/musepack.so*
%attr(755,root,root)%{_libdir}/deadbeef/nullout.so*
%attr(755,root,root)%{_libdir}/deadbeef/shellexec.so*
%attr(755,root,root)%{_libdir}/deadbeef/sid.so*
%attr(755,root,root)%{_libdir}/deadbeef/supereq.so*
%attr(755,root,root)%{_libdir}/deadbeef/tta.so*
%attr(755,root,root)%{_libdir}/deadbeef/vfs_curl.so*
%attr(755,root,root)%{_libdir}/deadbeef/vtx.so*
%attr(755,root,root)%{_libdir}/deadbeef/wildmidi.so*
%{_libdir}/deadbeef/convpresets/*

%files plugin-aac
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/deadbeef/aac.so*

%files plugin-alsa
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/deadbeef/alsa.so*

%files plugin-artwork
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/deadbeef/artwork.so*

%files plugin-cdda
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/deadbeef/cdda.so*

%files plugin-ffmpeg
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/deadbeef/ffmpeg.so*

%files plugin-flac
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/deadbeef/flac.so*

%files plugin-gtkui
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/deadbeef/ddb_gui_GTK2.so*
%attr(755,root,root)%{_libdir}/deadbeef/converter_gtkui.so*

%files plugin-hotkeys
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/deadbeef/hotkeys.so*

%files plugin-lastfm
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/deadbeef/lastfm.so*

%files plugin-mad
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/deadbeef/mpgmad.so*

%files plugin-notify
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/deadbeef/notify.so*

%files plugin-oss
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/deadbeef/oss.so*

%files plugin-pulse
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/deadbeef/pulse.so*

%files plugin-resampler
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/deadbeef/dsp_libsrc.so*

%files plugin-sndfile
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/deadbeef/sndfile.so*

%files plugin-vorbis
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/deadbeef/vorbis.so*

%files plugin-wavpack
%defattr(644,root,root,755)
%attr(755,root,root)%{_libdir}/deadbeef/wavpack.so*
