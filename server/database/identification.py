'''
Created on 09/10/2011

@author: Katcipis
'''

class Identification(object):
    '''
    Identification abstraction.
    '''

    def __init__(self, _id):
        '''
        Identification abstraction.
        '''
        self.__id = _id
        
    def getID (self):
        '''
        Get the identification raw data.
        @param self: The Identification object instance.
        @return: The identification raw data.
        '''
        return self.__id
    
    def __eq__ (self, other):
        '''
        Compares two Identifications, they will be equal if they have the same ID object.
        @param self: The Identification object instance.
        @param other: The other Identification object instance.
        '''
        return self.getID() == other.getID()
    
    def __ne__ (self, other):
        return not self.__eq__(other)
    
    def __hash__ (self):
        return hash(self.getID())
    
    def toDict (self):
        '''
        Get the identification as a dict. 
        Complex Identification objects will probably override this method.
        @param self: The Identification object instance.
        @return: The dict with all relevant data about this identification, 
                 this data must be enough to reconstruct the Identification object.
        '''
        return {'id' : self.getID(), 'type' : self.getType()}
    
    @staticmethod
    def fromDict (dict_id):
        '''
        Creates a Identification instance based on a dict. MUST be implemented by subclasses.
        @param dict_id: The Identification information, represented as a dict.
        @return: The Identification object.
        '''
        # Lets search for a subclass that has the given type.
        for subclass in Identification.__subclasses__():
            if subclass.getType() == dict_id['type']:
                if subclass.fromDict == Identification.fromDict:
                    print("Unknow type[{0}]".format(dict_id['type']))
                    raise NotImplemented()
                return subclass.fromDict (dict_id)
        
        print("THERE IS NO IDENTIFICATION SUBCLASSES !!!")     
        raise NotImplemented()  
    
    @staticmethod
    def getType ():
        '''
        Get the type of the identification. MUST be implemented by subclasses.
        @param self: The Identification object instance.
        @return: The type of the identification.
        '''
        raise NotImplemented()
        
