#include <python3.11/Python.h>
#include <stdlib.h>
#include <string.h>

#include "hello.py.h"

void hello_python() {
    PyObject *args, *func, *main;
    char *buffer = malloc(hello_py_len + 1);
    strncpy(buffer, hello_py, hello_py_len);
    buffer[hello_py_len] = 0;
    Py_Initialize();
    PyRun_SimpleString(buffer);
    main = PyImport_AddModule("__main__");
    func = PyObject_GetAttrString(main, "hello_python");
    args = PyTuple_New(0);
    PyObject_Call(func, args, NULL);
    Py_FinalizeEx();
    free(buffer);
}