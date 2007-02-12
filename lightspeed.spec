Summary:	Light Speed! - an interactive relativistic simulator
Summary(pl.UTF-8):   Light SPeed! - interaktywny, relatywistyczny symulator
Name:		lightspeed
Version:	1.2a
Release:	0.1
License:	MPL 1.0
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/lightspeed/%{name}-%{version}.tar.gz
# Source0-md5:	d6162f8b200db8ebfade791a71a439c0
URL:		http://lightspeed.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.0.1
BuildRequires:	gtkglarea1-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Light Speed! is an OpenGL-based program which illustrates the effects
of special relativity on the appearance of moving objects. When an
object accelerates past a few million meters per second, these effects
begin to grow noticeable, becoming more and more pronounced as the
speed of light is approached. These relativistic effects are
viewpoint-dependent, and include shifts in length, object hue,
brightness and shape.

The moving object is, by default, a geometric lattice. 3D Studio and
LightWave 3D objects may be imported as well. Best of all, the
simulator is completely interactive, rendering the exotic distortions
in real-time!

%description -l pl.UTF-8
Light Speed! jest opartym na OpenGL programem ilustrującym efekty
relatywistyczne w zachowaniu ruchomych obiektów. Kiedy obiekt
przyspiesza powyżej kilku milionów metrów na sekundę, te efekty
zaczynają być widoczne, tym bardziej, im bardziej prędkość zbliża się
do prędkości światła. Te efekty relatywistyczne są zależne od
położenia obserwatora i zawierają: zmiany długości, koloru, jasności 
i kształtu.

Ruchomy obiekt jest bryłą geometryczną. Mogą być importowane obiekty 
z 3D Studio i LightWave 3D. Symulator jest w pełni interaktywny,
renderuje egzotyczne zniekształcenia w czasie rzeczywistym!

%prep
%setup -q

%build
rm -f missing
#%%{__aclocal}
#%%{__autoconf}
#%%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog MATH README TODO
%attr(755,root,root) %{_bindir}/*
