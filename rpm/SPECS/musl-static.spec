%define	spname		musl
%define	musldir		%{_usr}/local/%{spname}
%define	profiled	%{_sysconfdir}/profile.d

Name:		%{spname}-static
Version:	1.1.24
Release:	0%{?dist}
Summary:	musl is a standard C/POSIX library

Group:		Development/Libraries
License:	MIT
URL:		http://www.musl-libc.org/
Source0:	http://www.musl-libc.org/releases/%{spname}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	glibc-static
BuildRequires:	glibc-headers
BuildRequires:	kernel-headers
Requires:	gcc
Requires:	kernel-headers

%description
%{spname} provides a new standard library to power a new generation of
Linux-based devices.  %{spname} is lightweight, fast, simple, free, and strives
to be correct in the sense of standards-conformance and safety.

This package provides compiler wrappers, headers, and static libraries for
%{spname}.


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
  --enable-optimize=no \
  --enable-wrapper=all
make %{?_smp_mflags}


%install
%make_install
# append our bin directory to the path
mkdir -p %{buildroot}%{profiled}
echo 'export PATH="${PATH}:%{musldir}/bin"' > %{buildroot}%{profiled}/%{name}.sh
# symlink in kernel-headers stuff
ln -s /usr/include/asm %{buildroot}%{musldir}/include/
ln -s /usr/include/asm-generic %{buildroot}%{musldir}/include/
ln -s /usr/include/linux %{buildroot}%{musldir}/include/
ln -s /usr/include/mtd %{buildroot}%{musldir}/include/


%files
%{musldir}/bin/*
%{musldir}/lib/lib*.a
%{musldir}/lib/*.o
%{musldir}/lib/*.specs
%{musldir}/include
%{profiled}/%{name}.sh


%changelog
* Sat Oct 26 2019 ryan woodsmall <rwoodsmall@gmail.com> - 1.1.24-0
- musl 1.1.24

* Wed Jul 17 2019 ryan woodsmall <rwoodsmall@gmail.com> - 1.1.23-0
- musl 1.1.23

* Thu Apr 11 2019 ryan woodsmall <rwoodsmall@gmail.com> - 1.1.22-0
- musl 1.1.22

* Tue Jan 22 2019 ryan woodsmall <rwoodsmall@gmail.com> - 1.1.21-0
- musl 1.1.21

* Tue Sep 11 2018 ryan woodsmall <rwoodsmall@gmail.com> - 1.1.20-0
- musl 1.1.20

* Thu Feb 22 2018 ryan woodsmall <rwoodsmall@gmail.com> - 1.1.19-0
- musl 1.1.19

* Wed Nov  1 2017 ryan woodsmall <rwoodsmall@gmail.com> - 1.1.18-0
- musl 1.1.18

* Fri Oct 20 2017 ryan woodsmall <rwoodsmall@gmail.com> - 1.1.17-0
- musl 1.1.17

* Wed Feb  1 2017 ryan woodsmall <rwoodsmall@gmail.com> - 1.1.16-7
- /usr/include/mtd symlink for musl

* Tue Jan 31 2017 ryan woodsmall <rwoodsmall@gmail.com> - 1.1.16-6
- require glibc-headers

* Tue Jan 31 2017 ryan woodsmall <rwoodsmall@gmail.com> - 1.1.16-5
- use %{_sysconfdir} instead of hard-coding /etc

* Tue Jan 31 2017 ryan woodsmall <rwoodsmall@gmail.com> - 1.1.16-4
- disable all optimzations

* Tue Jan 31 2017 ryan woodsmall <rwoodsmall@gmail.com> - 1.1.16-3
- fix description

* Tue Jan 31 2017 ryan woodsmall <rwoodsmall@gmail.com> - 1.1.16-2
- kernel-headers symlinks

* Tue Jan 31 2017 ryan woodsmall <rwoodsmall@gmail.com> - 1.1.16-1
- initial RPM build

* Tue Jan 31 2017 ryan woodsmall <rwoodsmall@gmail.com> - 1.1.16-0
- add profile.d script
