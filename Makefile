AR?=ar
CC?=clang
CXX?=clang++
LD?=ld.lld

ifeq ($(shell uname),Darwin)
    LDFLAGS := -Wl,-dead_strip -fuse-ld=lld
else
    LDFLAGS := -Wl,--gc-sections -lpthread -ldl -fuse-ld=lld
endif

ZIGFLAGS:=-fPIC --bundle-compiler-rt

.PHONY:
all: target/link-all-languages

.PHONY:
run: target/link-all-languages
	@target/link-all-languages

target/release:
	mkdir -p $@

target/link-all-languages: target/main.o target/release/libhello_rust.a target/release/libhello_cpp.a target/release/libhello_d.a target/release/libhello_c.a target/release/libhello_zig.a target/release/libhello_fortran.a
	$(CC) -o $@ $^ $(LDFLAGS) -lgfortran -lphobos2 -lstdc++

target/release/libhello_rust.a: src/lib.rs Cargo.toml
	cargo build --release --target-dir target

target/release/libhello_cpp.a: src/lib.cpp
	$(CXX) -c $^ -o target/release/libhello_cpp.o
	$(AR) rcs $@ target/release/libhello_cpp.o

target/release/libhello_c.a: src/lib.c
	$(CC) -c $^ -o target/release/libhello_c.o
	$(AR) rcs $@ target/release/libhello_c.o

target/release/libhello_zig.a: src/lib.zig
	zig build-lib $^ --output-dir target/release --name hello_zig $(ZIGFLAGS)

target/release/libhello_fortran.a: src/lib.f95
	gfortran -ffree-form -c $^ -o target/release/libhello_fortran.o
	$(AR) rcs $@ target/release/libhello_fortran.o

target/release/libhello_d.a: src/lib.d
	dmd -c $^ -of=target/release/libhello_d.o
	$(AR) rcs $@ target/release/libhello_d.o

target/main.o: src/main.c | target/release
	$(CC) -o $@ -c $<

.PHONY:
clean:
	@rm -rf target
