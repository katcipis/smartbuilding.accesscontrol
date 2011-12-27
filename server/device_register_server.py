#!/usr/bin/env python

import os, sys, Ice
from database.person_dao import PersonDAO
from database.device_dao import DeviceDAO
from database.rfid import RFID
from database import utils
from cfg import ice_cfg

Ice.loadSlice(os.path.join('slice', 'Database.ice'))

import Database


class ServerI(Database.DeviceRegisterServer):

    def __init__(self, *args, **kwargs):
        Database.DeviceRegisterServer.__init__(self, *args, **kwargs)
        self.__person_dao = PersonDAO()
        self.__device_dao = DeviceDAO()

    def register(self, ip, room, current=None):
        print('register: database device ip[{0}] on room[{1}]'.format(ip, room))
        self.__device_dao.add(str(room), {'ip':ip})
        return utils.get_allowed_persons_on_room(self.__person_dao.load_all(), room)
                


class ServerApp (Ice.Application):

    def run(self, args):
        # Terminate cleanly on receipt of a signal
        self.shutdownOnInterrupt()

        # Create an object adapter
        adapter = self.communicator().createObjectAdapterWithEndpoints("DeviceRegisterServer", "default -h {0} -p {1}".format(ice_cfg.DEVICE_REGISTER_SERVER_HOST, ice_cfg.DEVICE_REGISTER_SERVER_PORT))
        server = ServerI()
        # The server id must be well know and human readable (not a UUID)
        adapter.add(server, self.communicator().stringToIdentity(ice_cfg.DEVICE_REGISTER_SERVER_NAME))

        # All objects are created, allow client requests now
        adapter.activate()

        # Wait until we are done
        self.communicator().waitForShutdown()

        if self.interrupted():
            print self.appName() + ": terminating"

        return 0


if __name__ == '__main__':
    print('Running DeviceRegister server {ip}:{port}'.format(ip = ice_cfg.DEVICE_REGISTER_SERVER_HOST, port = ice_cfg.DEVICE_REGISTER_SERVER_PORT))
    app = ServerApp()
    sys.exit(app.main(sys.argv))
