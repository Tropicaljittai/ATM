class Admin:
    def getusers(self, atm):
        for key, value in atm.getpin().items():
            print(f'{key}={value}')
    def makeaccount(self, atm, pin, name, accnum, balance):
        atm.addaccount(pin, name, accnum, balance )
    def delaccount(self, atm, pin):
        atm.delaccount(pin)
    def adminpanel(self, atm):
        print(f"""
1. Get users and users' detail
2. Create new user account
3. Delete user account
4. Exit
                    """)
        while True:
            try:
                option = int(input("Enter 1, 2, 3, or 4: "))
            except:
                print("Error: Enter 1, 2, 3, or 4 only!\n")
                continue
            else:
                if option == 1:
                    for key, value in atm.getpin().items():
                        print(f'{key}={value}')
                elif option == 2:
                    pin = (input("Enter pin: \n"))
                    name = (input("Enter name: \n"))
                    accnum = int((input("Enter account number: \n")))
                    balance = int((input("Enter balance: \n")))
                    atm.addaccount(pin, name, accnum, balance)
                    print("Account successfully created!\n")
                elif option == 3:
                    pin = (input("Enter user's pin: \n"))
                    atm.delaccount(pin)
                elif option == 4:
                    break
