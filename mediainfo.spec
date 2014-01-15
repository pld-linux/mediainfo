Summary:	Supplies technical and tag information about a video or audio file (CLI)
Summary(pl.UTF-8):	Informacje techniczne i znaczniki dla plików wideo i dźwiękowych (CLI)
Name:		mediainfo
Version:	0.7.61
Release:	2
License:	LGPL v2+
Group:		Applications/Multimedia
Source0:	http://downloads.sourceforge.net/mediainfo/%{name}_%{version}.tar.bz2
# Source0-md5:	46fd776968ec1047cd2a5056a906cdf2
URL:		http://mediainfo.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libmediainfo-devel >= %{version}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libzen-devel
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.566
BuildRequires:	sed >= 4.0
BuildRequires:	wxGTK2-unicode-devel >= 2.6.0
BuildRequires:	zlib-devel
Requires:	libmediainfo >= %{version}
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

Supported files: DivX, XviD, H263, H.263, H264, x264, ASP, AVC,
iTunes, MPEG-1, MPEG1, MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V,
QuickTime, RealVideo, RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2,
MSMPEG4v3, VOB, DVD, WMA, VMW, ASF, 3GP, 3GPP, 3GP2

Supported formats/containers:
- Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1, MPEG-2,
  MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP, H.264, AVC...)
- Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
- Subtitles: SRT, SSA, ASS, SAMI

%description -l pl.UTF-8
Program MediaInfo działający z linii poleceń (CLI).

Dostępne są informacje:
- ogólne: tytuł, autor, reżyser, album, numer ścieżki, data, czas
  trwania...
- wideo: kodek, proporcje, liczba klatek na sekundę, pasmo...
- dźwięk: kodek, częstotliwość próbkowania, liczba kanałów, język,
  pasmo...
- tekst: język napisów
- książki: liczba rozdziałów, ich lista

Obsługiwane pliki: DivX, XviD, H263, H.263, H264, x264, ASP, AVC,
iTunes, MPEG-1, MPEG1, MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V,
QuickTime, RealVideo, RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2,
MSMPEG4v3, VOB, DVD, WMA, VMW, ASF, 3GP, 3GPP, 3GP2

Obsługiwane formaty/kontenery:
- wideo: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1, MPEG-2,
  MPEG-4, DVD (VOB) (kodeki: DivX, XviD, MSMPEG4, ASP, H.264, AVC...)
- dźwięk: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
- napisy: SRT, SSA, ASS, SAMI

%package gui
Summary:	Supplies technical and tag information about a video or audio file (GUI)
Summary(pl.UTF-8):	Informacje techniczne i znaczniki dla plików wideo i dźwiękowych (GUI)
Group:		X11/Applications/Multimedia
Requires:	kde-common-dirs >= 0.5
Requires:	libmediainfo >= %{version}
Requires:	libzen >= 0.4.9
Requires:	wxGTK2-unicode >= 2.6.0

%description gui
MediaInfo (Graphical User Interface).

What information can I get from MediaInfo?
- General: title, author, director, album, track number, date,
  duration...
- Video: codec, aspect, fps, bitrate...
- Audio: codec, sample rate, channels, language, bitrate...
- Text: language of subtitle
- Chapters: number of chapters, list of chapters

Supported files: DivX, XviD, H263, H.263, H264, x264, ASP, AVC,
iTunes, MPEG-1, MPEG1, MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V,
QuickTime, RealVideo, RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2,
MSMPEG4v3, VOB, DVD, WMA, VMW, ASF, 3GP, 3GPP, 3GP2

Supported formats/containers:
- Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1, MPEG-2,
  MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP, H.264, AVC...)
- Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
- Subtitles: SRT, SSA, ASS, SAMI

%description gui -l pl.UTF-8
Program MediaInfo z graficznym interfejsem użytkownika (GUI).

Dostępne są informacje:
- ogólne: tytuł, autor, reżyser, album, numer ścieżki, data, czas
  trwania...
- wideo: kodek, proporcje, liczba klatek na sekundę, pasmo...
- dźwięk: kodek, częstotliwość próbkowania, liczba kanałów, język,
  pasmo...
- tekst: język napisów
- książki: liczba rozdziałów, ich lista

Obsługiwane pliki: DivX, XviD, H263, H.263, H264, x264, ASP, AVC,
iTunes, MPEG-1, MPEG1, MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V,
QuickTime, RealVideo, RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2,
MSMPEG4v3, VOB, DVD, WMA, VMW, ASF, 3GP, 3GPP, 3GP2

Obsługiwane formaty/kontenery:
- wideo: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1, MPEG-2,
  MPEG-4, DVD (VOB) (kodeki: DivX, XviD, MSMPEG4, ASP, H.264, AVC...)
- dźwięk: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
- napisy: SRT, SSA, ASS, SAMI

%prep
%setup -q -n MediaInfo
%undos *.html *.txt Release/*.txt
chmod 644 *.html *.txt Release/*.txt

%build
# build CLI
cd Project/GNU/CLI
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}
# now build GUI
cd ../../../Project/GNU/GUI
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-wx-config=%{_bindir}/wx-gtk2-unicode-config
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C Project/GNU/CLI install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C Project/GNU/GUI install \
	DESTDIR=$RPM_BUILD_ROOT

# icon
install -d $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install Source/Resource/Image/MediaInfo.png \
	$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -d $RPM_BUILD_ROOT%{_pixmapsdir}
install Source/Resource/Image/MediaInfo.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

# menu-entry
install -d $RPM_BUILD_ROOT%{_desktopdir}
install Project/GNU/GUI/mediainfo-gui.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}
install -d $RPM_BUILD_ROOT%{_datadir}/apps/konqueror/servicemenus
install Project/GNU/GUI/mediainfo-gui.kde3.desktop \
	$RPM_BUILD_ROOT/%{_datadir}/apps/konqueror/servicemenus/mediainfo-gui.desktop
install -d $RPM_BUILD_ROOT%{_datadir}/kde4/services/ServiceMenus
install Project/GNU/GUI/mediainfo-gui.kde4.desktop \
	$RPM_BUILD_ROOT/%{_datadir}/kde4/services/ServiceMenus/mediainfo-gui.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc License.html History_CLI.txt Release/ReadMe_CLI_Linux.txt
%attr(755,root,root) %{_bindir}/mediainfo

%files gui
%defattr(644,root,root,755)
%doc License.html History_GUI.txt Release/ReadMe_GUI_Linux.txt
%attr(755,root,root) %{_bindir}/mediainfo-gui
%{_desktopdir}/mediainfo-gui.desktop
%{_pixmapsdir}/mediainfo.png
%{_iconsdir}/hicolor/128x128/apps/mediainfo.png
%dir %{_datadir}/apps/konqueror/servicemenus
%{_datadir}/apps/konqueror/servicemenus/mediainfo-gui.desktop
%{_datadir}/kde4/services/ServiceMenus/mediainfo-gui.desktop
