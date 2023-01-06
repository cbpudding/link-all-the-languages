#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

#include "langs.h"

#define NUMBER_OF_LANGUAGES sizeof(ENTRY_POINTS) / sizeof(ENTRY_POINTS[0])
#define NUMBER_OF_RT_FINIS sizeof(RUNTIME_FINIS) / sizeof(RUNTIME_FINIS[0])
#define NUMBER_OF_RT_INITS sizeof(RUNTIME_INITS) / sizeof(RUNTIME_INITS[0])

// Horrible thing I did for Tcl ~Alex
int ARGC;
char **ARGV;

int *CURRENT_CHALLENGE;
int SUCCESSFUL;

bool challenge(int challenge) {
    if(challenge == *CURRENT_CHALLENGE + 5) {
        *CURRENT_CHALLENGE = challenge;
        SUCCESSFUL++;
        return true;
    } else {
        return false;
    }
}

int main(int argc, char *argv[]) {
    // Store argc and argv for later
    ARGC = argc;
    ARGV = argv;
    // Let's get the challenge started
    CURRENT_CHALLENGE = malloc(sizeof(CURRENT_CHALLENGE));
    SUCCESSFUL = 0;
    // Initialize all the runtimes
    for(size_t i = 0; i < NUMBER_OF_RT_INITS; i++) {
        (*RUNTIME_INITS[i])();
    }
    // Prompt every language that has been compiled to say hi
    for(size_t i = 0; i < NUMBER_OF_LANGUAGES; i++) {
        (*ENTRY_POINTS[i])(*CURRENT_CHALLENGE);
    }
    // Clean up all the junk left over from the runtimes that were used
    for(size_t i = 0; i < NUMBER_OF_RT_FINIS; i++) {
        (*RUNTIME_FINIS[i])();
    }
    free(CURRENT_CHALLENGE);
    printf("Results: %u/%u languages passed.\r\n", SUCCESSFUL, NUMBER_OF_LANGUAGES);
    return 0;
}