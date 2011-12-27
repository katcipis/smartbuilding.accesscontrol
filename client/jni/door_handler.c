void Java_br_ufsc_identification_RFIDAcquirerService_init(JNIEnv* env, jobject thiz)
{
	system("echo -n a > /dev/ttyUSB0");
	system("echo -n a > /dev/ttyUSB5");
}

void Java_br_ufsc_identification_RFIDAcquirerService_openDoor(JNIEnv* env, jobject thiz)
{
	system("echo -n a > /dev/ttyUSB0");
	system("echo -n a > /dev/ttyUSB5");
}

void Java_br_ufsc_identification_RFIDAcquirerService_closeDoor(JNIEnv* env, jobject thiz)
{
	system("echo -n b > /dev/ttyUSB0");
	system("echo -n b > /dev/ttyUSB5");
}
