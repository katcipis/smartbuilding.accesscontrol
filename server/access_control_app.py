#!/usr/bin/env python

from gui.list_persons_window import ListPersonsWindow
from PySide.QtCore import *
from PySide.QtGui import *

if __name__ == '__main__':
	app = QApplication([])
	main_window = ListPersonsWindow()
        main_window.show()
	app.exec_()
