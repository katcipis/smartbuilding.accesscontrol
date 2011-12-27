'''
Created on 01/10/2011
@author: katcipis
'''
import unittest
from database.rfid import RFID

class RFIDTest(unittest.TestCase):

    def setUp (self):
        self._rfid_str = '0x487ff78920179'
        self._rfid = RFID (self._rfid_str)

    def testHasAID(self):
        self.assertEqual(self._rfid_str, self._rfid.getID())
        
    def testIsHashableAndCanBeInsertedOnASet(self):
        id_set = set()
        id_set.add(self._rfid)
        id_set.add(self._rfid)
        
        self.assertTrue(self._rfid in id_set)
        self.assertEqual(1, len(id_set))
        
    def testIfTwoRFIDsHaveTheSameIDTheyAreEqual (self):
        another_rfid = RFID (self._rfid.getID())
        self.assertEqual(another_rfid, self._rfid)
    
    def testIfTwoRFIDsHaveTheSameIDTheyHaveTheSameHash (self):
        another_rfid = RFID (self._rfid.getID())
        self.assertEqual(hash(another_rfid), hash(self._rfid))
        
    def testHasTheRFIDType (self):
        self.assertEqual ('RFID', self._rfid.getType())
    
    def testIfTwoRFIDsHaveDifferentIDTheyArentEqual (self):
        another_rfid = RFID (self._rfid.getID() + 'kmlo')
        self.assertNotEqual(another_rfid, self._rfid)
        
    def testIfTwoRFIDsAreEqualTheyCantBeUnEqual (self):
        another_rfid = RFID (self._rfid.getID())
        self.assertTrue(another_rfid == self._rfid)
        self.assertFalse(another_rfid != self._rfid)
    
    def testIfTwoRFIDsHaveDifferentIDTheyDontHaveTheSameHash (self):
        another_rfid = RFID (self._rfid.getID() + 'kmlo')
        self.assertNotEqual(hash(another_rfid), hash(self._rfid))
        
    
if __name__ == "__main__":
    unittest.main()
