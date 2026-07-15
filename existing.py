from getpass import getpass
from termcolor import colored
from db_config import get_db_connection

# Variables
mydb = get_db_connection()
mycursor = mydb.cursor()
nothing = ""
is_running = True
Mismatch = True
exis_username = ""

class existingacc:
    # Show Balance
    def showBalance(self):
        balance_query = "SELECT Balance FROM bank Where Username = %s"
        mycursor.execute(balance_query, (exis_username,))
        result = mycursor.fetchone()

        if result:
            return result[0]
        else:
            return 0.0

    # Deposit Money
    def deposit(self):
        amount = float(input("Enter an amount to be deposited: "))
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
    def withdraw(self):
        amount = float(input("Enter the amount to be withdrawn: "))
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
                existUsername = exis_username
                break
            else:
                print(colored("Incorrect password.", "red"))
                Mismatch = False

        print()
        print(f"1. Show Balance{nothing:<10} 2. Deposit")
        print(f"3. Withdraw{nothing:<14} 4. Log Out!")
        print()

        while True:

            choice = input("Enter your choice(1-4): ")

            match choice:
                case '1':
                    print(self.showBalance())
                case '2':
                    self.deposit()
                case '3':
                    self.withdraw()
                case '4':
                    print(colored("Logged out successfully!", "yellow"))
                    print(colored("Thank You! Have a nice day!", "yellow"))
                    return
                case _:
                    print("That is not a valid choice")

