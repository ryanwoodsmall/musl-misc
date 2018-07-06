# musl-misc
musl C library miscellaneous

## bits
- **rpm/SPECS/musl-static.spec** : centos/rhel 6 & 7 musl-libc static libs, headers and toolchain wrappers
- **musl-cross-make-confs/Makefile.arch_indep** : musl-cross-make Makefile driver for building a fully-static toolchain

## links
- **musl-libc** : http://www.musl-libc.org/
- **musl-cross-make** : https://github.com/richfelker/musl-cross-make

## todo
- integrate off64\_t/loff\_t fixes for gccgo, etc.:
  - https://www.mail-archive.com/gcc-bugs@gcc.gnu.org/msg476845.html
  - http://gcc-patches.gcc.gnu.narkive.com/xkNPk6Vm/libgo-patch-committed-fill-out-syscall-package-for-gnu-linux
  - http://gcc.1065356.n8.nabble.com/libgo-patch-committed-Fill-out-syscall-package-for-GNU-Linux-td491220.html
  - ```-D_LARGEFILE_SOURCE``` and/or ```-D_LARGEFILE64_SOURCE```? ```${OSCFLAGS}```
- split out ld.so patches into multiple arches?
