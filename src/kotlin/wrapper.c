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
        fputs("hello_kotlin: Failed to locate class!\r\n", stderr);
        return;
    }

    method = (*env)->GetStaticMethodID(env, class, "hello_kotlin", "()V");
    if(method == NULL) {
        fputs("hello_kotlin: Failed to locate hello_java function!\r\n", stderr);
        return;
    }

    (*env)->CallStaticVoidMethod(env, class, method);
}