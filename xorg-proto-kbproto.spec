Summary:	KB protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu KB i pomocnicze
Name:		xorg-proto-kbproto
Version:	1.0.3
Release:	2
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/kbproto-%{version}.tar.bz2
# Source0-md5:	6092cdb0a1225f95356ddbe6c2abaad5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KB protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu KB i pomocnicze.

%package devel
Summary:	KB protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu KB i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
KB protocol and ancillary headers

%description devel -l pl.UTF-8
Nagłówki protokołu KB i pomocnicze.

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/kbproto.pc
