%define	libmediainfo_ver	0.7.44
Summary:	Supplies technical and tag information about a video or audio file (CLI)
Name:		mediainfo
Version:	0.7.44
Release:	1
License:	GPL
Group:		Applications/Multimedia
URL:		http://mediainfo.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/mediainfo/source/mediainfo/%{version}/%{name}_%{version}.tar.bz2
# Source0-md5:	ed89fcc565ac38065bcb48e13efea5c6
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dos2unix
BuildRequires:	libmediainfo-devel >= %{libmediainfo_ver}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	wxGTK2-unicode-devel
BuildRequires:	zlib-devel
Requires:	libmediainfo >= %{libmediainfo_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MediaInfo CLI (Command Line Interface).

What information can I get from MediaInfo?
- General: title, author, director, album, track number, date,
  duration...
- Video: codec, aspect, fps, bitrate...
- Audio: codec, sample rate, channels, language, bitrate...
- Text: language of subtitle
- Chapters: number of chapters, list of chapters

DivX, XviD, H263, H.263, H264, x264, ASP, AVC, iTunes, MPEG-1, MPEG1,
MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V, QuickTime, RealVideo,
RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2, MSMPEG4v3, VOB, DVD, WMA,
VMW, ASF, 3GP, 3GPP, 3GP2

What format (container) does MediaInfo support?
- Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1, MPEG-2,
  MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP, H.264, AVC...)
- Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
- Subtitles: SRT, SSA, ASS, SAMI

%package gui
Summary:	Supplies technical and tag information about a video or audio file (GUI)
Group:		X11/Applications/Multimedia
Requires:	kde-common-dirs >= 0.5
Requires:	libmediainfo >= %{version}
Requires:	libzen >= 0.4.9

%description gui
MediaInfo (Graphical User Interface).

What information can I get from MediaInfo?
- General: title, author, director, album, track number, date,
  duration...
- Video: codec, aspect, fps, bitrate...
- Audio: codec, sample rate, channels, language, bitrate...
- Text: language of subtitle
- Chapters: number of chapters, list of chapters

DivX, XviD, H263, H.263, H264, x264, ASP, AVC, iTunes, MPEG-1, MPEG1,
MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V, QuickTime, RealVideo,
RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2, MSMPEG4v3, VOB, DVD, WMA,
VMW, ASF, 3GP, 3GPP, 3GP2

What format (container) does MediaInfo support?
- Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1, MPEG-2,
  MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP, H.264, AVC...)
- Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
- Subtitles: SRT, SSA, ASS, SAMI

%prep
%setup -q -n MediaInfo
dos2unix *.html *.txt Release/*.txt
chmod 644 *.html *.txt Release/*.txt

%build
export CFLAGS="%{rpmcflags}"
export CPPFLAGS="%{rpmcppflags}"
export CXXFLAGS="%{rpmcxxflags}"

# build CLI
cd Project/GNU/CLI
	%{__libtoolize}
	%{__aclocal}
	%{__autoconf}
	%{__automake}
	%configure
	%{__make}
cd -

# now build GUI
cd Project/GNU/GUI
	%{__libtoolize}
	%{__aclocal}
	%{__autoconf}
	%{__automake}
	%configure \
		--with-wx-config=%{_bindir}/wx-gtk2-unicode-config
	%{__make}
cd -

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C Project/GNU/CLI \
	install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C Project/GNU/GUI \
	install \
	DESTDIR=$RPM_BUILD_ROOT

# icon
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install Source/Ressource/Image/MediaInfo.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -dm 755 $RPM_BUILD_ROOT%{_pixmapsdir}
install Source/Ressource/Image/MediaInfo.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

# menu-entry
install -dm 755 $RPM_BUILD_ROOT/%{_desktopdir}
install Project/GNU/GUI/mediainfo-gui.desktop \
	$RPM_BUILD_ROOT/%{_desktopdir}
install -dm 755 $RPM_BUILD_ROOT/%{_datadir}/apps/konqueror/servicemenus
install Project/GNU/GUI/mediainfo-gui.kde3.desktop \
	$RPM_BUILD_ROOT/%{_datadir}/apps/konqueror/servicemenus/mediainfo-gui.desktop
install -dm 755 $RPM_BUILD_ROOT/%{_datadir}/kde4/services/ServiceMenus/
install Project/GNU/GUI/mediainfo-gui.kde4.desktop \
	$RPM_BUILD_ROOT/%{_datadir}/kde4/services/ServiceMenus/mediainfo-gui.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Release/ReadMe_CLI_Linux.txt
%doc License.html History_CLI.txt
%attr(755,root,root) %{_bindir}/mediainfo

%files gui
%defattr(644,root,root,755)
%doc Release/ReadMe_GUI_Linux.txt
%doc License.html History_GUI.txt
%attr(755,root,root) %{_bindir}/mediainfo-gui
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_iconsdir}/hicolor/128x128/apps/*.png
%dir %{_datadir}/apps/konqueror/servicemenus
%{_datadir}/apps/konqueror/servicemenus/*.desktop
%{_datadir}/kde4/services/ServiceMenus/*.desktop
