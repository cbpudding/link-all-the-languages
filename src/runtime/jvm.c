#include <jni.h>

JNIEnv *env;
JavaVM *vm;

void fini_jvm() {
    (*vm)->DestroyJavaVM(vm);
}

void init_jvm() {
    JavaVMInitArgs args;
    jint res;

    args.version = JNI_VERSION_10;
    args.nOptions = 0;

    res = JNI_CreateJavaVM(&vm, (void **)&env, &args);
    if(res != JNI_OK) {
        fputs("Failed to start JVM!", stderr);
        return;
    }
}