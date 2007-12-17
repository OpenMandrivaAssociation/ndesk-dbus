%define name ndesk-dbus
%define version 0.6.0
%define release %mkrel 1
%define pkgname ndesk-dbus-1.0

Summary: Managed D-Bus implementation
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.ndesk.org/archive/dbus-sharp/%{name}-%{version}.tar.gz
License: MIT
Group: System/Libraries
Url: http://www.ndesk.org/DBusSharp
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
%setup -q -n %name-%version

%build
./configure --prefix=%_prefix
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std pkgconfigdir=%_datadir/pkgconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING examples
%_prefix/lib/mono/%pkgname
%_prefix/lib/mono/gac/NDesk.DBus/
%_datadir/pkgconfig/%pkgname.pc
