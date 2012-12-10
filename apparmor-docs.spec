%define ver 2.0.1
%define rev 237

Name: apparmor-docs
Summary: AppArmor documentation and manpages
Version: %ver
Release: %mkrel 1.%rev.3
License: GPL
Group: System/Base
Source0: apparmor-docs-%{ver}-%{rev}.tar.gz
URL: http://forge.novell.com/modules/xfmod/project/?apparmor
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(id -u -n)
BuildArch: noarch
# pod2man, pod2html
BuildRequires: perl

%description
This package contains manpages and extra documentation for AppArmor.

%prep
%setup -q

%build
%make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install_manpages

# already present in apparmor-parser package
rm -f %{buildroot}%{_mandir}/man5/apparmor.d.5*
rm -f %{buildroot}%{_mandir}/man5/apparmor.vim.5*
rm -f %{buildroot}%{_mandir}/man5/subdomain.conf.5*
rm -f %{buildroot}%{_mandir}/man7/apparmor.7*
rm -f %{buildroot}%{_mandir}/man8/apparmor_parser.8*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.html *.css
%{_mandir}/man?/*





%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.1-1.237.3mdv2011.0
+ Revision: 616598
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 2.0.1-1.237.2mdv2010.0
+ Revision: 423989
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 2.0.1-1.237.1mdv2008.1
+ Revision: 135823
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import apparmor-docs


* Wed Jun 13 2007 Andreas Hasenack <andreas@mandriva.com> 2.0.1-1.237.1mdv2008.0
+ Revision: 38925
- removed conflicting manpages
- updated url
- Import apparmor-docs

