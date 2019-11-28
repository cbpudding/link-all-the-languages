AR?=ar
CC?=clang
CXX?=clang++

ifeq ($(shell uname),Darwin)
    LDFLAGS := -Wl,-dead_strip
else
    LDFLAGS := -Wl,--gc-sections -lpthread -ldl
endif

ZIGFLAGS:=-fPIC --bundle-compiler-rt

.PHONY:
all: target/link-all-languages
	@printf "\x1b[0;36mRunning...\e[0m\n"
	@target/link-all-languages
	@printf "\e[92mDone\e[0m\n"

.PHONY:
run: target/link-all-languages
	@target/link-all-languages

target:
	@mkdir -p $@

target/link-all-languages: target/main.o target/debug/libhello_rust.a target/debug/libhello_cpp.a target/debug/libhello_c.a target/debug/libhello_zig.a
	@$(CC) -o $@ $^ $(LDFLAGS) -lstdc++

target/debug/libhello_rust.a: src/lib.rs Cargo.toml
	@printf "\x1b[0;36mBuilding $@ ...\e[0m\n"
	@cargo build --target-dir target
	@printf "\e[92mBuilt $@\e[0m\n"

target/debug/libhello_cpp.a: src/lib.cpp
	@printf "\x1b[0;36mBuilding $@ ...\e[0m\n"
	@$(CXX) -c $^ -o target/debug/libhello_cpp.o
	@$(AR) rcs $@ target/debug/libhello_cpp.o
	@printf "\e[92mBuilt $@\e[0m\n"

target/debug/libhello_c.a: src/lib.c
	@printf "\x1b[0;36mBuilding $@ ...\e[0m\n"
	@$(CC) -c $^ -o target/debug/libhello_c.o
	@$(AR) rcs $@ target/debug/libhello_c.o
	@printf "\e[92mBuilt $@\e[0m\n"

target/debug/libhello_zig.a: src/lib.zig
	@printf "\x1b[0;36mBuilding $@ ...\e[0m\n"
	@zig build-lib $^ --output-dir target/debug --name hello_zig $(ZIGFLAGS)
	@printf "\e[92mBuilt $@\e[0m\n"

target/main.o: src/main.c | target
	@printf "\x1b[0;36mBuilding $@ ...\e[0m\n"
	@$(CC) -o $@ -c $<
	@printf "\e[92mBuilt $@\e[0m\n"

.PHONY:
clean:
	@rm -rf target
