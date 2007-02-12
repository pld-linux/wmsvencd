Summary:	Window Maker Dockable CD-Player with CDDB
Summary(pl.UTF-8):   Dokowalny odtwarzacz CD dla Window Makera z obsługą CDDB
Name:		wmsvencd
Version:	0.5.0
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.harshbutfair.org/dl/%{name}-%{version}.tar.gz
# Source0-md5:	2315a1e05534cdfec20134bbccefc5cc
Source1:	%{name}.desktop
Patch0:		%{name}-compile.patch
URL:		http://www.harshbutfair.org/software/wmsvencd.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmsvencd is yet another CD player for X. It displays the current track
number, time, disc title, song title, and CD player controls all in
atiny 64x64 pixels.

%description -l pl.UTF-8
wsvencd jest jeszcze jednym odtwarzaczem CD pod X-y. Wyświetla bieżący
numer piosenki, czas, tytuł płyty, tytuł piosenki oraz kontrolki
odtwarzacza - wszystko w malutkim obszarze 64x64 pixele.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_desktopdir}/docklets

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1x $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/docklets/%{name}.desktop
