
%define plugin	powermate
%define name	vdr-plugin-%plugin
%define version	0.0.5
%define rel	4

Summary:	VDR plugin: Control VDR through a Griffin PowerMate
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://home.arcor.de/andreas.regel/vdr_plugins.htm
Source:		http://home.arcor.de/andreas.regel/files/powermate/vdr-%plugin-%version.tgz
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin allows using a Griffin PowerMate to control some of VDR's
functions through the mapping of remote control keys to PowerMate actions.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# the PowerMate device (default is /dev/input/event0)
var=POWERMATE_DEVICE
param=--device=POWERMATE_DEVICE
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.5-3mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.5-2mdv2009.1
+ Revision: 359352
- rebuild for new vdr

* Sun May 11 2008 Anssi Hannula <anssi@mandriva.org> 0.0.5-1mdv2009.0
+ Revision: 205448
- new version
- drop patches, fixed upstream

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.3-14mdv2009.0
+ Revision: 197964
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.3-13mdv2009.0
+ Revision: 197708
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt for api changes of VDR 1.3.38 (P0 from e-tobi)
- adapt for api changes of VDR 1.5.0 (P1 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.3-12mdv2008.1
+ Revision: 145188
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-11mdv2008.1
+ Revision: 103183
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-10mdv2008.0
+ Revision: 50032
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-9mdv2008.0
+ Revision: 42119
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.3-8mdv2008.0
+ Revision: 22770
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-7mdv2007.0
+ Revision: 90961
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-6mdv2007.1
+ Revision: 74071
- rebuild for new vdr
- Import vdr-plugin-powermate

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-2mdv2007.0
- rebuild for new vdr

* Wed Jul 19 2006 Anssi Hannula <anssi@mandriva.org> 0.0.3-1mdv2007.0
- initial Mandriva release

