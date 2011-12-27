'''
Created on 01/10/2011
@author: katcipis
'''

class PersonConstructionError(Exception):
    '''
    Simple exception that is raised when a Person 
    is created with invalid parameters.
    '''

    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self):
        return repr(self.error_msg)



class Person(object):
    '''
    Holds all information about a Person on the context of access control.
    '''

    def __init__(self, name, cpf):
        '''
        Constructor.
        @param self: The Person object instance.
        @param name: The person name (Obligatory).
        @param cpf: The person CPF (Obligatory).
        '''
        
        if name == '' or name == None:
            raise PersonConstructionError('Invalid name, it must be a not empty string')

        if cpf == '' or cpf == None:
            raise PersonConstructionError('Invalid cpf, it must be a not empty string')

        self.__name = name
        self.__cpf = cpf
        self.__ids = set()
        self.__rooms = set()
    
        
    def getName (self):
        '''
        Get the person name.
        @param self: The Person object instance.
        @return: The person name.
        '''
        return self.__name
    
    
    def getCPF (self):
        '''
        Get the person CPF.
        @param self: The Person object instance.
        @return: The person CPF.
        '''
        return self.__cpf
    
    def getIDs (self):
        '''
        Get the person Identifications.
        @param self: The Person object instance.
        @return: A frozenset with all identifications, if there is no identification returns a empty frozenset.
        '''
        return frozenset(self.__ids)
    
    def addID (self, identification):
        '''
        Add a new identification to this person.
        @param self: The Person object instance.
        @param identification: The identification (Must be immutable and hashable). 
        '''
        self.__ids.add(identification)
        
    def addAllowedRoom (self, room):
        '''
        Add a new room to this person allowed set.
        The room will be converted to an integer with int().
        @param self: The Person object instance.
        @param room: The room (Must be a number). 
        '''
        self.__rooms.add(int(room))
        
    def getAllowedRooms (self):
        '''
        Get all rooms that this person is allowed to enter.
        @param self: The Person object instance.
        @return: A frozenset with all allowed rooms numbers, if there is no room returns a empty frozenset.
        '''
        return frozenset(self.__rooms)
    
    def __eq__ (self, other):
        '''
        Compares two Persons, they will be equal if they have the same CPF.
        @param self: The Person object instance.
        @param other: The other Person object instance.
        '''
        if other == None:
            return False

        return self.getCPF() == other.getCPF()
    
    def __ne__ (self, other):
        return not self.__eq__(other)
    
    def __hash__ (self):
        return hash(self.getCPF())
    
        
