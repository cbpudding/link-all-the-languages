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

LANGUAGES:=c cpp d fortran rust zig carp

OBJECTS:=$(addsuffix .a, $(addprefix target/release/libhello_, $(LANGUAGES)))

.PHONY:
all: target/link-all-languages

.PHONY:
clean:
	@rm -rf target

.PHONY:
run: target/link-all-languages
	@target/link-all-languages

target/link-all-languages: target/main.o $(OBJECTS)
	$(CC) -Os -march=native -o $@ $^ $(LDFLAGS) -lgfortran -lphobos2 -lstdc++ -lm

target/main.o: src/main.c | target/release
	$(CC) -Os -march=native -o $@ -c $<

target/release:
	mkdir -p $@

target/release/libhello_c.a: src/lib.c
	$(CC) -Os -march=native -mtune=native -c $^ -o target/release/libhello_c.o
	$(AR) rcs $@ target/release/libhello_c.o

target/release/libhello_cpp.a: src/lib.cpp
	$(CXX) -Os -march=native -mtune=native -c $^ -o target/release/libhello_cpp.o
	$(AR) rcs $@ target/release/libhello_cpp.o

target/release/libhello_carp.a: src/lib.carp
	carp -b --generate-only src/lib.carp
	$(CC) -I $(CARP_DIR)/core -c out/main.c -o target/release/libhello_carp.o
	rm -r out
	$(AR) rcs target/release/libhello_carp.a target/release/libhello_carp.o

target/release/libhello_d.a: src/lib.d
	dmd -O -release -c $^ -of=target/release/libhello_d.o
	$(AR) rcs $@ target/release/libhello_d.o

target/release/libhello_fortran.a: src/lib.f95
	gfortran -Os -march=native -mtune=native -ffree-form -c $^ -o target/release/libhello_fortran.o
	$(AR) rcs $@ target/release/libhello_fortran.o

target/release/libhello_rust.a: src/lib.rs Cargo.toml
	cargo build --release --target-dir target

target/release/libhello_zig.a: src/lib.zig
	zig build-lib $^ --output-dir target/release --name hello_zig $(ZIGFLAGS)
