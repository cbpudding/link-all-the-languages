#include <ruby-3.0.0/ruby.h>
#include <stdlib.h>
#include <string.h>

#include "hello.rb.h"

void hello_ruby() {
    char *buffer = malloc(hello_rb_len + 1);
    int state;
    strncpy(buffer, hello_rb, hello_rb_len);
    buffer[hello_rb_len] = 0;
    ruby_setup();
    rb_eval_string_protect(buffer, &state);
    rb_funcall(rb_vm_top_self(), rb_intern("hello_ruby"), 0, NULL);
    ruby_finalize();
    free(buffer);
}