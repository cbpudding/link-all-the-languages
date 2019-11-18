#include <functions.h>

const void (*hello[])(void) = {hello_c, hello_cpp, hello_rust};

#define NUMBER_OF_LANGUAGES sizeof(hello) / sizeof(hello[0])

void main() {
	for(int i = 0; i < NUMBER_OF_LANGUAGES; i++) {
		(*hello[i])();
	}
}
