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
- symlinks
  - ```musl-gcc```
  - ```musl-g++```
  - ```musl-ldd``` (```ld.so``` or ```libc.so```, via https://wiki.musl-libc.org/faq.html#Q:-Where-is-%3Ccode%3Eldd%3C/code%3E?)
- a fake sysroot is needed (perl and the like can use it
- need to be able to self-host
  - currently dies on compiling shared objects and/in C++ ABI issues
  - libtool? use slibtool?
  - error ad infinitum
```
libtool: link: x86_64-linux-musl-g++  -fPIC -DPIC -shared -nostdlib /usr/local/crosware/software/statictoolchain/201901150448-x86_64-linux-musl/bin/../lib/gcc/x86_64-linux-musl/6.4.0/../../../../x86_
64-linux-musl/lib/crti.o /usr/local/crosware/software/statictoolchain/201901150448-x86_64-linux-musl/bin/../lib/gcc/x86_64-linux-musl/6.4.0/crtbeginS.o  .libs/findcomp.o .libs/libcc1.o .libs/names.o 
.libs/callbacks.o .libs/connection.o .libs/marshall.o   -L/usr/local/crosware/software/statictoolchain/201901150448-x86_64-linux-musl/bin/../lib/gcc/x86_64-linux-musl/6.4.0 -L/usr/local/crosware/soft
ware/statictoolchain/201901150448-x86_64-linux-musl/bin/../lib/gcc -L/usr/local/crosware/software/statictoolchain/201901150448-x86_64-linux-musl/bin/../lib/gcc/x86_64-linux-musl/6.4.0/../../../../x86
_64-linux-musl/lib -L/usr/local/crosware/software/statictoolchain/201901150448-x86_64-linux-musl/bin/../x86_64-linux-musl/lib /usr/local/crosware/software/statictoolchain/201901150448-x86_64-linux-mu
sl/bin/../lib/gcc/x86_64-linux-musl/6.4.0/../../../../x86_64-linux-musl/lib/libstdc++.a -lm -lc -lgcc /usr/local/crosware/software/statictoolchain/201901150448-x86_64-linux-musl/bin/../lib/gcc/x86_64
-linux-musl/6.4.0/crtendS.o /usr/local/crosware/software/statictoolchain/201901150448-x86_64-linux-musl/bin/../lib/gcc/x86_64-linux-musl/6.4.0/../../../../x86_64-linux-musl/lib/crtn.o  -static-libstd
c++ -static-libgcc ../libiberty/pic/libiberty.a   -Wl,-soname -Wl,libcc1.so.0 -Wl,-retain-symbols-file -Wl,../../src_gcc/libcc1/libcc1.sym -o .libs/libcc1.so.0.0.0
/usr/local/crosware/software/statictoolchain/201901150448-x86_64-linux-musl/bin/../lib/gcc/x86_64-linux-musl/6.4.0/../../../../x86_64-linux-musl/bin/ld: /usr/local/crosware/software/statictoolchain/2
01901150448-x86_64-linux-musl/bin/../lib/gcc/x86_64-linux-musl/6.4.0/../../../../x86_64-linux-musl/lib/libstdc++.a(class_type_info.o): relocation R_X86_64_32S against symbol `_ZTVN10__cxxabiv117__cla
ss_type_infoE' can not be used when making a shared object; recompile with -fPIC
/usr/local/crosware/software/statictoolchain/201901150448-x86_64-linux-musl/bin/../lib/gcc/x86_64-linux-musl/6.4.0/../../../../x86_64-linux-musl/bin/ld: /usr/local/crosware/software/statictoolchain/2
01901150448-x86_64-linux-musl/bin/../lib/gcc/x86_64-linux-musl/6.4.0/../../../../x86_64-linux-musl/lib/libstdc++.a(eh_aux_runtime.o): relocation R_X86_64_32 against symbol `_ZNSt8bad_castD1Ev' can no
t be used when making a shared object; recompile with -fPIC
/usr/local/crosware/software/statictoolchain/201901150448-x86_64-linux-musl/bin/../lib/gcc/x86_64-linux-musl/6.4.0/../../../../x86_64-linux-musl/bin/ld: /usr/local/crosware/software/statictoolchain/2
01901150448-x86_64-linux-musl/bin/../lib/gcc/x86_64-linux-musl/6.4.0/../../../../x86_64-linux-musl/lib/libstdc++.a(eh_globals.o): relocation R_X86_64_TPOFF32 against `_ZZN12_GLOBAL__N_110get_globalEv
E6global' can not be used when making a shared object; recompile with -fPIC
```
