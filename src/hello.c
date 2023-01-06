#include <stdio.h>

#include "challenge.h"

void hello_c(int c) {
    puts("Hello from C!");
    // TODO: Should we do something on success here? ~Alex
    challenge(c + 5);
}