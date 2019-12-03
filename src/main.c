#include "functions.h"

const void (*hello[])() = { hello_c, hello_cpp, hello_rust, hello_zig };

#define NUMBER_OF_LANGUAGES sizeof(hello) / sizeof(hello[0])

int main() {
	for(int i = 0; i < NUMBER_OF_LANGUAGES; i++) {
		(*hello[i])();
	}
	return 0;
}
