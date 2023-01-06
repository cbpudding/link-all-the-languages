#include <stdbool.h>
#include <stdio.h>

extern bool challenge(int c);

void hello_c(int c) {
    puts("Hello from C!");
    // TODO: Should we do something on success here? ~Alex
    challenge(c + 5);
}