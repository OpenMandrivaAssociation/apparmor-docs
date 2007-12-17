%define ver 2.0.1
%define rev 237

Name: apparmor-docs
Summary: AppArmor documentation and manpages
Version: %ver
Release: %mkrel 1.%rev.1
License: GPL
Group: System/Base
Source0: apparmor-docs-%{ver}-%{rev}.tar.gz
URL: http://forge.novell.com/modules/xfmod/project/?apparmor
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



