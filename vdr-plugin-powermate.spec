
%define plugin	powermate
%define name	vdr-plugin-%plugin
%define version	0.0.3
%define rel	14

Summary:	VDR plugin: Control VDR through a Griffin PowerMate
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://home.arcor.de/andreas.regel/vdr_plugins.htm
Source:		http://home.arcor.de/andreas.regel/files/powermate/vdr-%plugin-%version.tar.bz2
Patch0:		91_powermate-0.0.3-1.3.38.dpatch
Patch1:		92_powermate-0.0.3-1.5.0.dpatch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin allows using a Griffin PowerMate to control some of VDR's
functions through the mapping of remote control keys to PowerMate actions.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# the PowerMate device (default is /dev/input/event0)
var=POWERMATE_DEVICE
param=--device=POWERMATE_DEVICE
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


