# Conditional build:
%bcond_without	gui	# build without GUI

Summary:	Supplies technical and tag information about a video or audio file (CLI)
Summary(pl.UTF-8):	Informacje techniczne i znaczniki dla plików wideo i dźwiękowych (CLI)
Name:		mediainfo
Version:	23.04
Release:	1
License:	BSD or Apache v2.0 or LGPL v2.1+ or GPL v2+ or MPL v2.0+
Group:		Applications/Multimedia
#Source0Download: https://github.com/MediaArea/MediaInfo/releases
Source0:	https://github.com/MediaArea/MediaInfo/archive/v%{version}/MediaInfo-%{version}.tar.gz
# Source0-md5:	fc769e1801b63bf89362daea377665e8
URL:		https://mediaarea.net/MediaInfo
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libmediainfo-devel >= %{version}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libzen-devel >= 0.4.37
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.566
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
%{?with_gui:BuildRequires:	wxGTK3-unicode-devel >= 3.0.0}
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	libmediainfo >= %{version}
Requires:	libzen >= 0.4.37
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
Requires:	libzen >= 0.4.37
Requires:	wxGTK3-unicode >= 3.0.0

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
%setup -q -n MediaInfo-%{version}
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
%if %{with gui}
# now build GUI
cd ../../../Project/GNU/GUI
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-wx-config=%{_bindir}/wx-gtk3-unicode-config
%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C Project/GNU/CLI install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with gui}
%{__make} -C Project/GNU/GUI install \
	DESTDIR=$RPM_BUILD_ROOT

# Remove kde3 and kde4 files
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/{apps,kde4}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc License.html History_CLI.txt README.md Release/ReadMe_CLI_Linux.txt
%attr(755,root,root) %{_bindir}/mediainfo

%if %{with gui}
%files gui
%defattr(644,root,root,755)
%doc License.html History_GUI.txt Release/ReadMe_GUI_Linux.txt
%attr(755,root,root) %{_bindir}/mediainfo-gui
%{_desktopdir}/mediainfo-gui.desktop
%{_pixmapsdir}/mediainfo.xpm
%{_iconsdir}/hicolor/256x256/apps/mediainfo.png
%{_iconsdir}/hicolor/scalable/apps/mediainfo.svg
%{_datadir}/kservices5/ServiceMenus/mediainfo-gui.desktop
%{_datadir}/metainfo/mediainfo-gui.metainfo.xml
%endif
