# Link All the Languages!

An ongoing project created by Alexander Hill where we link as many programming languages as possible into a single executable.

## Theory

Most programming languages provide a foreign function interface to the C language. Therefore, language X should be able to call functions in language Y and language Y should be able to call functions in language X using the C ABI.

## Languages

### Implemented

- Assembly
- C
- C++
- D
- Fortran
- Go
- Java
- Lua
- Python
- Ruby
- Rust

### In-progress

- C#
- COBOL
- Javascript
- Kotlin
- Pascal
- Perl
- PHP
- Rexx
- Smalltalk

### To-do

- Ada
- Agda
- ALGOL
- Ballerina
- BCPL
- Bosque
- Caml
- Carp
- Clojure
- CoffeeScript
- Common Lisp
- Coq
- Dart
- Elixir
- Erlang
- F#
- Forth
- FreeBasic
- Futhark
- Haskell
- Haxe
- Idris
- Janet
- Julia
- MATLAB
- Mercury
- Nim
- OCaml
- Oz
- R
- Racket
- Raku
- Scheme
- Squirrel
- Swift
- Tcl
- Typescript
- Zig

### Impossible

- Crystal(crystal-lang/crystal#921)

## Rules for including languages

1. Languages must be statically linked
2. Languages must be able to use their standard library
3. Languages must be able to call C and be called by C
4. Languages must be stable(1.0.0 or greater in semantic versioning)