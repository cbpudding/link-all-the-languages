OBJECTS=hello_rust.so main.o

.PHONY: all
all: link

.PHONY: link
link: build
	gcc -o hello $(addprefix build/, $(OBJECTS))

.PHONY: build
build: builddir rust
	gcc -I include -c -o build/main.o src/main.c

.PHONY: clean
clean:
	rm -rf $(addprefix build/, $(OBJECTS))

.PHONY: builddir
builddir:
	mkdir -p build

.PHONY: rust
rust: builddir
	rustc -o build/hello_rust.so src/hello.rs
