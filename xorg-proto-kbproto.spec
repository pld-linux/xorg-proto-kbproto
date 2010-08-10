Summary:	KB extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia KB
Name:		xorg-proto-kbproto
Version:	1.0.5
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/kbproto-%{version}.tar.bz2
# Source0-md5:	e7edb59a3f54af15f749e8f3e314ee62
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.3
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
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/XKB*.h
%{_pkgconfigdir}/kbproto.pc
