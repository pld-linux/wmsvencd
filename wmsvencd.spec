Summary:	Window Maker Dockable CD-Player with CDDB
Summary(pl):	Dokowalny odtwarzacz CD dla Window Makera z obs³ug± CDDB
Name:		wmsvencd
Version:	0.5.0
Release:	1
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://www.cs.uwa.edu.au/~cook-s/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop 
Patch0:         %{name}-compile.patch
URL:            http://www.linuxfreak.com/~wmsvencd
BuildRequires: 	XFree86-devel
BuildRequires:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6
%define _mandir %{_prefix}/man

%description
wmsvencd is yet another CD player for X. It displays the current track number, time,
disc title, song title, and CD player controls all in atiny 64x64 pixels.

%description -l pl
wsvencd jest jeszcze jednym odtwarzaczem CD pod X-y. Wy¶wietla bie¿±cy numer
piosenki, czas, tytu³ p³yty, tytu³ piosenki oraz kontrolki odtwarzacza -
wszystko w malutkim obszarze 64x64 pixele. 

%prep
%setup -q
%patch0 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT/usr/X11R6/share/applnk/DockApplets

install -s %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1x $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/DockApplets

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*

/usr/X11R6/share/applnk/DockApplets/%{name}.desktop
