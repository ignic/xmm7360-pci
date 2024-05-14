%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     xmm7360-pci
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  Driver for Fibocom L850-GL / Intel XMM7360. 
License:  GPLv3
URL:      https://github.com/ignic/xmm7360-pci

Source:   %{url}/archive/refs/heads/master.tar.gz

Provides: %{name}-kmod-common = %{version}
Requires: %{name}-kmod >= %{version}
Requires: python3-configargparse
Requires: python3-pyroute2

BuildRequires: systemd-rpm-macros

%description
Driver for Fibocom L850-GL / Intel XMM7360.

%prep
%setup -q -c %{name}-master

%files
%doc %{name}-master/README.md

%changelog
{{{ git_dir_changelog }}}
