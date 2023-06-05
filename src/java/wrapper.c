#include <jni.h>
#include <stdio.h>

#include "challenge.h"
#include "jni/Hello.h"
#include "Hello.class.h"

extern JNIEnv *env;
extern JavaVM *vm;

JNIEXPORT jboolean JNICALL Java_Hello_challenge(JNIEnv *env, jclass class, jint c) {
    return (jboolean)challenge((int)c + 5);
}

void hello_java(int c) {
    jclass class;
    jmethodID method;

    class = (*env)->DefineClass(env, "Hello", NULL, (const jbyte *)Hello_class, Hello_class_len);
    if(class == NULL) {
        fputs("hello_java: Failed to locate class!\r\n", stderr);
        return;
    }

    method = (*env)->GetStaticMethodID(env, class, "hello_java", "(I)V");
    if(method == NULL) {
        fputs("hello_java: Failed to locate hello_java function!\r\n", stderr);
        return;
    }

    (*env)->CallStaticIntMethod(env, class, method, (jint)c);
}