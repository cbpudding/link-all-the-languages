#include <stdlib.h>
#include <string.h>
#include <tcl.h>

#include "hello.tcl.h"

extern char *ARGV[];

void hello_tcl_native() {
    unsigned char *buffer = malloc(hello_tcl_len + 1);
    Tcl_Interp *interp;
    Tcl_FindExecutable(ARGV[0]);
    interp = Tcl_CreateInterp();
    if(Tcl_Init(interp) == TCL_OK) {
        strncpy(buffer, (void *)hello_tcl, hello_tcl_len);
        buffer[hello_tcl_len] = 0;
        Tcl_Eval(interp, buffer);
        // TODO: Is there a better way to call the procedure? ~Alex
        Tcl_Eval(interp, "hello_tcl");
        Tcl_Finalize();
    }
    free(buffer);
}