Name:       ppp
Summary:    Point-to-Point
Version:    2.4.9
Release:    1
License:    BSD and GPLv2+ and LGPLv2+ and Public Domain
URL:        https://ppp.samba.org/
Source0:    %{name}-%{version}.tar.gz
Patch0:     0001-ppp-2.4.9-build-sys-don-t-hardcode-LIBDIR-but-set-it-according.patch
Patch1:     0002-Revert-pppd-Fix-setting-IPv6-peer-address-212.patch
Requires:   openssl-libs
BuildRequires:  coreutils
BuildRequires:  sed
BuildRequires:  openssl-devel
BuildRequires:  libpcap-devel

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
%configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make %{?_smp_mflags} INSTROOT=%{buildroot} install

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
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

%files devel
%defattr(-,root,root,-)
%{_includedir}/pppd

%files libs
%defattr(-,root,root,-)
%{_libdir}/pppd
