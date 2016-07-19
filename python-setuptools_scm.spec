%global srcname setuptools_scm
%global sum The blessed package to manage your versions by scm tags

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{srcname}
Version:        1.15.6
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            http://pypi.python.org/pypi/%{srcname}
Source0:        https://pypi.io/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.bz2

BuildArch:      noarch
# For tests
BuildRequires:  git-core
BuildRequires:  mercurial

%description
Setuptools_scm handles managing your python package versions in scm metadata.
It also handles file finders for the suppertes scms.

%package -n python2-%{srcname}
Summary:        %{sum}
BuildRequires:  python2-devel
BuildRequires:  pytest
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Setuptools_scm handles managing your python package versions in scm metadata.
It also handles file finders for the suppertes scms.


%if 0%{?with_python3}
%package -n python3-%{srcname}
Summary:        %{sum}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Setuptools_scm handles managing your python package versions in scm metadata.
It also handles file finders for the suppertes scms.
%endif


%prep
%autosetup -n %{srcname}-%{version}

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
# Must do the python2 install first because the scripts in /usr/bin are
# overwritten with every setup.py install, and in general we want the
# python3 version to be the default.
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

%check
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} -vv
%if 0%{?with_python3}
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -vv
# Cleanup stray .pyc files from running python in python3 tests
rm %{buildroot}%{python3_sitelib}/%{srcname}/*.pyc
%endif

%files -n python2-%{srcname}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python2_sitelib}/*

%if 0%{?with_python3}
%files -n python3-%{srcname}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python3_sitelib}/*
%endif


%changelog
* Thu Jun 15 2017 Orion Poplawski <orion@cora.nwra.com> - 1.15.6-1
- Update to 1.15.6

* Mon Apr 10 2017 Orion Poplawski <orion@cora.nwra.com> - 1.15.5-1
- Update to 1.15.5

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 04 2017 Kevin Fenzi <kevin@scrye.com> - 1.15.0-1
- Update to 1.15.0

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 1.13.0-2
- Rebuild for Python 3.6

* Mon Oct 10 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.13.0-1
- Update to 1.13.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 4 2016 Orion Poplawski <orion@cora.nwra.com> - 1.10.1-2
- No python2 package on EPEL (setuptools too old)

* Thu Dec 17 2015 Orion Poplawski <orion@cora.nwra.com> - 1.10.1-1
- Update to 1.10.1

* Wed Dec 2 2015 Orion Poplawski <orion@cora.nwra.com> - 1.9.0-1
- Update to 1.9.0

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Oct 19 2015 Orion Poplawski <orion@cora.nwra.com> - 1.8.0-2
- Cleanup stray .pyc files from tests

* Sat Sep 19 2015 Orion Poplawski <orion@cora.nwra.com> - 1.8.0-1
- Update to 1.8.0
- Fix license tag

* Mon Sep 14 2015 Orion Poplawski <orion@cora.nwra.com> - 1.7.0-1
- Initial package
