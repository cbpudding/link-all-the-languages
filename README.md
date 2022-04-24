# Link All the Languages!

An ongoing project created by Alexander Hill where we link as many programming languages as possible into a single executable.

## Theory

Most programming languages provide a foreign function interface to the C language. Therefore, language X should be able to call functions in language Y and language Y should be able to call functions in language X using the C ABI.

## Languages

### Implemented

- C
- C++
- D
- Fortran
- Go
- Lua
- Rust

### In-progress

- Crystal
- Java
- Pascal

### To Do

- Assembly
- C#
- Carp
- COBOL
- Common Lisp
- Dart
- Elixir
- Erlang
- F#
- Forth
- FreeBasic
- Futhark
- Haskell
- Idris
- Janet
- Javascript
- Julia
- Kotlin
- Nim
- OCaml
- Python
- R
- Ruby
- Scheme
- Smalltalk
- Swift
- Tcl
- Typescript
- Zig

### Impossible

*Haven't found anything yet*

## Rules for including languages

1. Languages must be statically linked
2. Languages must be able to use their standard library
3. Languages must be able to call C and be called by C
4. Languages must be stable(1.0.0 or greater in semantic versioning)