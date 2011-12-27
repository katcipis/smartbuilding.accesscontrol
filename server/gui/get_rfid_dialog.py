from PySide.QtUiTools import QUiLoader
from rfid.rfid_listener import RFIDListener
import os

_UI_DIR = os.path.join(os.getcwd(), 'gui', 'ui')
_UI_PATH   = os.path.join(_UI_DIR, "get_rfid.ui")

class GetRFIDDialog():

    def __init__(self):
        loader = QUiLoader()
        self.__ui = loader.load(_UI_PATH)
        self.__rfid = None
        RFIDListener(self.__rfid_callback)
        self.__ui.exec_()

    def __rfid_callback(self, rfid):
        self.__rfid = rfid
        self.__ui.hide()

    def getRFID(self):
        return self.__rfid
