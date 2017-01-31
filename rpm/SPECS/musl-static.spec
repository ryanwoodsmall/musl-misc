%define	spname		musl
%define	musldir		%{_usr}/local/%{spname}
%define	profiled	/etc/profile.d

Name:		%{spname}-static
Version:	1.1.16
Release:	1%{?dist}
Summary:	musl is a standard C/POSIX library

Group:		Development/Libraries
License:	MIT
URL:		http://www.musl-libc.org/
Source0:	http://www.musl-libc.org/releases/%{spname}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	glibc-static
Requires:	gcc

%description
%{spname} provides a new standard library to power a new generation of
Linux-based devices.  %{spname} is lightweight, fast, simple, free, and strives
to be correct in the sense of standards-conformance and safety.

This package provides compiler wrappers and static libraries for %{spname}.


%prep
%setup -q -n %{spname}-%{version}


%build
./configure \
  --prefix=%{musldir} \
  --enable-debug \
  --enable-warnings \
  --enable-visibility \
  --disable-shared \
  --enable-static \
  --enable-wrapper=all
make %{?_smp_mflags}


%install
%make_install
mkdir -p %{buildroot}%{profiled}
echo 'export PATH="${PATH}:%{musldir}/bin"' > %{buildroot}%{profiled}/%{name}.sh


%files
%{musldir}/bin/*
%{musldir}/lib/lib*.a
%{musldir}/lib/*.o
%{musldir}/lib/*.specs
%{musldir}/include
%{profiled}/%{name}.sh


%changelog
* Tue Jan 31 2017 ryan woodsmall <rwoodsmall@gmail.com> - 1.16.1-1
- initial RPM build
- add profile.d script
