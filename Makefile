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
	target/link-all-languages

.PHONY:
run: target/link-all-languages
	@target/link-all-languages

target:
	mkdir -p $@

target/link-all-languages: target/main.o target/debug/libhello_rust.a target/debug/libhello_cpp.a target/debug/libhello_c.a target/debug/libhello_zig.a
	$(CC) -o $@ $^ $(LDFLAGS) -lstdc++

target/debug/libhello_rust.a: src/lib.rs Cargo.toml
	cargo build --target-dir target

target/debug/libhello_cpp.a: src/lib.cpp
	$(CXX) -c $^ -o target/debug/libhello_cpp.o
	$(AR) rcs $@ target/debug/libhello_cpp.o

target/debug/libhello_c.a: src/lib.c
	$(CC) -c $^ -o target/debug/libhello_c.o
	$(AR) rcs $@ target/debug/libhello_c.o

target/debug/libhello_zig.a: src/lib.zig
	zig build-lib $^ --output-dir target/debug --name hello_zig $(ZIGFLAGS)

target/main.o: src/main.c | target
	$(CC) -o $@ -c $<

.PHONY:
clean:
	@rm -rf target
