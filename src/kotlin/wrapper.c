#include <jni.h>
#include <stdio.h>

#include "HelloKt.class.h"

extern JNIEnv *env;
extern JavaVM *vm;

void hello_kotlin() {
    jclass class;
    jmethodID method;

    class = (*env)->DefineClass(env, "HelloKt", NULL, (const jbyte *)HelloKt_class, HelloKt_class_len);
    if(class == NULL) {
        fputs("Failed to locate class!", stderr);
        return;
    }

    method = (*env)->GetStaticMethodID(env, class, "hello_kotlin", "()V");
    if(method == NULL) {
        fputs("Failed to locate hello_java function!", stderr);
        return;
    }

    (*env)->CallStaticVoidMethod(env, class, method);
}