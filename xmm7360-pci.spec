%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     xmm7360-pci
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Driver for Fibocom L850-GL / Intel XMM7360. 
License:  GPLv3
URL:      https://github.com/ignic/xmm7360-pci

VCS:      {{{ git_dir_vcs }}}
Source:   {{{ git_dir_pack }}}

Requires: python3-configargparse
Requires: python3-pyroute2

BuildRequires: systemd-rpm-macros

%description
Driver for Fibocom L850-GL / Intel XMM7360.

%prep
{{{ git_dir_setup_macro }}}

%install
install -m 755 -D -t %{buildroot}%{_datadir}/%{name}/rpc rpc/open_xdatachannel.py
install -m 644 -D -t %{buildroot}%{_datadir}/%{name}/rpc rpc/rpc*.py
install -m 644 -D -t %{buildroot}%{_unitdir} examples/xmm7360.service
install -m 644 -D xmm7360.ini.sample %{buildroot}%{_sysconfdir}/xmm7360

%files
%doc README.md
%{_datadir}/%{name}/rpc/*
%{_unitdir}/*
%{_sysconfdir}/xmm7360

%changelog
* Wed May 15 2024 ignic <ignic@mail.org> - 1
- First package
