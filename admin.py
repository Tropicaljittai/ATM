
class Account:
    def __init__(self, atm, pin, name, accnumber, balance):
        self.__pin = atm.getUserPin(pin)
        self.__name = atm.getUser(pin)
        self.__accnumber = atm.getaccnum(pin)
        self.__balance = atm.checkbal(pin)

    def getPin(self):
        return self.__pin  
    def getBalance(self):
        return self.__balance
    def getName(self):
        return self.__name
    def getAccnum(self):
        return self.__accnumber