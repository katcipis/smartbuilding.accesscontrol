from PySide.QtUiTools import QUiLoader

import os

_UI_DIR = os.path.join(os.getcwd(), 'gui', 'ui')
_UI_PATH   = os.path.join(_UI_DIR, "message.ui")

class MessageDialog():

    def __init__(self, title_detail, message):
        loader = QUiLoader()
        self.__ui = loader.load(_UI_PATH)
        self.__ui.setWindowTitle('Access Control - ' + title_detail)
        self.__ui._message.setText(message)
        self.__ui.exec_()
