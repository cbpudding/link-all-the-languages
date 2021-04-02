#include <stdlib.h>

#include "langs.h"

#define NUMBER_OF_LANGUAGES sizeof(ENTRY_POINTS) / sizeof(ENTRY_POINTS[0])

int main(int argc, char *argv[]) {
    for(size_t i = 0; i < NUMBER_OF_LANGUAGES; i++) {
        (*ENTRY_POINTS[i])();
    }
    return 0;
}