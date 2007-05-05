
%define plugin	powermate
%define name	vdr-plugin-%plugin
%define version	0.0.3
%define rel	8

Summary:	VDR plugin: Control VDR through a Griffin PowerMate
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://home.arcor.de/andreas.regel/vdr_plugins.htm
Source:		http://home.arcor.de/andreas.regel/files/powermate/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
This plugin allows using a Griffin PowerMate to control some of VDR's
functions through the mapping of remote control keys to PowerMate actions.

%prep
%setup -q -n %plugin-%version

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


