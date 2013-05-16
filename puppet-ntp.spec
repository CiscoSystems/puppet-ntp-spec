Name:		puppet-ntp	
Version:	0.3
Release:	1cisco%{?dist}
Summary:	Puppet Ntp module

Group:		System Environment/Base
License: 	Apache License 2.0	
URL:		https://github.com/CiscoSystems/puppet-ntp.git
Source0: 	%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%define tmpname %(echo %{name} | cut -d- -f 2-)

%description
The NTP module allows Puppet to install, configure, and then manage your Network Time Protocol service. The module allows you to setup and manage time settings across many servers from one place.

%prep
%setup -q


%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_usr}/share/puppet/modules/%{tmpname}/
cp -R * %{buildroot}/%{_usr}/share/puppet/modules/%{tmpname}/

%files
%dir %{_usr}/share/puppet/modules/%{tmpname}/
%{_usr}/share/puppet/modules/%{tmpname}/*


%defattr(-,root,root,-)
%doc README.markdown CHANGELOG LICENSE

%clean
rm -rf %{buildroot}

%changelog
* Thu May 16 2013 Pradeep Kilambi <pkilambi@cisco.com> 0.3-1cisco
- 

* Tue May 07 2013 Pradeep Kilambi <pkilambi@cisco.com> 0.2-1cisco
- new package built with tito

* Tue Apr 24 2013 Pradeep Kilambi <pkilambi@cisco.com> - 0.1-1cisco
- Initial package.

