from getpass import getpass
from termcolor import colored
from db_config import get_db_connection

# Variables
mydb = get_db_connection()
mycursor = mydb.cursor(buffered=True)
nothing = ""
is_running = True
Mismatch = True
exis_username = ""

class existingacc:
    # Show Balance
    def showBalance(self):
        global exis_username
        balance_query = "SELECT Balance FROM bank Where Username = %s"
        mycursor.execute(balance_query, (exis_username,))
        balance = mycursor.fetchone()

        tpin = int(input("TPIN: "))
        query = "SELECT TPIN FROM bank WHERE Username = %s"
        mycursor.execute(query, (exis_username,))
        result = mycursor.fetchone()
        
        if result is None:
            print("Error: User not found in database.")
            return None
        dbTPIN = result[0]

        if tpin == dbTPIN:
            if result:
                return balance[0]
            else:
                return 0.0
        else:
            print(colored("Wrong Pin!", "red"))

    # Deposit Money
    def deposit(self, amount):
        current_bal = self.showBalance()
        new_balance = current_bal + amount

        if amount <= 0:
            print("That's not a valid amount")
            return 0
        else:
            balance_query = "UPDATE bank SET Balance = %s WHERE Username = %s"
            mycursor.execute(balance_query, (new_balance, exis_username))
            mydb.commit()
            return amount

    # Withdraw Money
    def withdraw(self, amount):
        current_bal = self.showBalance()
        new_balance = current_bal - amount

        if amount > current_bal:
            print("Insufficient funds")
            return 0
        elif amount < 0:
            print("Amount should be grater than 0")
            return 0
        else:
            balance_query = "UPDATE bank SET balance = %s WHERE Username = %s"
            mycursor.execute(balance_query, (new_balance, exis_username))
            mydb.commit()
            return amount

    def accTransfer(self, accNo):
        amtTransfer = int(input("Amount: "))
        currentbal = self.showBalance()
        if currentbal < amtTransfer:
            print(colored("Insufficient Balance!⚠️", "yellow"))
        elif amtTransfer <=0:
            print("You can't transfer amount less than or equal to 0")
        else:
            new_balance = currentbal - amtTransfer

        query = "SELECT balance FROM bank WHERE `Account No.` = %s"
        mycursor.execute(query, (accNo,))
        result = mycursor.fetchone()
        balance = result[0]
        tranferdBalance = balance + amtTransfer

        try:
            balanceUpdate = "UPDATE bank SET Balance = %s WHERE Username = %s"
            mycursor.execute(balanceUpdate, (new_balance, exis_username))
            print(colored("Amount Debitted", "cyan"))

            balanceUpdate = "UPDATE bank SET Balance = %s WHERE `Account No.` = %s"
            mycursor.execute(balanceUpdate, (tranferdBalance, accNo))
            print(colored(f"Amount Creditted to Account No: {accNo}", "green"))
            mydb.commit()
        except Exception as e:
            mydb.rollback()
            print(colored(f"Transaction Failed! No changes were made: {e}", "red"))

        

    def existUser(self):
        global exis_username
        existUsername = input("Enter your username: ")
        check = mycursor.execute("SELECT Password FROM bank WHERE Username = %s", (existUsername,))
        result = mycursor.fetchone()
        if not result:
            print(colored("User not found", "red"))
            return
        db_password = result[0]

        while True:
            exis_password = getpass("Enter your password: ")
            if db_password == exis_password:
                print(colored("Login Successful!", "green"))
                
                exis_username = existUsername
                break
            else:
                print(colored("Incorrect password.", "red"))
                Mismatch = False

        print()
        print(f"1. Show Balance{nothing:<10} 2. Deposit")
        print(f"3. Withdraw{nothing:<14} 4. Account Transfer")
        print("5. Log Out!")
        print()

        while True:

            choice = input("Enter your choice(1-5): ")

            match choice:
                case '1':
                    print(self.showBalance())
                case '2':
                    amount = float(input("Enter an amount to be deposited: "))
                    self.deposit(amount)
                case '3':
                    amount = float(input("Enter an amount to be withdrawn: "))
                    self.withdraw(amount)
                case '4':
                    accNo = input("Account No: ")
                    self.accTransfer(accNo)
                case '5':
                    print(colored("Logged out successfully!", "yellow"))
                    print(colored("Thank You! Have a nice day!", "yellow"))
                    exit()
                case _:
                    print("That is not a valid choice")

