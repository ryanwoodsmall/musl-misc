# musl-misc
musl C library miscellaneous

## bits
- **rpm/SPECS/musl-static.spec** : centos/rhel 6 & 7 musl-libc static libs, headers and toolchain wrappers
- **musl-cross-make-confs/Makefile.arch_indep** : musl-cross-make Makefile driver for building a fully-static toolchain

## links
- **musl-libc** : http://www.musl-libc.org/
- **musl-cross-make** : https://github.com/richfelker/musl-cross-make

## todo
- new musl-cross-make build
- integrate off64\_t/loff\_t fixes for gccgo, etc.:
  - https://www.mail-archive.com/gcc-bugs@gcc.gnu.org/msg476845.html
  - http://gcc-patches.gcc.gnu.narkive.com/xkNPk6Vm/libgo-patch-committed-fill-out-syscall-package-for-gnu-linux
  - http://gcc.1065356.n8.nabble.com/libgo-patch-committed-Fill-out-syscall-package-for-GNU-Linux-td491220.html
  - ```-D_LARGEFILE_SOURCE``` and/or ```-D_LARGEFILE64_SOURCE```? ```${OSCFLAGS}```
- split out ld.so patch into multiple arches?
- binutils needs a patch to set ```ELF(|(32|64))_DYNAMIC_INTERPRETER``` (found via compiling **jed** and getting an ELF dynamic bin with ```/lib/ld64.so.1``` as its interp):
```
binutils-2.27 $ egrep -Hr '#define.*DYNAMIC_INTERPRETER.*/(lib|ld).*\.so' | sort
bfd/elf32-arc.c:#define ELF_DYNAMIC_INTERPRETER  "/sbin/ld-uClibc.so"
bfd/elf32-arm.c:#define ELF_DYNAMIC_INTERPRETER     "/usr/lib/ld.so.1"
bfd/elf32-bfin.c:#define ELF_DYNAMIC_INTERPRETER "/lib/ld.so.1"
bfd/elf32-cris.c:#define ELF_DYNAMIC_INTERPRETER "/lib/ld.so.1"
bfd/elf32-frv.c:#define ELF_DYNAMIC_INTERPRETER "/lib/ld.so.1"
bfd/elf32-hppa.c:#define ELF_DYNAMIC_INTERPRETER "/lib/ld.so.1"
bfd/elf32-i370.c:#define ELF_DYNAMIC_INTERPRETER "/lib/ld.so"
bfd/elf32-i386.c:#define ELF_DYNAMIC_INTERPRETER "/usr/lib/libc.so.1"
bfd/elf32-lm32.c:#define ELF_DYNAMIC_INTERPRETER "/usr/lib/libc.so.1"
bfd/elf32-m32r.c:#define ELF_DYNAMIC_INTERPRETER "/usr/lib/libc.so.1"
bfd/elf32-m68k.c:#define ELF_DYNAMIC_INTERPRETER "/usr/lib/libc.so.1"
bfd/elf32-metag.c:#define ELF_DYNAMIC_INTERPRETER "/lib/ld-uClibc.so.0"
bfd/elf32-nds32.c:#define ELF_DYNAMIC_INTERPRETER "/usr/lib/ld.so.1"
bfd/elf32-nios2.c:#define ELF_DYNAMIC_INTERPRETER "/lib/ld.so.1"
bfd/elf32-or1k.c:#define ELF_DYNAMIC_INTERPRETER "/usr/lib/ld.so.1"
bfd/elf32-ppc.c:#define ELF_DYNAMIC_INTERPRETER "/usr/lib/ld.so.1"
bfd/elf32-s390.c:#define ELF_DYNAMIC_INTERPRETER "/lib/ld.so.1"
bfd/elf32-score7.c:#define ELF_DYNAMIC_INTERPRETER              "/usr/lib/ld.so.1"
bfd/elf32-score.c:#define ELF_DYNAMIC_INTERPRETER     "/usr/lib/ld.so.1"
bfd/elf32-sh.c:#define ELF_DYNAMIC_INTERPRETER "/usr/lib/libc.so.1"
bfd/elf32-tic6x.c:#define ELF_DYNAMIC_INTERPRETER "/lib/ld-uClibc.so.0"
bfd/elf32-tilepro.c:#define ELF32_DYNAMIC_INTERPRETER "/lib/ld.so.1"
bfd/elf32-xtensa.c:#define ELF_DYNAMIC_INTERPRETER "/lib/ld.so"
bfd/elf64-alpha.c:#define ELF_DYNAMIC_INTERPRETER "/usr/lib/ld.so"
bfd/elf64-ppc.c:#define ELF_DYNAMIC_INTERPRETER "/usr/lib/ld.so.1"
bfd/elf64-s390.c:#define ELF_DYNAMIC_INTERPRETER "/lib/ld64.so.1"
bfd/elf64-sh64.c:#define ELF_DYNAMIC_INTERPRETER "/usr/lib/libc.so.1"
bfd/elf64-x86-64.c:#define ELF32_DYNAMIC_INTERPRETER "/lib/ldx32.so.1"
bfd/elf64-x86-64.c:#define ELF64_DYNAMIC_INTERPRETER "/lib/ld64.so.1"
bfd/elf-m10300.c:#define ELF_DYNAMIC_INTERPRETER "/lib/ld.so.1"
bfd/elfnn-aarch64.c:#define ELF_DYNAMIC_INTERPRETER     "/lib/ld.so.1"
bfd/elfnn-ia64.c:#define ELF_DYNAMIC_INTERPRETER "/usr/lib/ld.so.1"
bfd/elfxx-sparc.c:#define ELF32_DYNAMIC_INTERPRETER "/usr/lib/ld.so.1"
bfd/elfxx-sparc.c:#define ELF64_DYNAMIC_INTERPRETER "/usr/lib/sparcv9/ld.so.1"
bfd/elfxx-tilegx.c:#define ELF32_DYNAMIC_INTERPRETER "/lib32/ld.so.1"
bfd/elfxx-tilegx.c:#define ELF64_DYNAMIC_INTERPRETER "/lib/ld.so.1"
```
