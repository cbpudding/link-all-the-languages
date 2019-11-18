LIBRARIES=stdc++
OBJECTS=hello_c.o hello_cpp.o hello_rust.so main.o

.PHONY: all
all: link

.PHONY: link
link: build
	gcc $(addprefix -l, $(LIBRARIES)) -o hello $(addprefix build/, $(OBJECTS))

.PHONY: build
build: builddir c cpp rust
	gcc -I include -c -o build/main.o src/main.c

.PHONY: clean
clean:
	rm -rf $(addprefix build/, $(OBJECTS))

.PHONY: builddir
builddir:
	mkdir -p build

.PHONY: c
c: builddir
	gcc -c -o build/hello_c.o src/hello.c

.PHONY: cpp
cpp: builddir
	g++ -c -o build/hello_cpp.o src/hello.cpp

.PHONY: rust
rust: builddir
	rustc -o build/hello_rust.so src/hello.rs
