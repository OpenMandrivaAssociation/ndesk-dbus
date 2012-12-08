%define name ndesk-dbus
%define version 0.6.1a
%define release %mkrel 10
%define pkgname ndesk-dbus-1.0

Summary: Managed D-Bus implementation
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.ndesk.org/archive/dbus-sharp/%{name}-%{version}.tar.gz
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

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
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
%doc README COPYING
%_prefix/lib/mono/%pkgname
%_prefix/lib/mono/gac/NDesk.DBus/

%files devel
%defattr(-,root,root)
%doc examples
%_datadir/pkgconfig/%pkgname.pc


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.1a-8mdv2011.0
+ Revision: 666602
- mass rebuild

* Fri Oct 08 2010 Funda Wang <fwang@mandriva.org> 0.6.1a-7mdv2011.0
+ Revision: 584163
- rebuild

* Mon Aug 09 2010 Götz Waschk <waschk@mandriva.org> 0.6.1a-6mdv2011.0
+ Revision: 567916
- split out devel package

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.1a-5mdv2010.1
+ Revision: 523409
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.6.1a-4mdv2010.0
+ Revision: 426247
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.6.1a-3mdv2009.1
+ Revision: 351629
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 0.6.1a-2mdv2009.0
+ Revision: 265197
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 0.6.1a-1mdv2009.0
+ Revision: 192442
- new version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Oct 21 2007 Götz Waschk <waschk@mandriva.org> 0.6.0-1mdv2008.1
+ Revision: 101052
- new version
- fix build

* Mon Aug 06 2007 Götz Waschk <waschk@mandriva.org> 0.5.2-2mdv2008.0
+ Revision: 59367
- remove file conflicting with native dbus

* Mon Aug 06 2007 Götz Waschk <waschk@mandriva.org> 0.5.2-1mdv2008.0
+ Revision: 59362
- Import ndesk-dbus



* Mon Aug  6 2007 Götz Waschk <waschk@mandriva.org> 0.5.2-1mdv2008.0
- initial package
