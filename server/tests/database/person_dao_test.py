'''
Created on 09/10/2011

@author: katcipis
'''
import unittest
import couchdb
from database.person_dao import PersonDAO
from database.person import Person
from database.rfid import RFID

class PersonDAOTest(unittest.TestCase):

    def setUp (self):
        server = couchdb.Server()
        try:
            server.delete('test')
            server.delete('another-test')
        except:
            pass
        self._db = server.create('test')
        self._another_db = server.create('another-test')
        self._person_dao = PersonDAO (self._db)
        
    def tearDown (self):
        server = couchdb.Server()
        server.delete('test')
        server.delete('another-test')

    def assertPersonsAreEqualAndHaveSameData (self, person1, person2):
        self.assertEqual(person1, person2)
        self.assertEqual(person1.getCPF(), person2.getCPF())
        self.assertEqual(person1.getName(), person2.getName())
        self.assertEqual(person1.getIDs(), person2.getIDs())
        self.assertEqual(person1.getAllowedRooms(), person2.getAllowedRooms())

    def testIfThereIsNoPersonWithAGivenCPFReturnsNone(self):
        self._person_dao.save (Person ('Stephanie', '051.256.987.56'))
        self.assertEqual(None, self._person_dao.load('wrong CPF'))
        
    def testAfterSavingCanLoadAPersonUsingTheCPF(self):
        name = 'Stephanie'
        cpf = '051.265.789.89'
        personOrig = Person (name, cpf)
        self._person_dao.save (personOrig)
        personLoaded = self._person_dao.load(cpf)
        
        self.assertPersonsAreEqualAndHaveSameData (personOrig, personLoaded)

    def testAfterSavingCanLoadAPersonUsingTheCPFOnAnotherDAO(self):
        name = 'Stephanie'
        cpf = '051.265.789.89'
        personOrig = Person (name, cpf)
        self._person_dao.save (personOrig)
        another_dao = PersonDAO (self._db)
        personLoaded = another_dao.load(cpf)

        self.assertPersonsAreEqualAndHaveSameData (personOrig, personLoaded)

    def testPersonCantBeLoadedOnADAOThatUsesADifferentDB(self):
        name = 'Stephanie'
        cpf = '051.265.789.89'
        server = couchdb.Server()
        personOrig = Person (name, cpf)
        self._person_dao.save (personOrig)
        another_dao = PersonDAO (self._another_db)
        personLoaded = another_dao.load(cpf)
        self.assertEqual(None, personLoaded)
        
    def testTheAllowedRoomsAreSavedCorrectly(self):
        name = 'Stephanie'
        cpf = '051.265.789.89'
        
        person = Person (name, cpf)
        person.addAllowedRoom(512)
        person.addAllowedRoom(256)
        
        self._person_dao.save (person)
        personLoaded = self._person_dao.load(cpf)
        
        self.assertPersonsAreEqualAndHaveSameData (person, personLoaded)
        
    def testRFIDsAreSavedCorrectly(self):
        name = 'Stephanie'
        cpf = '051.265.789.89'
        
        person = Person (name, cpf)
        person.addID(RFID('dfeferscd'))
        person.addID(RFID('dfeferscdsdsd234'))
        
        self._person_dao.save (person)
        personLoaded = self._person_dao.load(cpf)
        
        self.assertPersonsAreEqualAndHaveSameData(person, personLoaded)
    
    def testWhenAPersonIsSavedIfThereIsNoPersonWithTheGivenCPFReturnsTrue(self):
        self.assertTrue(self._person_dao.save(Person ('Stephanie', '051.265.789.89')))
        
    def testWhenAPersonIsUpdatedIfThereIsNoPersonWithTheGivenCPFReturnsFalse(self):
        self.assertFalse(self._person_dao.update(Person ('Stephanie', '051.265.789.89')))
    
    def testWhenAPersonIsSavedIfThereIsAlreadyAPersonWithTheGivenCPFReturnsFalse(self):
        self.assertTrue(self._person_dao.save(Person ('Stephanie', '051.265.789.89')))
        self.assertFalse(self._person_dao.save(Person ('Stephanie', '051.265.789.89')))
        
    def testWhenAPersonIsUpdatedIfThereIsAlreadyAPersonWithTheGivenCPFReturnsFalse(self):
        self.assertTrue(self._person_dao.save(Person ('Stephanie', '051.265.789.89')))
        self.assertTrue(self._person_dao.update(Person ('Stephanie Katcipis', '051.265.789.89')))

    def testIfThereIsNoPersonOnTheDatabaseLoadAllReturnsAEmptyList(self):
        self.assertEqual([], self._person_dao.load_all())

    def testAfterAPersonIsRemovedItWontBeOnTheDatabaseAnymore(self):
        cpf = '051.265.789.89'

        self.assertTrue(self._person_dao.save(Person ('Stephanie', cpf)))
        self.assertNotEqual([], self._person_dao.load_all())
        self.assertNotEqual(None, self._person_dao.load(cpf))

        self.assertTrue(self._person_dao.delete(cpf))
        self.assertEqual([], self._person_dao.load_all())
        self.assertEqual(None, self._person_dao.load(cpf))

    def testIfYouRemoveSomeoneNotOnTheDatabaseReturnsFalse(self):
         self.assertFalse(self._person_dao.delete('015.125.989.85'))

    def testAllPersonsAddedAreReturnedOnLoadAll(self):
        person1 = Person ('Stephanie', '051.265.789.89')
        person1.addID(RFID('dfeferscd'))
        person1.addAllowedRoom(512)
        
        person2 = Person ('Katz', '789.265.789.89')
        person2.addID(RFID('derscd'))
        person2.addAllowedRoom(256)
  
        self._person_dao.save(person1)
        persons = self._person_dao.load_all()
        self.assertEqual(1, len(persons))
        self.assertTrue(person1 in persons)
        self.assertPersonsAreEqualAndHaveSameData (person1, persons[0])

        self._person_dao.save(person2)
        persons = self._person_dao.load_all()
        self.assertEqual(2, len(persons))
        self.assertTrue(person1 in persons)
        self.assertTrue(person2 in persons)
        
        if person1 == persons[0]:
            self.assertPersonsAreEqualAndHaveSameData (person1, persons[0])
            self.assertPersonsAreEqualAndHaveSameData (person2, persons[1])
        else:
            self.assertPersonsAreEqualAndHaveSameData (person1, persons[1])
            self.assertPersonsAreEqualAndHaveSameData (person2, persons[0])


    def testWhenAPersonIsSavedIfThereIsAlreadyAPersonWithTheGivenCPFTheFirstOneRemains(self):
        cpf = '051.265.789.89'
        firstSaved = Person ('Stephanie', cpf)
        firstSaved.addID(RFID('dfeferscd'))
        firstSaved.addAllowedRoom(512)
        
        self.assertTrue(self._person_dao.save(firstSaved))
        self.assertFalse(self._person_dao.save(Person ('Stephanie B. A.', cpf)))
        personLoaded = self._person_dao.load(cpf)
        self.assertPersonsAreEqualAndHaveSameData (firstSaved, personLoaded)

        
    def testWhenAPersonIsUpdatedTheOldPersonInfoIsReplacedByTheNewOne(self):
        cpf = '051.265.789.89'
        firstSaved = Person ('Stephanie', cpf)
        firstSaved.addID(RFID('dfeferscd'))
        firstSaved.addAllowedRoom(512)
        
        updatedperson = Person ('Stephanie B. A. K.', cpf)
        updatedperson.addID(RFID('anotherRFID'))
        updatedperson.addAllowedRoom(256)
        updatedperson.addAllowedRoom(1024)
        
        self.assertTrue(self._person_dao.save(firstSaved))
        personLoaded = self._person_dao.load(cpf)
        self.assertPersonsAreEqualAndHaveSameData (firstSaved, personLoaded)
        
        self.assertTrue(self._person_dao.update(updatedperson))
        personLoaded = self._person_dao.load(cpf)
        self.assertPersonsAreEqualAndHaveSameData (updatedperson, personLoaded)
        
        

if __name__ == "__main__":
    unittest.main()
