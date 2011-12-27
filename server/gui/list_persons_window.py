from PySide.QtUiTools import QUiLoader
from PySide.QtGui import QListWidgetItem

from gui.register_dialog import RegisterDialog
from gui.confirm_dialog import ConfirmDialog
from database.person_dao import PersonDAO
from database.person import Person
from database.cache_coeherence_manager import CacheCoeherenceManager

import os

_UI_DIR = os.path.join(os.getcwd(), 'gui', 'ui')
_UI_PATH   = os.path.join(_UI_DIR, "list-persons.ui")

class ListPersonsWindow():

    def __init__(self):
        loader = QUiLoader()
        self.__ui = loader.load(_UI_PATH)
        self.show = self.__ui.show

        self.__ui.add.clicked.connect(self.__add_handler)
        self.__ui.remove.clicked.connect(self.__remove_handler)
        self.__ui.allowed_persons.itemDoubleClicked.connect(self.__person_double_clicked)

        self.__person_dao = PersonDAO()
        self.__cache = CacheCoeherenceManager()
        self.__refresh()



    def __remove_handler (self):
        person_name = self.__ui.allowed_persons.currentItem().text()
        person_cpf  = self.__ui.allowed_persons.currentItem()._person_cpf
        confirm_del = ConfirmDialog('Remove Person', 'Are you sure you want to remove ' + 
                                    person_name + ', CPF - ' + person_cpf)
        
        if not confirm_del.confirmed():
            return

        person = self.__person_dao.load(person_cpf)
        self.__person_dao.delete(person_cpf)
        self.__update_person_on_devices(person)
        self.__refresh()


    def __person_double_clicked (self, person):
        loaded_person = self.__person_dao.load(person._person_cpf)
        register = RegisterDialog()
        register.show(loaded_person)

        if register.rejected():
            return

        added_person = register.getAddedPerson()

        if person._person_cpf == added_person.getCPF():
            self.__person_dao.update(added_person)
        else:
            #changed CPF, remove the old one
            self.__person_dao.delete(person._person_cpf)
            self.__person_dao.save(added_person)
 
        self.__refresh()


    def __update_person_on_devices(self, person):
        for room in person.getAllowedRooms():
            self.__cache.update(room)

    def __add_handler(self):
        register = RegisterDialog()
        register.show()
 
        if register.rejected():
            return

        person = register.getAddedPerson()
        self.__person_dao.save(person)
        self.__update_person_on_devices(person)
 
        self.__refresh()


    def __refresh(self):
        persons = self.__person_dao.load_all()
        self.__ui.allowed_persons.clear()

        for person in persons:
            person_item = QListWidgetItem(person.getName())
            #we are going to store the cpf on the person object ;-)
            person_item._person_cpf = person.getCPF()
            self.__ui.allowed_persons.addItem(person_item)
