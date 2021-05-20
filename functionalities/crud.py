import pandas as pd
from functionalities.gen import Gen
USER_DATA_PATH = "./data/users.csv"
ESTATE_DATA_PATH = "./data/data.csv"


class UserCrud:
    def __init__(self, user):
        self.user = user
        self.userType = 1
    def createThoroughfare(self):
        print()

    def viewThoroughfare(self):
        print()

    def updateThoroughfare(self):
        print()

    def createProperties(self):
        print()

    def viewProperties(self):
        print()

    def updateProperties(self):
        print()

    def generateInvoice(self):
        print()

    def printInvoice(self):
        print()

class ManagerCrud(UserCrud):
    def __init__(self):
        self.userType = 2

    def deleteThoroughfare(self):
        print()

    def deleteProperties(self):
        print()

    def deleteHousehold(self):
        print()

    def deleteHouseholdCustodian(self):
        print()

    def createUser(self):
        print()

    def viewTotalInvoice(self):
        print()

class AdminCrud(ManagerCrud):
    def __init__(self):
        self.userType = 3

    def createUser(self, type, estate):
        newId = Gen.ranGen()
        ls = [newId, type, estate]
        df = pd.read_csv(USER_DATA_PATH)
        dd = pd.DataFrame([ls], columns=['Id', 'type', 'estate'])
        df = df.append(dd, ignore_index=True)
        df.to_csv(USER_DATA_PATH, index=False)

    def createEstate(self, name, contact, manager, location):
        df = pd.read_csv(ESTATE_DATA_PATH)
        ls = [name, contact, manager, location]
        dd = pd.DataFrame([ls], columns=['name', 'contact', 'manager', 'location'])
        df = df.append(dd, ignore_index=True)
        df.to_csv(ESTATE_DATA_PATH, index=False)

    def viewEstate(self):
        ls=[]
        df = pd.read_csv(ESTATE_DATA_PATH)
        for i in range(len(df)):
            ls.append([df['name'][i], df['contact'][i], df['manager'][i], df['location'][i]])
        return ls


