# musl-misc
musl C library miscellaneous

## bits
- **rpm/SPECS/musl-static.spec** : centos/rhel 6 & 7 musl-libc static libs, headers and toolchain wrappers
- **musl-cross-make-confs/Makefile.arch_indep** : musl-cross-make Makefile driver for building a fully-static toolchain

## links
- **musl-libc** : http://www.musl-libc.org/
- **musl-cross-make** : https://github.com/richfelker/musl-cross-make
- **crosware**, where this is used : https://github.com/ryanwoodsmall/crosware

## todo
- integrate off64\_t/loff\_t fixes for gccgo, etc.:
  - https://www.mail-archive.com/gcc-bugs@gcc.gnu.org/msg476845.html
  - http://gcc-patches.gcc.gnu.narkive.com/xkNPk6Vm/libgo-patch-committed-fill-out-syscall-package-for-gnu-linux
  - http://gcc.1065356.n8.nabble.com/libgo-patch-committed-Fill-out-syscall-package-for-GNU-Linux-td491220.html
  - ```-D_LARGEFILE_SOURCE``` and/or ```-D_LARGEFILE64_SOURCE```? ```${OSCFLAGS}```
- split out ld.so patches into multiple arches?
- a fake sysroot is needed (perl and the like can use it)

### bootstrapping
- alpine works fine
  - see apk and bash/curl commands in comments
- crosware
  - need to be able to self-host
    - can't
    - currently dies on compiling shared objects and/in C++ ABI issues
    - libtool? use slibtool
    - need a ```${cwsw}/wget/current/bin/wget --no-check-certificate "${@}"``` wrapper
      - or try busybox wget and relax gnu check?
    - environment...
      - **wget wrapper**
      - libtool -> slibtool symlink
      - ```crosware install statictoolchain git ; crosware update ; crosware install binutils slibtool ; . ${cwtop}/etc/profile```
      - ```env LIBTOOL=slibtool CFLAGS=-fPIC CXXFLAGS=-fPIC LDFLAGS="${LDFLAGS//-static/}" LIBS='-liberty' make -f ~/Makefile.arch_indep```
    - errors ad infinitum
      - gmp
      - mpfr
      - mpc
      - binutils
  - testing on https://github.com/ryanwoodsmall/dockerfiles/tree/master/crosware

#### this doesn't work:

leads to c++ abi issues previously observed (https://github.com/ryanwoodsmall/musl-misc/blob/776f8211b8019e8197ae0e9dcf0b524d29b43d81/README.md)
```
env \
  LD_LIBRARY_PATH="$(echo ${cwsw}/{binutils,gmp,mpc,mpfr}/current/lib | tr ' ' ':')" \
  LIBTOOL=slibtool \
  CFLAGS=-fPIC \
  CXXFLAGS=-fPIC \
  LIBS=-liberty \
  LDFLAGS="${LDFLAGS//-static/}" \
  make -f ~/Makefile.arch_indep >/tmp/musl-cross-make.out 2>&1
```
