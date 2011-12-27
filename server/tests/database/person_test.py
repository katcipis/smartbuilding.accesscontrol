'''
Created on 01/10/2011

@author: katcipis
'''
import unittest
from database.person import Person, PersonConstructionError
from database.rfid import RFID

class PersonTest(unittest.TestCase):
   

    def setUp (self):
        self._james_name = 'James Bond'
        self._james_cpf = '014.012.356.98'
        self._james = Person (self._james_name, self._james_cpf)


    def testHasAName(self):
        self.assertEqual(self._james_name, self._james.getName())
        
    def testHasACPF(self):
        self.assertEqual(self._james_cpf, self._james.getCPF())
        
    def testIfHasNoIdsThenGetIDsReturnsEmptySet(self):
        self.assertEqual (set(), self._james.getIDs())
        
    def testIfHasNoAllowedRoomsThenGetAllowedRoomsReturnsEmptySet(self):
        self.assertEqual (set(), self._james.getAllowedRooms())
    
    def testAfterAddingAIDGetIDsWillReturnIt (self):
        rfid = RFID('abacate')
        self._james.addID(rfid)
        ids = self._james.getIDs ()
        self.assertEqual(1, len(ids))
        self.assertTrue(rfid in ids)
        
    def testAfterAddingARoomGetAllowedRoomsWillReturnIt (self):
        room = 512
        self._james.addAllowedRoom(room)
        rooms = self._james.getAllowedRooms()
        self.assertEqual(1, len(rooms))
        self.assertTrue(room in rooms)
    
    def testAddingTheSameARoomTwiceHasNoEffect (self):
        room = 512
        self._james.addAllowedRoom(room)
        self._james.addAllowedRoom(room)
        rooms = self._james.getAllowedRooms ()
        self.assertEqual(1, len(rooms))
        self.assertTrue(room in rooms)
        
    def testAddingTheSameAIDTwiceHasNoEffect (self):
        rfid = RFID('abacate')
        self._james.addID(rfid)
        self._james.addID(rfid)
        ids = self._james.getIDs ()
        self.assertEqual(1, len(ids))
        self.assertTrue(rfid in ids)
    
    def testIfTwoPersonsHaveTheSameCPFTheyAreEqual (self):
        otherPerson = Person (self._james_name + ' Johannes', self._james_cpf)
        self.assertEqual (otherPerson, self._james)
        
    def testIfTwoPersonsHaveDifferentCPFsTheyArentEqual (self):
        otherPerson = Person (self._james_name, self._james_cpf + '0152')
        self.assertNotEqual (otherPerson, self._james)

    def testIfTwoPersonsAreEqualTheyCantBeUnEqual (self):
        otherPerson = Person (self._james_name, self._james_cpf)
        self.assertTrue(otherPerson == self._james)
        self.assertFalse(otherPerson != self._james)
        
    def testIfTwoPersonsAreEqualTheyHaveTheSameHash (self):
        otherPerson = Person (self._james_name, self._james_cpf)
        self.assertEqual (hash(otherPerson), hash(self._james))
        
    def testIfTwoPersonsArentEqualTheyDontHaveTheSameHash (self):
        otherPerson = Person (self._james_name, self._james_cpf + '0152')
        self.assertNotEqual (hash(otherPerson), hash(self._james))

    def testAllowedRoomsWillAlwaysBeAnInt(self):
        self._james.addAllowedRoom('512')
        self.assertTrue(512 in self._james.getAllowedRooms())
        self.assertFalse('512' in self._james.getAllowedRooms())
        
    def testNameCantBeAEmptyString(self):
        self.assertRaises(PersonConstructionError, Person, '', self._james_cpf)

    def testCPFCantBeAEmptyString(self):
        self.assertRaises(PersonConstructionError, Person, self._james_cpf, '')

    def testKnowsItIsNotNone(self):
        self.assertNotEqual(None, self._james)

    def testIsHashableAndCanBeInsertedOnASet(self):
        person_set = set()
        person_set.add(self._james)
        person_set.add(self._james)
        
        self.assertTrue(self._james in person_set)
        self.assertEqual(1, len(person_set))
        

if __name__ == "__main__":
    unittest.main()
