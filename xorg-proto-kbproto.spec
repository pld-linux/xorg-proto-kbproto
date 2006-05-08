Summary:	KB protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u KB i pomocnicze
Name:		xorg-proto-kbproto
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/kbproto-%{version}.tar.bz2
# Source0-md5:	3ae193c317a3621966c3c53d83a254f4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KB protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u KB i pomocnicze.

%package devel
Summary:	KB protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u KB i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
KB protocol and ancillary headers

%description devel -l pl
Nag³ówki protoko³u KB i pomocnicze.

%prep
%setup -q -n kbproto-X11R7.0-%{version}

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/kbproto.pc
