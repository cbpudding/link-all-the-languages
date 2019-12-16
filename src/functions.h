extern const void hello_c();       // lib.c
extern const void hello_cpp();     // lib.cpp
extern const void hello_fortran(); // lib.f95
extern const void hello_rust();    // lib.rs
extern const void hello_zig();     // lib.zig

const void (*hello[])() = { hello_c, hello_cpp, hello_fortran, hello_rust, hello_zig };
#define NUMBER_OF_LANGUAGES sizeof(hello) / sizeof(hello[0])
