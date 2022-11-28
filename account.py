
class ATM():
    def __init__(self):
        self.__numofuser = 5
        self.__accounts = {
            "1111": { "name": "Samuel", "accnumber": 113782, "amt": 52000 },
            "1112": { "name": "Jane", "accnumber": 128361, "amt": 20000 },
            "1113": { "name": "Mimi", "accnumber": 372351, "amt": 70000 },
            "1114": { "name": "James", "accnumber": 293452, "amt": 30000 },
            "1115": { "name": "Jake", "accnumber": 632124, "amt": 60000 },
            }
    def addaccount(self, pin, name, accnum, balance):
        self.__accounts[pin]={ "name": name, "accnumber": accnum, "amt": balance }
        self.__numofuser+=1
    def delaccount(self, pin):
        self.__accounts.pop(str(pin))
        self.__numofuser-=1
    def getUserPin(self, pin):
        return self.__accounts[pin]
    def getpin(self):
        return self.__accounts
    def getUser(self, i):
        return self.__accounts[i]["name"]
    def getaccnum(self, i):
        return self.__accounts[i]["accnumber"]
    def deposit(self, amount, i):
        if (amount>=0):
            self.__accounts[i]["amt"] = amount+self.__accounts[i]["amt"]
        else:
            print("Enter a valid number!")
    def withdraw(self, amount, i):
        if (amount>self.__accounts[i]["amt"]):
            print("Insufficient balance. You only have", self.__accounts[i]["amt"])
        else:
            self.__accounts[i]["amt"] = self.__accounts[i]["amt"] - amount
    def checkbal(self, i):
        return self.__accounts[i]["amt"]
    def exit(self, i):
                    print(f"""
Transaction complete.                         
Account holder: {self.__accounts[i]["name"]}                  
Account number: {self.__accounts[i]["accnumber"]}                
Available balance: {self.__accounts[i]["amt"]}                    
          """)
    def transanction(self):
        atm = ATM()
        while True:
            pin = input("Enter pin: ")
            if (pin == "admin11"):
                from admin1 import Admin
                admin = Admin()
                admin.adminpanel(atm)
            elif (pin in atm.getpin()):
                print(f"""
1. Check Balance
2. Deposit
3. Withdraw
4. Account Details
5. Exit
                    """)
                while True:
                    try:
                        option = int(input("Enter 1, 2, 3, 4, or 5: "))
                    except:
                        print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                        continue
                    else:
                            if option == 1:
                                print(atm.checkbal(pin))
                            elif option == 2:
                                amount = int(input("How much you want to deposit: "))
                                atm.deposit(amount,pin)
                            elif option == 3:
                                amount = int(input("How much you want to withdraw: "))
                                atm.withdraw(amount,pin)
                            elif option == 4:
                                from admin import Account
                                account = Account(atm, pin, atm.getUser(pin), atm.getaccnum(pin), atm.checkbal(pin))
                                print("\n")
                                print("Account holder:", account.getName())
                                print("Account number:", account.getAccnum())
                                print("Available balance:", account.getBalance())
                                print("\n")
                            elif option == 5:
                                atm.exit(pin)
                                quit()
            else:
                print("Pin is not listed!\n")




	