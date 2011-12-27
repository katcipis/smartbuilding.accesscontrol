from database.device_dao import DeviceDAO
from database.person_dao import PersonDAO
from database import utils
from cfg import ice_cfg
import os, traceback, Ice

Ice.loadSlice(os.path.join('slice', 'Database.ice'))
import Database

class CacheCoeherenceManager(object):


    def __init__(self):
        self.__device_dao = DeviceDAO()  
        self.__person_dao = PersonDAO()
        self.__ice_communicator = Ice.initialize()

    def update (self, room):
        persons = utils.get_allowed_persons_on_room(self.__person_dao.load_all(), room)

        for device in self.__device_dao.get_devices(room):
            if self.__update_device_cache(device, persons):
                print("CacheCoeherenceManager: update: device[{0}] update with success".format(device))
            else:
                print("CacheCoeherenceManager: update: unable to connect on device[{0}], removing it from db".format(device))
                self.__device_dao.remove(room, device)


    def __update_device_cache(self, device, persons):
        try:
            ip = device['ip']
            print('CacheCoeherenceManager: update_device_cache: updating device[{ip}]'.format(ip = ip))

            proxy_name = "{name}:default -h {ip} -p {port}".format(name = ice_cfg.CACHE_COEHERENCE_SERVER_NAME,
                                                                              ip = ip, port = ice_cfg.CACHE_COEHERENCE_SERVER_PORT)
            print('CacheCoeherenceManager: update_device_cache: connecting at [{0}]'.format(proxy_name))

            base = self.__ice_communicator.stringToProxy(proxy_name)
            print('CacheCoeherenceManager: update_device_cache: obtained proxy base object')
            cache_server = Database.CacheCoeherenceServerPrx.checkedCast(base)
            print('CacheCoeherenceManager: update_device_cache: obtained CacheCoeherenceServer proxy object')
            if not cache_server:
                raise RuntimeError("Invalid proxy")

            cache_server.update(persons)
 
        except:
            traceback.print_exc()
            return False

        return True 
