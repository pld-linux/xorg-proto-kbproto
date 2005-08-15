# $Rev: 3241 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	KB protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u KB i pomocnicze
Name:		xorg-proto-kbproto
Version:	1.0
Release:	0.02
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/proto/kbproto-%{version}.tar.bz2
# Source0-md5:	45af2e6c1fd9a5d858cdfc827b0d504e
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/kbproto-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
KB protocol and ancillary headers.

%description -l pl
Nag��wki protoko�u KB i pomocnicze.


%package devel
Summary:	KB protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u KB i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
KB protocol and ancillary headers

%description devel -l pl
Nag��wki protoko�u KB i pomocnicze.


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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/kbproto.pc
