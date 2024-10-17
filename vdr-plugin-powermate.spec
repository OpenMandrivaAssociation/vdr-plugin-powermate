%define plugin	powermate

Summary:	VDR plugin: Control VDR through a Griffin PowerMate
Name:		vdr-plugin-%plugin
Version:	0.0.5
Release:	6
Group:		Video
License:	GPL
URL:		https://home.arcor.de/andreas.regel/vdr_plugins.htm
Source:		http://home.arcor.de/andreas.regel/files/powermate/vdr-%plugin-%{version}.tgz
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin allows using a Griffin PowerMate to control some of VDR's
functions through the mapping of remote control keys to PowerMate actions.

%prep
%setup -q -n %plugin-%{version}
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
%doc README HISTORY




