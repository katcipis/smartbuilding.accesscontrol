module Database {

    enum IDType { RFID, Face };

    dictionary<string, string> IDMetadata;

    struct Identification {
        IDType type;
        string data;
        IDMetadata metadata;
    };
    
    sequence<Identification> PersonIDs;

    struct Person {
        string name;
        PersonIDs ids;
    };

    sequence<Person> AllowedPersons;

    interface DeviceRegisterServer {

        AllowedPersons register(string ip, int room);
    };
    
    interface CacheCoeherenceServer {
        void update (AllowedPersons persons);
    };

};
