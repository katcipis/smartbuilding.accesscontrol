import dbus
import dbus.mainloop.glib

class RFIDListener():

    def __init__(self, rfid_callback):
        dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
        self.__bus = dbus.SessionBus()
        self.__bus.add_signal_receiver(rfid_callback, 
                                       dbus_interface = 'br.ufsc.AccessControl.RFIDReader',
                                       signal_name = "new_rfid")
