'''
Created on 29/10/2011
@author: katcipis
'''

from couchdb import ResourceConflict
import couchdb
from cfg import database_cfg

class DeviceDAO(object):
    '''
    Device Data Access Object
    '''
   
    REGISTERED_DEVICES = 'registered-devices'
 
    def __init__(self, db=None):
        '''
        Constructor
        @param self: The Device DAO object instance.
        @param db: The database object that will be used by this DAO.
        '''
        if not db:
            server = couchdb.Server(database_cfg.SERVER_URL)
            if database_cfg.DEVICES_DATABASE_NAME in server:
                db = server[database_cfg.DEVICES_DATABASE_NAME]
            else:
                db = server.create(database_cfg.DEVICES_DATABASE_NAME)

        self.__db = db
        

    def add (self, room, device):
        '''
        Add a new Device to a room.
        If the device is already added on the given room, nothing happens.
        If the device is already added on another room, it will be 
        removed from that room and added on this new one. 
        @param self: The Device DAO object instance.
        @param room: The room where the device will be added.
        @param device: The device.
        '''
        room = str(room)
        devices = []

        if room in self.__db:
            devices = self.__db[room][DeviceDAO.REGISTERED_DEVICES]
            if device in devices:
                return

            self.__db.delete(self.__db[room])
           
        #if the device is changing its room we must remove the old register
        for r in self.__db:
            if device in self.__db[r][DeviceDAO.REGISTERED_DEVICES]:
                self.remove(r, device)

        devices.append(device)
        self.__db[room] = { DeviceDAO.REGISTERED_DEVICES : devices }

    
    def remove (self, room, device):
        '''
        Remove a device from the given room.
        @param self: The Device DAO object instance.
        @param room: The room where the device will be added.
        @param device: The device.
        '''
        room = str(room)
        devices = []

        if room in self.__db:
            devices = self.__db[room][DeviceDAO.REGISTERED_DEVICES]

        if device in devices:
            devices.remove(device)
            self.__db.delete(self.__db[room])
            self.__db[room] = { DeviceDAO.REGISTERED_DEVICES : devices }


    def get_devices (self, room):
        '''
        Get all Devices registered on the given room.
        @param self: The Device DAO object instance.
        @param room: The room.
        @return: A list of devices or a empty list if no devices are registered on the given room.
        '''
        room = str(room)
        if not room in self.__db:
            return []

        return self.__db[room][DeviceDAO.REGISTERED_DEVICES]
