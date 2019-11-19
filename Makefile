LIBRARIES=stdc++
OBJECTS=$(addprefix build/, $(addsuffix .ll, hello.c hello.cpp hello.rs main.c))

.PHONY: all
all: link

.PHONY: link
link: build
	ld.lld $(shell llvm-config --ldflags) $(addprefix -l, $(LIBRARIES)) -o hello $(OBJECTS)

.PHONY: build
build: builddir $(OBJECTS)

.PHONY: clean
clean:
	rm -rf $(OBJECTS) hello

.PHONY: builddir
builddir:
	mkdir -p build

build/%.cpp.ll: src/%.cpp builddir
	clang -emit-llvm -c -o $@ $<

build/%.rs.ll: src/%.rs builddir
	rustc --crate-type=lib --emit=llvm-bc -o $@ $<

build/%.c.ll: src/%.c builddir
	clang -emit-llvm -c -Iinclude -o $@ $<
