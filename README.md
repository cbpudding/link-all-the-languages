# Link All The Languages!
-------------------------

A big bundle of different languages all being invoked from a C program.

## Why?

We want to see if we can!

The idea here is that if we can link all these languages into C,
we can link them in any order with or without C.

## Getting Started
This project has two build systems:
 - A GNU Makefile
 - A custom Python 3 script

### GNU Make
If you choose to use the GNU Makefile, you must install all of the language toolchains (listed below)
used in this project.
```sh
git clone https://github.com/cbpudding/link-all-the-languages
cd link-all-the-languages
make run
```
[Note that we plan to deprecate this build method.](https://github.com/cbpudding/link-all-the-languages/issues/13)


### Python Build
If you choose to use the Python 3 script, you only need to ensure you have the toolchains for the
languages you want to try on your machine. This method still requires a C toolchain.
```sh
git clone https://github.com/cbpudding/link-all-the-languages
cd link-all-the-languages
./run.sh
```

## Languages Used (so far)
 - [C](https://en.wikipedia.org/wiki/C_(programming_language))
 - [C++](https://isocpp.org/)
 - [Carp](https://github.com/carp-lang/Carp)
 - [D (DMD)](https://dlang.org/)
 - [Nim](https://nim-lang.org/)
 - [Rust (Cargo)](https://www.rust-lang.org/)
 - [Fortran (GNU)](https://gcc.gnu.org/fortran/)
 - [Zig](https://ziglang.org/)
