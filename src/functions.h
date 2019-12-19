extern const void hello_c();       // lib.c
extern const void hello_cpp();     // lib.cpp
extern const void hello_d();       // lib.d
extern const void hello_fortran(); // lib.f95
extern const void hello_rust();    // lib.rs
extern const void hello_zig();     // lib.zig
extern const void hello_carp();    // lib.carp

const void (*hello[])() = { hello_c, hello_cpp, hello_d, hello_fortran, hello_rust, hello_zig, hello_carp };
#define NUMBER_OF_LANGUAGES sizeof(hello) / sizeof(hello[0])
