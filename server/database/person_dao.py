'''
Created on 09/10/2011

@author: katcipis
'''
from person import Person
from identification import Identification
from rfid import RFID #We need to import all subclasses from identification, so fromDict works.
from couchdb import ResourceConflict
import couchdb
from cfg import database_cfg 


#Keys used internally
_ID_KEY = '_id'
_NAME_KEY = 'name'
_ALLOWED_ROOMS_KEY = 'allowed-rooms'
_IDENTIFICATIONS_KEY = 'ids'


class PersonDAO(object):
    '''
    Person Data Access Object
    '''
    
    def __init__(self, db=None):
        '''
        Constructor
        @param self: The Person DAO object instance.
        @param db: The database object that will be used by this DAO (Obligatory).
        '''
        if not db:
            server = couchdb.Server(database_cfg.SERVER_URL)
            if database_cfg.PERSON_DATABASE_NAME in server:
                db = server[database_cfg.PERSON_DATABASE_NAME]
            else:
                db = server.create(database_cfg.PERSON_DATABASE_NAME)

        self.__db = db
        

    def __fromPersonToDict(self, person):
        '''
        Converts a Person object to a dict, so it can be saved on the database.
        @param self: The Person DAO object instance.
        @param person: The Person object instance.
        '''
        return {_ID_KEY : person.getCPF(), 
                _NAME_KEY : person.getName(),
                _ALLOWED_ROOMS_KEY : list(person.getAllowedRooms()),
                _IDENTIFICATIONS_KEY : [_id.toDict() for _id in person.getIDs()]
               }

        
    def save (self, person):
        '''
        Persist a Person object on the database.
        @param self: The Person DAO object instance.
        @param person: The Person object instance.
        @return: True on success, False if there is already a person with the same CPF.
        '''
        try:
            self.__db.save(self.__fromPersonToDict(person))
        except ResourceConflict:
            return False
        
        return True

    
    def update (self, person):
        '''
        Updates a Person object on the database.
        All data about this Person will be replaced by the new data.
        @param self: The Person DAO object instance.
        @param person: The Person object instance.
        @return: True on success, False if the CPF of the Person is not found.
        '''
        if self.delete(person.getCPF()):
            return self.save(person)
         
        return False
        

    def load_all (self):
        '''
        Get all Persons from the database.
        @param self: The Person DAO object instance.
        @return: A list with all Persons stored on this database.
        '''
        return [self.load(cpf) for cpf in self.__db]


    def delete (self, cpf):
        '''
        Delete a Person from the database based on its cpf.
        @param self: The Person DAO object instance.
        @param cpf: The cpf.
        @return: True on success, False if there is no one with this cpf.
        '''
        if cpf in self.__db:
            self.__db.delete(self.__db[cpf])
            return True

        return False


    def load (self, cpf):
        '''
        Get a Person from the database based on its cpf.
        @param self: The Person DAO object instance.
        @param cpf: The cpf.
        @return: The Person object instance or None if no Person with this CPF is found.
        '''
        if cpf in self.__db:
            person_data = self.__db[cpf]
            person_obj = Person (person_data[_NAME_KEY], person_data.id)
            [person_obj.addAllowedRoom(room) for room in person_data[_ALLOWED_ROOMS_KEY]]
            
            for id_data in person_data[_IDENTIFICATIONS_KEY]:
                id_obj = Identification.fromDict(id_data)
                person_obj.addID(id_obj)
                
            return person_obj
        
        return None

