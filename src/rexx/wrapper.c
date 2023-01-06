#include <rexxsaa.h>
#include <stddef.h>
#include <stdio.h>

#include "hello.rex.h"

void hello_rexx() {
    RXSTRING instore[2];
    // Populate instore
    MAKERXSTRING(instore[0], hello_rex, hello_rex_len);
    MAKERXSTRING(instore[1], NULL, 0);
    // Execute our code with the Rexx interpreter
    RexxStart(0, NULL, "hello.rex", instore, NULL, RXCOMMAND, NULL, NULL, NULL);
}