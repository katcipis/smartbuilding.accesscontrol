LOCAL_PATH := $(call my-dir)

include $(CLEAR_VARS)

OPENCV_CAMERA_MODULES:=off
include ~/Desktop/sda1/home/davi/cco/eclipse/OpenCV-2.3.1-android-bin/OpenCV-2.3.1/share/OpenCV/OpenCV.mk

#LOCAL_MODULE    := door_handler
#LOCAL_SRC_FILES := door_handler.c
#LOCAL_LDLIBS +=  -llog -ldl

#include $(BUILD_SHARED_LIBRARY)

#include libusb_jni/Android.mk
include door_handler/Android.mk
