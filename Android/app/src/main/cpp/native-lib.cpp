#include <jni.h>
#include <string>

extern "C" JNIEXPORT jstring JNICALL
Java_com_dictalearn_app_MainActivity_stringFromJNI(
        JNIEnv* env,
        jobject /* this */) {
    std::string message = "DictaLearn Native C++ Engine Ready";
    return env->NewStringUTF(message.c_str());
}
