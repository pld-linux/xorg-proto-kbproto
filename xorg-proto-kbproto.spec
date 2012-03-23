Summary:	KB extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia KB
Name:		xorg-proto-kbproto
Version:	1.0.6
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/kbproto-%{version}.tar.bz2
# Source0-md5:	677ea8523eec6caca86121ad2dca0b71
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd43-xml
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KB (XKEYBOARD) extension headers.

%description -l pl.UTF-8
Pliki nagłówkowe rozszerzenia KB (XKEYBOARD).

%package devel
Summary:	KB extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia KB
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
KB (XKEYBOARD) extension headers.

%description devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia KB (XKEYBOARD).

%prep
%setup -q -n kbproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog README specs/{XKBproto-*.svg,xkbproto.html}
%{_includedir}/X11/extensions/XKB*.h
%{_pkgconfigdir}/kbproto.pc
