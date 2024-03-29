# musl-misc
musl C library miscellaneous

## bits
- **rpm/SPECS/musl-static.spec** : centos/rhel 6 & 7 musl-libc static libs, headers and toolchain wrappers
- **musl-cross-make-confs/Makefile.arch_indep** : musl-cross-make Makefile driver for building a fully-static toolchain

## links
- **musl-libc** : http://www.musl-libc.org/
- **musl-cross-make** : https://github.com/richfelker/musl-cross-make
- **crosware**, where this is used : https://github.com/ryanwoodsmall/crosware

## docker dockerfiles/scripts/resources
- musl static lib rpm: https://github.com/ryanwoodsmall/dockerfiles/tree/master/centos-rpm-builds
- crosware static toolchain builder: https://github.com/ryanwoodsmall/dockerfiles/tree/master/crosware/statictoolchain
- docker container: https://hub.docker.com/r/ryanwoodsmall/crosware

## todo
- XXX - move to either a .gz (everywhere) or an .xz (maybe not everywhere) archive
- XXX - 9cc 9.5.0 + musl 1.2.3 is the end of line for 9, need to figure out 10/11/12
- XXX - gcc 9.4 + musl 1.2.2 seems to break openssh+libressl
  - related to mallocng?
  - 1.2.0 and 1.2.1 w/`--with-malloc=oldmalloc` in `MUSL_CONFIG` seems to work
  - 1.2.2 doesn't want to build with `--with-malloc=oldmalloc`
- XXX - gcc 10 enables `-fno-common` by default, needs multiple workarounds
- XXX - gcc 10 conflicts with crosware binutils, libiberty or similar, need to figure out
- crank up default stack size? from habitat core/musl (default 80KB -> 2MB?):
  - `sed -i 's/#define DEFAULT_STACK_SIZE .*/#define DEFAULT_STACK_SIZE 2097152/' src/internal/pthread_impl.h`
- `--enable-new-dtags` - RUNPATH instead of RPATH
- need gnu patch, should test for it
- **riscv64** kernel headers not included... need to fix (make general for non intel/arm)
- integrate off64\_t/loff\_t fixes for gccgo, etc.:
  - https://www.mail-archive.com/gcc-bugs@gcc.gnu.org/msg476845.html
  - http://gcc-patches.gcc.gnu.narkive.com/xkNPk6Vm/libgo-patch-committed-fill-out-syscall-package-for-gnu-linux
  - http://gcc.1065356.n8.nabble.com/libgo-patch-committed-Fill-out-syscall-package-for-GNU-Linux-td491220.html
  - ```-D_LARGEFILE_SOURCE``` and/or ```-D_LARGEFILE64_SOURCE```? ```${OSCFLAGS}```
- split out ld.so patches into multiple arches?
- a fake sysroot is needed (perl and the like can use it)
- utmp/wtmp, i.e:
```
/usr/local/crosware/software/statictoolchain/current/x86_64-linux-musl/include/utmp.h:#define _PATH_UTMP "/dev/null/utmp"
/usr/local/crosware/software/statictoolchain/current/x86_64-linux-musl/include/utmp.h:#define _PATH_WTMP "/dev/null/wtmp"
/usr/local/crosware/software/statictoolchain/current/x86_64-linux-musl/include/paths.h:#define _PATH_UTMP       "/dev/null/utmp"
/usr/local/crosware/software/statictoolchain/current/x86_64-linux-musl/include/paths.h:#define _PATH_WTMP       "/dev/null/wtmp"
```

### bootstrapping
- alpine works fine
  - see apk and bash/curl commands in comments
- crosware
  - need to be able to self-host
  - need a ```${cwsw}/wget/current/bin/wget --no-check-certificate "${@}"``` wrapper
    - or try busybox wget and relax gnu check?
  - environment...
    - **wget wrapper**
    - ```crosware install statictoolchain git ; crosware update ; crosware install binutils slibtool ; . ${cwtop}/etc/profile```

### alpine options

```
--enable-checking=release
--disable-fixed-point
--disable-libstdcxx-pch
--disable-multilib
--disable-nls
--disable-werror
--disable-symvers
--enable-__cxa_atexit
--enable-default-pie
--enable-default-ssp
--enable-cloog-backend
--enable-languages=c,c++,d,objc,go,fortran,ada
--disable-libssp
--disable-libmpx
--disable-libmudflap
--disable-libsanitizer
--enable-shared
--enable-threads
--enable-tls
--with-system-zlib
--with-linker-hash-style=gnu
```

#### this doesn't work:::

**OLD**

- libtool? use slibtool
- errors ad infinitum
  - gmp (fixed)
  - mpfr (fixed)
  - mpc (fixed)
  - binutils (fixed)
- libtool -> slibtool symlink
- currently dies on compiling shared objects and/in C++ ABI issues
- this gets through a shared build:
  - ```LIBTOOL=slibtool CFLAGS=-fPIC CXXFLAGS=-fPIC LIBS="-L${cwsw}/binutils/current/lib/ -liberty" LDFLAGS="${LDFLAGS} -s --static" make -f ~/Makefile.arch_indep```
  - but flakes out with c++/abi diffs again'
  - shared vs static vs host-shared?
  - tinkering with ```COMMON_CONFIG="--build=$(gcc -dumpmachine) --target=$(gcc -dumpmachine) --host=$(gcc -dumpmachine)"```
  - musl-cross-make sets target, may override or ignore build/host
- nope ```env LIBTOOL=slibtool CFLAGS=-fPIC CXXFLAGS=-fPIC LDFLAGS="${LDFLAGS//-static/}" LIBS='-liberty' make -f ~/Makefile.arch_indep```
- huh uh? ```env LIBTOOL=slibtool CFLAGS=-fPIC CXXFLAGS=-fPIC LIBS="-L${cwsw}/binutils/current/lib/ -liberty" LDFLAGS="${LDFLAGS} -s --static" make -f ~/Makefile.arch_indep  ) ) >/tmp/musl-cross-make.out 2>&1```
- leads to c++ abi issues previously observed (https://github.com/ryanwoodsmall/musl-misc/blob/776f8211b8019e8197ae0e9dcf0b524d29b43d81/README.md)
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
