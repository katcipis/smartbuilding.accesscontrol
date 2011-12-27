'''
Created on 01/10/2011

@author: katcipis
'''
from identification import Identification

class RFID(Identification):
    '''
    Holds information about a RFID identification.
    '''

    def __init__(self, rfid):
        '''
        Constructor
        @param self: The RFID object instance.
        @param rfid: The RFID identification string (Obligatory).
        '''
        Identification.__init__(self, rfid)
    
    @staticmethod
    def getType ():
        '''
        Get the type of the identification.
        @return: The type of the identification.
        '''
        return 'RFID'
    
    @staticmethod
    def fromDict (dict_id):
        '''
        Creates a RFID instance based on a dict.
        @param dict_id: The RFID information, represented as a dict.
        @return: The RFID object.
        '''
        return RFID(dict_id['id'])