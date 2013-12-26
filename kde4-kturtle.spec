%define		_state		stable
%define		orgname		kturtle

Summary:	K Desktop Environment - A Logo interpreter
Summary(pl.UTF-8):	K Desktop Environment - Interpreter języka Logo
Name:		kde4-kturtle
Version:	4.12.0
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	1253a3ebfd31feb5c193c84e610eb47a
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
Obsoletes:	kde4-kdeedu-kturtle < 4.6.99
Obsoletes:	kturtle <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KTurtle is a Logo programming language interpreter for KDE. The Logo
programming language is very easy and thus it can be used by young
children. A unique quality of Logo is that the commands or
instructions can be translated (please see the translation how to if
you want to help in your own language), so the 'programmer' can
program in his or her native language. This makes Logo ideal for
teaching kids the basics of programming, mathematics and geometry. One
of the reasons many children like Logo is because of the turtle, a
programmable icon which can be moved around the screen with simple
commands and can be programmed to draw objects.

KTurtle features:
- integrated Logo interpreter, no need to download any other program
- powerful editor for the Logo commands with syntax highlighting, line
  numbering and more
- nice "playground" for the turtle where your commands visualized
- translation of the Logo commands (among others in: Dutch, French
  German, Latin and Swedish)
- context help for each Logo command

%description -l pl.UTF-8
KTurtle to interpreter języka programowania Logo dla KDE. Język Logo
jest bardzo łatwy, przez co może być używany przez małe dzieci.
Unikalna jakość Logo polega na tym, że polecenia czy instrukcje mogą
być tłumaczone (proszę zobaczyć howto dla tłumaczy, aby pomóc przy
tłumaczeniu na własny język), dzięki czemu "programista" może
programować w języku ojczystym. To czyni Logo idealnym do nauki dzieci
podstaw programowania, matematyki i geometrii. Jednym z powodów, dla
których wiele dzieci lubi Logo, jest żółw - programowalna ikona, którą
można przesuwać po ekranie prostymi poleceniami i programować do
rysowania obiektów.

Możliwości KTurtle:
- zintegrowany interpreter Logo, nie trzeba ściągać żadnego innego
  programu
- potężny edytor do poleceń Logo z podświetlaniem składni,
  numerowaniem linii itp.
- ładne "boisko" dla żółwia, gdzie wizualizowane są polecenia
- tłumaczenia poleceń Logo (m.in. na język francuski, holenderski,
  łaciński, niemiecki i szwedzki)
- pomoc kontekstowa dla każdego polecenia Logo.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kturtle
%{_desktopdir}/kde4/kturtle.desktop
%{_datadir}/apps/kturtle
%{_iconsdir}/hicolor/*x*/apps/kturtle.png
%{_iconsdir}/hicolor/scalable/apps/kturtle.svgz
%{_datadir}/config/kturtle.knsrc
