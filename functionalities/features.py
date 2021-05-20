import enum


class ThoroughfareType(enum.Enum):
    street = 1
    close = 2
    avenue = 3
    crescent = 4
    lane = 5
    court = 6
    road = 7


class Thoroughfare:
    def __init__(self, name, thoroughfareType):
        self.name = name
        self.thoroughfareType = thoroughfareType


class Estate:
    def __init__(self, name, thoroughfares, properties, contact, manager, location):
        self.name = name;
        self.contact = contact
        self.manager = manager
        self.location = location
        self.thoroughfares = thoroughfares
        self.properties = properties


class PropertyType(enum.Enum):
    house = 1
    semiDetached = 2
    terrace = 3
    blockOfFlats = 4


class PropertyOwnershipType(enum.Enum):
    owned = 1
    rented = 2
    managed = 3


class Property:
    def __init__(self, address, owner, completionDate, ownershipType, households):
        self.address = address
        self.owner = owner
        self.completionDate = completionDate
        self.ownershipType = ownershipType
        self.households = households


class Household:
    def __init__(self, custodian):
        self.custodian = custodian
