import Ice, os
from database.rfid import RFID

Ice.loadSlice(os.path.join('slice', 'Database.ice'))

import Database

_id_types = { RFID.getType() : Database.IDType.RFID }

def get_allowed_persons_on_room(persons, room):
    ice_persons = []
    for person in persons:
        if room in person.getAllowedRooms():
            ids = []
            for _id in person.getIDs():
                ids.append(Database.Identification(type = _id_types[_id.getType()], data = _id.getID()))

            ice_persons.append(Database.Person(name = person.getName(), ids = ids))

    return ice_persons
