Name:       ppp
Summary:    Point-to-Point
Version:    2.5.2
Release:    1
License:    BSD and GPLv2+ and LGPLv2+ and Public Domain
URL:        https://github.com/sailfishos/ppp
Source0:    %{name}-%{version}.tar.gz
Requires:   openssl-libs
BuildRequires:  coreutils
BuildRequires:  sed
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(libcrypt)

%description
PPP point-to-point tunnelling daemon.


%package devel
Summary:    PPP devel files
Requires:   ppp-libs = %{version}-%{release}

%description devel
PPP devel files.

%package libs
Summary:    PPP libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description libs
PPP libraries.


%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
autoreconf -fi
%configure --prefix=/usr
%make_build

%install
rm -rf %{buildroot}
%make_install

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%{_sbindir}/chat
%{_sbindir}/pppd
%{_sbindir}/pppdump
%{_sbindir}/pppoe-discovery
%{_sbindir}/pppstats
%exclude %{_mandir}/man8/chat.8.gz
%exclude %{_mandir}/man8/pppd.8.gz
%exclude %{_mandir}/man8/pppdump.8.gz
%exclude %{_mandir}/man8/pppstats.8.gz
%exclude %{_mandir}/man8/pppd-radius.8.gz
%exclude %{_mandir}/man8/pppd-radattr.8.gz
%exclude %{_mandir}/man8/pppoe-discovery.8.gz
%exclude %{_sysconfdir}/ppp/chap-secrets.example
%exclude %{_sysconfdir}/ppp/eaptls-client.example
%exclude %{_sysconfdir}/ppp/eaptls-server.example
%exclude %{_sysconfdir}/ppp/openssl.cnf.example
%exclude %{_sysconfdir}/ppp/options.example
%exclude %{_sysconfdir}/ppp/pap-secrets.example

%files devel
%{_includedir}/pppd
%{_libdir}/pkgconfig/pppd.pc

%files libs
%{_libdir}/pppd
