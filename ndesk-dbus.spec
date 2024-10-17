%define pkgname ndesk-dbus-1.0

Summary:	Managed D-Bus implementation
Name:		ndesk-dbus
Version:	0.6.1a
Release:	22
License:	MIT
Group:		System/Libraries
Url:		https://www.ndesk.org/DBusSharp
Source0:	http://www.ndesk.org/archive/dbus-sharp/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(mono)

%description
dbus-sharp is a C Sharp implementation of D-Bus. It's often referred to as
"managed D-Bus" to avoid confusion with existing bindings (which wrap
libdbus).

D-Bus is an inter-process communication framework that lets
applications interface with the system event bus as well as allowing
them to talk to one another in a peer-to-peer configuration.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
dbus-sharp is a C# implementation of D-Bus. It's often referred to as
"managed D-Bus" to avoid confusion with existing bindings (which wrap
libdbus).

D-Bus is an inter-process communication framework that lets
applications interface with the system event bus as well as allowing
them to talk to one another in a peer-to-peer configuration.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
%make_build

%install
%make_install pkgconfigdir=%{_datadir}/pkgconfig

%files
%doc README COPYING
%{_prefix}/lib/mono/%{pkgname}
%{_prefix}/lib/mono/gac/NDesk.DBus/

%files devel
%doc examples
%{_datadir}/pkgconfig/%{pkgname}.pc

