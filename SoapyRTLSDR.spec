Name:           SoapyRTLSDR
Version:	%{VERSION}
Release:        1%{?dist}
Summary:        SoapySDR RTL-SDR Support Module
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/pothosware/SoapyRTLSDR
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:	rtl-sdr-devel
BuildRequires:	SoapySDR-devel

%description
SoapySDR RTL-SDR Support Module

%prep
%setup -n %{name}-soapy-rtlsdr-%{version}

%build
mkdir build
cmake3 . -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE.txt README.md
%{_libdir}/SoapySDR/modules*/librtlsdrSupport.so

%changelog

