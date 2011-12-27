'''
Created on 29/10/2011
@author: katcipis
'''

import unittest
import couchdb
from database.device_dao import DeviceDAO

class DeviceDAOTest(unittest.TestCase):

    def setUp (self):
        server = couchdb.Server()

        try:
            server.delete('test')
            server.delete('other-test')
        except:
            pass

        self._db = server.create('test')
        self._another_db = server.create('other-test')
        self._device_dao = DeviceDAO (self._db)
        
    def tearDown (self):
        server = couchdb.Server()
        server.delete('test')
        server.delete('other-test')


    def testRoomCanBeANumber(self):
        device = {'ip':'127.0.0.1'}
        self._device_dao.add(500, device)

        devices = self._device_dao.get_devices(500)
        self.assertEqual(1, len(devices))
        self.assertEqual(device, devices[0])
        self._device_dao.remove(500, device)

        devices = self._device_dao.get_devices(500)
        self.assertEqual(0, len(devices))


    def testAfterAddingADeviceItWillBeThere(self):
        device = {'ip':'127.0.0.1'}
        self._device_dao.add('500', device)
        devices = self._device_dao.get_devices('500')
        self.assertEqual(1, len(devices))
        self.assertEqual(device, devices[0])

    def testAfterRemovingADeviceItWontBeThere(self):
        device = {'ip':'127.0.0.1'}
        self._device_dao.add('500', device)

        devices = self._device_dao.get_devices('500')
        self.assertEqual(1, len(devices))
        self.assertEqual(device, devices[0])

        self._device_dao.remove('500', device)
        devices = self._device_dao.get_devices('500')
        self.assertEqual(0, len(devices))

    def testRemovingADeviceFromARoomThatHasNoDeviceDoesNothing(self):
        self._device_dao.remove('500', {'whatever':'device'})
        devices = self._device_dao.get_devices('500')
        self.assertEqual(0, len(devices))

    def testIfADeviceIsAddedOnMultipleRoomsOnlyTheLastAddWillCount(self):
        device = {'ip':'127.0.0.1'}
        
        self._device_dao.add('35948789', device)
        self._device_dao.add('500', device)
        self._device_dao.add('777', device)

        self.assertEqual([], self._device_dao.get_devices('500'))
        self.assertEqual([], self._device_dao.get_devices('35948789'))

        devices = self._device_dao.get_devices('777')
        self.assertEqual(1, len(devices))
        self.assertTrue(device in devices)
        
    def testRemovingADeviceThatIsNotOnTheDBDoesNothing(self):
        device = {'ip':'127.0.0.1'}
        another_device = {'abacate': 'hahaha'}
        self._device_dao.add('500', device)
        self._device_dao.remove('500', another_device)
        devices = self._device_dao.get_devices('500')
        self.assertEqual(1, len(devices))
        self.assertEqual(device, devices[0])

    def testARoomCanHaveNoDeviceRegistered(self):
        self.assertEqual([], self._device_dao.get_devices('500'))

    def testIfTheSameDeviceIsAddedMultipleTimesItWillBeLikeItHasBeenAddedOnlyOnce(self):
        device = {'ip':'127.0.0.1'}
        self._device_dao.add('500', device)
        self._device_dao.add('500', device)
        self._device_dao.add('500', device)
        self._device_dao.add('500', device)
        devices = self._device_dao.get_devices('500')
        self.assertEqual(1, len(devices))
        self.assertEqual(device, devices[0])

    def testAllDevicesCanBeRetrievedFromARoom(self):
        device  = {'ip':'127.0.0.1'}
        device2 = {'ip':'192.168.160.181'}

        self._device_dao.add('500', device)
        self._device_dao.add('500', device2)

        devices = self._device_dao.get_devices('500')
        self.assertEqual(2, len(devices))
        self.assertTrue(device in devices)
        self.assertTrue(device2 in devices)

    def testDeviceCanBeADictWithAnyData(self):
        device = {'ip':'127.0.0.1', 'metadata' : 'hahaha', 'abacate': 5 }
        self._device_dao.add('500', device)
        devices = self._device_dao.get_devices('500')
        self.assertEqual(1, len(devices))
        self.assertEqual(device, devices[0])

    def testSavedDeviceWillBeAvailableOnAnotherDAOInstance(self):
        device = {'ip':'127.0.0.1'}
        self._device_dao.add('500', device)
        another_dao = DeviceDAO (self._db)
        devices = another_dao.get_devices('500')
        self.assertEqual(1, len(devices))
        self.assertEqual(device, devices[0])

    def testSavedDeviceWontBeAvailableOnAnotherADAOUsingADifferentDB(self):
        device = {'ip':'127.0.0.1'}
        server = couchdb.Server()
        self._device_dao.add('500', device)
        another_dao = DeviceDAO (self._another_db)
        devices = another_dao.get_devices('500')
        self.assertEqual(0, len(devices))


if __name__ == "__main__":
    unittest.main()
