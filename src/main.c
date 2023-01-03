#include <stdlib.h>

#include "langs.h"

#define NUMBER_OF_LANGUAGES sizeof(ENTRY_POINTS) / sizeof(ENTRY_POINTS[0])

// Horrible thing I did for Tcl ~Alex
int ARGC;
char **ARGV;

int main(int argc, char *argv[]) {
    ARGC = argc;
    ARGV = argv;
    for(size_t i = 0; i < NUMBER_OF_LANGUAGES; i++) {
        (*ENTRY_POINTS[i])();
    }
    return 0;
}