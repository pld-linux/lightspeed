Summary:	Light Speed! - an interactive relativistic simulator
Name:		lightspeed
Version:	1.2
Release:	1
Copyright:	MozPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://fox.mit.edu/skunk/soft/src/%{name}-%{version}.tar.gz
URL:		http://fox.mit.edu/skunk/soft/lightspeed/
BuildRequires:	gtk+-devel >= 1.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define _prefix /usr/X11R6

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

%prep
%setup -q

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

gzip -9nf AUTHORS CONTROLS COPYING ChangeLog MATH OVERVIEW README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,CONTROLS,COPYING,ChangeLog,MATH,OVERVIEW,README,TODO}.gz
%attr(755,root,root) %{_bindir}/*
