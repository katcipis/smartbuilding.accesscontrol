from PySide.QtUiTools import QUiLoader
from PySide.QtCore import Qt
from PySide.QtGui import QDialog, qRgb, QImage, QPixmap
from gui.get_rfid_dialog import GetRFIDDialog

from database.person import Person
from database.rfid import RFID
import cv, os, numpy

_UI_DIR  = os.path.join(os.getcwd(), 'gui', 'ui')
_UI_PATH = os.path.join(_UI_DIR, "register.ui")


class RegisterDialog():

    def __init__(self):
        loader = QUiLoader()
        self.__ui = loader.load(_UI_PATH)
        self.rfid_lock = False
        self.__ui.is_done.clicked.connect(self.__done)
        self.__ui.get_rfid.clicked.connect(self.__get_rfid)
        self.__ui.discard_photo.clicked.connect(self.__discard_photo)
        self.__ui.add_room.clicked.connect(self.__add_new_allowed_room)
        self.__ui.take_photo.clicked.connect(self.__take_photo)
        

    def show (self, person = None):
        if person:
            self.__ui.person_name.setText(person.getName())
            self.__ui.person_cpf.setText(person.getCPF())

            for room in person.getAllowedRooms():
                self.__ui.allowed_rooms.addItem(str(room))

            for identification in person.getIDs():
                if identification.getType() == RFID.getType():
                    self.__ui.person_rfid.setText(identification.getID())
        
        self.__ui.exec_()


    def rejected(self):
        if self.__ui.result() == QDialog.Rejected:
            return True

        if self.getAddedPerson() == None:
            return True

        return False

    # some magic to convert from opencv to Qt. Don't touch this.
    def __toQImage(self, im):
        gray_color_table = [qRgb(i, i, i) for i in range(256)]
        if im is None:
            return QImage()

        if im.dtype == numpy.uint8:
            if len(im.shape) == 2:
                qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_Indexed8)
                qim.setColorTable(gray_color_table)
                return qim

            elif len(im.shape) == 3:
                if im.shape[2] == 3:
                    qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_RGB888)
                    return qim
                elif im.shape[2] == 4:
                    qim = QImage(im.data, im.shape[1], im.shape[0], im.strides[0], QImage.Format_ARGB32)
                    return qim


    def __cv2array(self, im):
        depth2dtype = {
                        cv.IPL_DEPTH_8U: 'uint8',
                        cv.IPL_DEPTH_8S: 'int8',
                        cv.IPL_DEPTH_16U: 'uint16',
                        cv.IPL_DEPTH_16S: 'int16',
                        cv.IPL_DEPTH_32S: 'int32',
                        cv.IPL_DEPTH_32F: 'float32',
                        cv.IPL_DEPTH_64F: 'float64',
                }

        arrdtype=im.depth
        a = numpy.fromstring(im.tostring(),dtype=depth2dtype[im.depth],count=im.width*im.height*im.nChannels)
        a.shape = (im.height,im.width,im.nChannels)
        return a

    def __webcam(self):
	capture = cv.CaptureFromCAM(-1)	
	for i in range(10):
		frame = cv.QueryFrame(capture)
	if not frame:
		return
	arr = self.__cv2array(frame)
	image = self.__toQImage(arr)
	image = image.rgbSwapped()
	self.__ui.photo_label.setPixmap(QPixmap.fromImage(image).scaled(self.__ui.photo_label.size(),Qt.KeepAspectRatio))

    def __done(self):
        self.__ui.setResult(QDialog.Accepted)
        self.__ui.hide()


    def getAddedPerson(self):
        name = self.__ui.person_name.text()
        if name == '':
            return

        cpf = self.__ui.person_cpf.text()
        if cpf == '':
            return

        person = Person(name, cpf)

        [person.addAllowedRoom(self.__ui.allowed_rooms.item(i).text()) for i in range(self.__ui.allowed_rooms.count())]
        
        if self.__ui.person_rfid.text() != '':
            person.addID(RFID(self.__ui.person_rfid.text()))

        return person

    def __get_rfid(self):
        rfid_dialog = GetRFIDDialog()
        rfid = rfid_dialog.getRFID()
        if rfid != None:
            self.__ui.person_rfid.setText(rfid)

    def __discard_photo(self):
        print "not done yet =)"

    def __add_new_allowed_room (self):
        self.__ui.allowed_rooms.addItem((self.__ui.added_room.text()))

    def __take_photo(self):
        self.__webcam()

    def __set_rfid_text(self, text):
        if not self.rfid_lock:
            self.__ui.centralwidget.person_rfid.setText(text)
