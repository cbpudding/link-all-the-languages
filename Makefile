.PHONY:
run: build/hello
	./build/hello

build/hello: build/librust_hello.a build/hello_cpp.a
	$(CC) src/main.c src/hello.c build/hello_cpp.a build/librust_hello.a -o build/hello -lstdc++
build/librust_hello.a: src/rust-hello/*
	sh -c "cd src/rust-hello &&\
		cargo build --release &&\
		cp target/release/librust_hello.a ../../build/librust_hello.a &&\
		cd ../.."
build/hello_cpp.a: build/hello_cpp.o
	$(AR) rcs build/hello_cpp.a build/hello_cpp.o
build/hello_cpp.o: src/hello.cpp
	$(CXX) -c src/hello.cpp -o build/hello_cpp.o

.PHONY:
clean: clean_rust
	rm -rf build
	mkdir -p build

.PHONY:
clean_rust:
	sh -c "cd src/rust-hello &&\
		cargo clean"
