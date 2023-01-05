#include <stdlib.h>

#include "langs.h"

#define NUMBER_OF_LANGUAGES sizeof(ENTRY_POINTS) / sizeof(ENTRY_POINTS[0])
#define NUMBER_OF_RT_FINIS sizeof(RUNTIME_FINIS) / sizeof(RUNTIME_FINIS[0])
#define NUMBER_OF_RT_INITS sizeof(RUNTIME_INITS) / sizeof(RUNTIME_INITS[0])

// Horrible thing I did for Tcl ~Alex
int ARGC;
char **ARGV;

int main(int argc, char *argv[]) {
    // Store argc and argv for later
    ARGC = argc;
    ARGV = argv;
    // Initialize all the runtimes
    for(size_t i = 0; i < NUMBER_OF_RT_INITS; i++) {
        (*RUNTIME_INITS[i])();
    }
    // Prompt every language that has been compiled to say hi
    for(size_t i = 0; i < NUMBER_OF_LANGUAGES; i++) {
        (*ENTRY_POINTS[i])();
    }
    // Clean up all the junk left over from the runtimes that were used
    for(size_t i = 0; i < NUMBER_OF_RT_FINIS; i++) {
        (*RUNTIME_FINIS[i])();
    }
    return 0;
}