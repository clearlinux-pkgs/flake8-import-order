#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flake8-import-order
Version  : 0.18.1
Release  : 25
URL      : https://files.pythonhosted.org/packages/81/47/5f2cea0164e77dd40726d83b4c865c2a701f60b73cb6af7b539cd42aafb4/flake8-import-order-0.18.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/81/47/5f2cea0164e77dd40726d83b4c865c2a701f60b73cb6af7b539cd42aafb4/flake8-import-order-0.18.1.tar.gz
Summary  : Flake8 and pylama plugin that checks the ordering of import statements.
Group    : Development/Tools
License  : LGPL-3.0
Requires: flake8-import-order-license = %{version}-%{release}
Requires: flake8-import-order-python = %{version}-%{release}
Requires: flake8-import-order-python3 = %{version}-%{release}
Requires: pycodestyle
Requires: setuptools
BuildRequires : buildreq-distutils3
BuildRequires : pycodestyle
BuildRequires : setuptools

%description
===================
        
        |Build Status|

%package license
Summary: license components for the flake8-import-order package.
Group: Default

%description license
license components for the flake8-import-order package.


%package python
Summary: python components for the flake8-import-order package.
Group: Default
Requires: flake8-import-order-python3 = %{version}-%{release}

%description python
python components for the flake8-import-order package.


%package python3
Summary: python3 components for the flake8-import-order package.
Group: Default
Requires: python3-core
Provides: pypi(flake8_import_order)
Requires: pypi(pycodestyle)
Requires: pypi(setuptools)

%description python3
python3 components for the flake8-import-order package.


%prep
%setup -q -n flake8-import-order-0.18.1
cd %{_builddir}/flake8-import-order-0.18.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635728326
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/flake8-import-order
cp %{_builddir}/flake8-import-order-0.18.1/COPYING %{buildroot}/usr/share/package-licenses/flake8-import-order/f45ee1c765646813b442ca58de72e20a64a7ddba
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/flake8-import-order/f45ee1c765646813b442ca58de72e20a64a7ddba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
