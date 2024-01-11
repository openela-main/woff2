Name:           woff2
Version:        1.0.2
Release:        5%{?dist}
Summary:        Web Open Font Format 2.0 library

License:        MIT
URL:            https://github.com/google/woff2
Source0:        https://github.com/google/woff2/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/google/woff2/pull/121
Patch0:         covscan.patch

BuildRequires:  cmake
BuildRequires:  brotli-devel >= 1.0

%description
Web Open Font Format (WOFF) 2.0 is an update to the existing WOFF 1.0 with
improved compression that is achieved by using the Brotli algorithm. The primary
purpose of the WOFF2 format is to efficiently package fonts linked to Web
documents by means of CSS @font-face rules.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files and utils for %{name}

%prep
%autosetup -p1 -n %{name}-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%cmake .. \
    -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
    -DCMAKE_INSTALL_LIBDIR="%{_libdir}"
popd

make %{?_smp_mflags} -C %{_target_platform}

%install
%make_install -C %{_target_platform}

%files
%license LICENSE
%{_libdir}/libwoff2common.so.*
%{_libdir}/libwoff2dec.so.*
%{_libdir}/libwoff2enc.so.*

%files devel
%{_includedir}/woff2
%{_libdir}/libwoff2common.so
%{_libdir}/libwoff2dec.so
%{_libdir}/libwoff2enc.so
%{_libdir}/pkgconfig/libwoff2common.pc
%{_libdir}/pkgconfig/libwoff2dec.pc
%{_libdir}/pkgconfig/libwoff2enc.pc

%changelog
* Mon Feb 01 2021 Eike Rathke <erack@redhat.com> - 1.0.2-5
- Resolves: rhbz#1919435 bump NVR for rebuild

* Wed Oct 10 2018 Tomas Popela <tpopela@redhat.com> - 1.0.2-4
- Fix Coverity scan issues
- Resolves: rhbz#1637782

* Mon Jul 16 2018 Tomas Popela <tpopela@redhat.com> - 1.0.2-3
- Rebuild for brotli update

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 14 2017 Tomas Popela <tpopela@redhat.com> 1.0.2-1
- Update to 1.0.2

* Mon Oct 09 2017 Tomas Popela <tpopela@redhat.com> 1.0.1-1
- Initial import (rhbz#1499676)
