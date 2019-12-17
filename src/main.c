#include "functions.h"

int main() {
	for(int i = 0; i < NUMBER_OF_LANGUAGES; i++) {
		(*hello[i])();
	}
	return 0;
}
