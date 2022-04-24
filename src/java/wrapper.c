#include <jni.h>
#include <stdio.h>

#include "Hello.class.h"

void hello_java() {
    JavaVM *vm;
    JNIEnv *env;
    JavaVMInitArgs args;
    jint res;
    jclass class;
    jmethodID method;

    args.version = JNI_VERSION_10;
    args.nOptions = 0;

    res = JNI_CreateJavaVM(&vm, (void **)&env, &args);
    if(res != JNI_OK) {
        fputs("Failed to start JVM!", stderr);
        return;
    }

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

    (*vm)->DestroyJavaVM(vm);
}