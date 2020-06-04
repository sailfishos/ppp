Name:       ppp
Summary:    Point-to-Point
Version:    2.4.8
Release:    1
Group:      Applications/Internet
License:    BSD and GPLv2+ and LGPLv2+ and Public Domain
URL:        https://ppp.samba.org/
Source0:    https://download.samba.org/pub/%{name}/%{name}-%{version}.tar.gz
Patch0:     ppp-destdir.patch
Requires:   openssl-libs
BuildRequires:  coreutils
BuildRequires:  sed
BuildRequires:  openssl-devel

%description
PPP point-to-point tunnelling daemon.


%package devel
Summary:    PPP devel files
Group:      Development/Libraries
Requires:   ppp-libs = %{version}-%{release}

%description devel
PPP devel files.

%package libs
Summary:    PPP libraries
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description libs
PPP libraries.


%prep
%setup -q -n %{name}-%{version}/%{name}
%patch0 -p1

%build
%configure --prefix=/usr
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

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
