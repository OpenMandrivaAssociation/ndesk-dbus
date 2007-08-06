%define name ndesk-dbus
%define version 0.5.2
%define release %mkrel 1
%define oname dbus-sharp
%define pkgname ndesk-dbus-1.0

Summary: Managed D-Bus implementation
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.ndesk.org/archive/dbus-sharp/%{oname}-%{version}.tar.bz2
License: MIT
Group: System/Libraries
Url: http://www.ndesk.org/DBusSharp
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildArch: noarch

%description
dbus-sharp is a C# implementation of D-Bus. It's often referred to as
"managed D-Bus" to avoid confusion with existing bindings (which wrap
libdbus).

D-Bus is an inter-process communication framework that lets
applications interface with the system event bus as well as allowing
them to talk to one another in a peer-to-peer configuration.

%prep
%setup -q -n %oname-%version

%build
%make
cd examples
make

%install
rm -rf $RPM_BUILD_ROOT
gacutil -i -check_refs -package %pkgname src/NDesk.DBus.dll -root %buildroot/%_prefix/lib
install -m 644 -D %pkgname.pc.in %buildroot%_datadir/pkgconfig/%pkgname.pc
perl -pi -e "s^\@prefix\@^%_prefix^" %buildroot%_datadir/pkgconfig/%pkgname.pc
install tools/dbus-monitor.exe %buildroot/%_prefix/lib/mono/%pkgname
install -d -m 755 %buildroot%_bindir
cat > %buildroot%_bindir/dbus-monitor << EOF
#!/bin/sh
mono --debug %_prefix/lib/mono/%pkgname/dbus-monitor.exe \$@
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING examples
%attr(755,root,root) %_bindir/dbus-monitor
%_prefix/lib/mono/%pkgname
%_prefix/lib/mono/gac/NDesk.DBus/
%_datadir/pkgconfig/%pkgname.pc
