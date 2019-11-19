CC=clang
CXX=clang
LD=ld.lld
RUST=rustc

CFLAGS=$(shell llvm-config --cflags) -emit-llvm -Iinclude
CXXFLAGS=$(shell llvm-config --cxxflags) -emit-llvm
LDFLAGS=$(shell llvm-config --ldflags)
RUSTFLAGS=--crate-type=lib --emit=llvm-bc

LDLIBS=stdc++
OBJECTS=$(addprefix build/, $(addsuffix .ll, hello.c hello.cpp hello.rs main.c))

.PHONY: all
all: link

.PHONY: link
link: build
	$(LD) $(LDFLAGS) $(addprefix -l, $(LDLIBS)) -o hello $(OBJECTS)

.PHONY: build
build: build/ $(OBJECTS)

.PHONY: clean
clean:
	$(RM) $(OBJECTS) hello

build/:
	mkdir -p build

build/%.cpp.ll: src/%.cpp build/
	$(CXX) $(CXXFLAGS) -c -o $@ $<

build/%.rs.ll: src/%.rs build/
	$(RUST) $(RUSTFLAGS) -o $@ $<

build/%.c.ll: src/%.c build/
	$(CC) $(CFLAGS) -c -o $@ $<
