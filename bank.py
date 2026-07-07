from getpass import getpass
import os
import mysql.connector
from termcolor import colored
import random
from dotenv import load_dotenv

load_dotenv()

# Database Connection
mydb = mysql.connector.connect(
    host = os.getenv('DB_HOST'),
    user = os.getenv('DB_USER'),
    password = os.getenv('DB_PASSWORD'),
    database = os.getenv('DB_NAME'),
    auth_plugin='mysql_native_password'
)
# Variables
mycursor = mydb.cursor(buffered=True)
nothing = ""
is_running = True

# Welcome page
print(colored("Hi! Welcome to ___ bank.", "red"))
operation = int(input("""What do you like to do? 
      1) Open Account
      2) Existing user? Sign in\n"""))


def showBalance():
    balance_query = "SELECT Balance FROM bank Where Username = %s"
    mycursor.execute(balance_query, (exis_username,))
    result = mycursor.fetchone()

    if result:
        return result[0]
    else:
        return None

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    current_bal = showBalance()
    new_balance = current_bal + amount

    if amount <= 0:
        print("That's not a valid amount")
        return 0
    else:
        balance_query = "UPDATE bank SET Balance = %s WHERE Username = %s"
        mycursor.execute(balance_query, (new_balance, exis_username))
        mydb.commit()
        return amount

def withdraw():
    amount = float(input("Enter the amount to be withdrawn: "))
    current_bal = showBalance()
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

if operation == 2:
    exis_username = input("Enter your username: ")
    exis_password = getpass("Enter your password: ")

    check = mycursor.execute("SELECT Password FROM bank WHERE Username = %s", (exis_username,))
    result = mycursor.fetchone()

    if result:
        db_password = result[0]
        if db_password == exis_password:
            print(colored("Login Successful!", "Green"))
        else:
            print(colored("Incorrect password.", "Red"))
    else:
        print("User not found")

    while is_running:
        print()
        print(f"1. Show Balance{nothing:<10} 2. Deposit")
        print(f"3. Withdraw{nothing:<14} 4. Exit")
        print("")

        choice = input("Enter your choice(1-4): ")

        if choice == '1':
            print(showBalance())
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            is_running = False
        else:
            print("That is not a valid choice")

    print("Thank You! Have a nice day!")
    

elif operation == 1:
    name = input("Enter your full name: ")
    phone = input("Phone no.: ")
    address = input("Address: ")
    City = input("City: ")
    State = input("State: ")
    email = input("email id: ")
    Aadhar_num = input("Aadhar number: ")
    Pan = input("PAN num: ")
    new_username = name[:5] + phone[:3] + Pan[2:6]
    print()
    ini_pass = getpass("Create a 8 unit Password\n")
    conf_pass = getpass("Confirm the Password\n")
    print()
    if ini_pass == conf_pass:
        print(colored("🎉Account Created🎉", "Light Green"))
        print("You can sign-in now!")
        print(f"Use the username: {new_username}")
        print(f"Account No. : {random.randint(1000000000, 9999999999)}")
    else:
        print("Password Mismatch!")

    
    try:
        sql = """INSERT INTO BANK 
                (Name, Phone, Address, City, State, `email id`, Aadhar, `Account No.`, Username, PAN, Password)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        val = (name, phone, address, City, State, email, Aadhar_num, random.randint(1000000000, 9999999999), new_username, Pan, conf_pass)
    
        mycursor.execute(sql, val)

        mydb.commit()
    except Exception:
        print(Exception)

else:
    print("Wrong Operation! Please enter the number of the operation you want to perform")
