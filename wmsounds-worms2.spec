Summary:	Worms2 sounds for WindowMaker
Summary(pl):	D¼wiêki z Worms2 dla WindowMakera
Name:		wmsounds-worms2
Version:	1
Release:	1
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Copyright:	GPL
Source:		ftp://shadowmere.student.utwente.nl/pub/WindowMaker/worms2sounds.tar.gz
Requires:	WindowMaker
BuildArch:	noarch
BuildRoot:   	/tmp/%{name}-%{version}-root

%define 	_prefix 	/usr/X11R6

%description
A bunch of standard Worms 2 sounds for WindowMaker.

%description -l pl
Zestaw d¼wiêków z Worms 2 dla WindowMakera.

%prep
%setup -q -c
%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/WindowMaker/{SoundSets,Sounds}

install SoundSets/Worms2 $RPM_BUILD_ROOT%{_datadir}/WindowMaker/SoundSets
install Sounds/*.wav     $RPM_BUILD_ROOT%{_datadir}/WindowMaker/Sounds

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/WindowMaker/Sounds/*.wav
%config %verify(not size mtime md5) %{_datadir}/WindowMaker/SoundSets/Worms2
