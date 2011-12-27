from PySide.QtUiTools import QUiLoader
from PySide.QtGui import QDialog
import os

_UI_DIR = os.path.join(os.getcwd(), 'gui', 'ui')
_UI_PATH   = os.path.join(_UI_DIR, "confirm-operation.ui")

class ConfirmDialog():

    def __init__(self, operation_detail, operation):
        loader = QUiLoader()
        self.__ui = loader.load(_UI_PATH)
        self.__ui.setWindowTitle('Access Control - ' + operation_detail)
        self.__ui.operation_text.setText(operation)
        self.__ui.exec_()


    def confirmed(self):
        if self.__ui.result() == QDialog.Rejected:
            return False

        return True
