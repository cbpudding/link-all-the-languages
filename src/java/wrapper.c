#include <jni.h>
#include <stdio.h>

#include "Hello.class.h"

extern JNIEnv *env;
extern JavaVM *vm;

void hello_java() {
    jclass class;
    jmethodID method;

    class = (*env)->DefineClass(env, "Hello", NULL, (const jbyte *)Hello_class, Hello_class_len);
    if(class == NULL) {
        fputs("Failed to locate class!", stderr);
        return;
    }

    method = (*env)->GetStaticMethodID(env, class, "hello_java", "()V");
    if(method == NULL) {
        fputs("Failed to locate hello_java function!", stderr);
        return;
    }

    (*env)->CallStaticVoidMethod(env, class, method);
}