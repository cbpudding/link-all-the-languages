# Link All the Languages!

An ongoing project created by Alexander Hill where we link as many programming languages as possible into a single executable.

## Theory

Most programming languages provide a foreign function interface to the C language. Therefore, language X should be able to call functions in language Y and language Y should be able to call functions in language X using the C ABI.

## Languages

### Tier 3 (Statically linked and fully interoperable)

- Assembly
- C
- Zig

### Tier 2 (Can call C and be called by C)

- C++
- D
- Lua
- Rust

### Tier 1 (Can be called by C)

- Fortran
- Go
- Java
- Kotlin
- Python
- Rexx
- Ruby
- Tcl

### To-do

- Ada
- Agda
- ALGOL
- APL
- B
- Ballerina
- BCPL
- Boo
- Bosque
- C#
- C--
- Caml
- Carbon
- Carp
- Clojure
- COBOL
- CoffeeScript
- Common Lisp
- Coq
- Dart
- Eiffel
- Elixir
- Erlang
- F
- F#
- Forth
- FreeBasic
- Futhark
- Groovy
- Hack
- Haskell
- Haxe
- Hy
- Idris
- Janet
- Javascript
- Julia
- MATLAB
- Mercury
- Modula-3
- Nim
- OCaml
- Oz
- Pascal
- Perl
- PL/I
- PHP
- PowerShell
- Prolog
- R
- Racket
- Raku
- Ratfor
- RPG
- Scala
- Scheme
- Smalltalk
- Squirrel
- Swift
- Typescript
- Unison
- Zig

### Impossible

- Crystal(crystal-lang/crystal#921)

## Rules for including languages

1. Languages must be statically linked
2. Languages must be able to use their standard library
3. Languages must be able to call C and be called by C
4. Languages must be stable(1.0.0 or greater in semantic versioning)
