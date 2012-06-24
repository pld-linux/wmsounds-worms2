Summary:	Worms2 sounds for WindowMaker
Summary(pl):	D�wi�ki z Worms2 dla WindowMakera
Name:		wmsounds-worms2
Version:	2
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	ftp://shadowmere.student.utwente.nl/pub/WindowMaker/worms2sounds.tar.gz
Requires:	WindowMaker
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix 	/usr/X11R6

%description
A bunch of standard Worms 2 sounds for WindowMaker.

%description -l pl
Zestaw d�wi�k�w z Worms 2 dla WindowMakera.

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
