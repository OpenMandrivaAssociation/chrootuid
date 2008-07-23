%define name chrootuid
%define version 1.3
%define release %mkrel 4

Summary:	Run command in restricted environment
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	ftp://ftp.porcupine.org/pub/security/%{name}%{version}.tar.bz2
License:	BSD
Url:		ftp://ftp.porcupine.org/pub/security/index.html
Group:		System/Servers
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	groff

%description
Chrootuid makes it easy to run a network service at low privilege level
and with restricted file system access.
At Eindhoven University, they use this program to run the gopher
and www (world-wide web) network daemons in a minimal environment:
the daemons have access only to their own directory tree,
and run under a low-privileged userid.
The arrangement greatly reduces the impact of possible loopholes
in daemon software.

%prep
%setup -q -n %{name}%{version}

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 0755 %{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}
install -D -m 0755 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1*

