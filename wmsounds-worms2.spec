Summary:	Worms2 sounds for WindowMaker
Summary(pl.UTF-8):	Dźwięki z Worms2 dla WindowMakera
Name:		wmsounds-worms2
Version:	2
Release:	5
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	ftp://shadowmere.student.utwente.nl/pub/WindowMaker/worms2sounds.tar.gz
# Source0-md5:	ba753aac69aca1e4fd11430ecb46d20f
Requires:	wmsoundserver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
A bunch of standard Worms 2 sounds for WindowMaker.

%description -l pl.UTF-8
Zestaw dźwięków z Worms 2 dla WindowMakera.

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
%config %verify(not md5 mtime size) %{_datadir}/WindowMaker/SoundSets/Worms2
