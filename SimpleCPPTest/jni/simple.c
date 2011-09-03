#include <string.h>
#include <jni.h>

/* This is a trivial JNI example where we use a native method
 * to return a new VM String. 
 * We are going to learn a lot about the damn JNI :-)
 */
jstring
Java_br_ufsc_lisha_simplecpptest_SimpleCPPTestActivity_stringFromSimple( JNIEnv* env,
                                                                         jobject thiz )
{
    return (*env)->NewStringUTF(env, "Hello world generated on a C shared library :-)");
}
