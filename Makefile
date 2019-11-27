.PHONY:
run: build/hello
	./build/hello

build/hello: build/librust_hello.a build/hello_cpp.a
	mkdir -p build
	$(CC) src/main.c src/hello.c build/hello_cpp.a build/librust_hello.a -o build/hello -lstdc++
build/librust_hello.a: src/rust-hello/*
	mkdir -p build
	sh -c "cd src/rust-hello &&\
		cargo build --release --target-dir target &&\
		cp target/release/librust_hello.a ../../build/librust_hello.a &&\
		cd ../.."
build/hello_cpp.a: build/hello_cpp.o
	mkdir -p build
	$(AR) rcs build/hello_cpp.a build/hello_cpp.o
build/hello_cpp.o: src/hello.cpp
	mkdir -p build
	$(CXX) -c src/hello.cpp -o build/hello_cpp.o

.PHONY:
clean: clean_rust
	rm -rf build

.PHONY:
clean_rust:
	sh -c "cd src/rust-hello &&\
		cargo clean"
