from existing import existingacc
from getpass import getpass
from termcolor import colored
import random
from db_config import get_db_connection


# Variables
mydb = get_db_connection()
mycursor = mydb.cursor()
nothing = ""
is_running = True
Mismatch = True
exis_username = ""

class newAcc(existingacc):
    def createAcc(self):
        global Mismatch
        Mismatch = True
        name = input("Enter your full name: ")
        phone = input("Phone no.: ")
        address = input("Address: ")
        City = input("City: ")
        State = input("State: ")
        email = input("email id: ")
        Aadhar_num = input("Aadhar number: ")
        Pan = input("PAN num: ")
        TPIN = int(input("Enter a 4 digit pin: "))
        new_username = name[:5] + phone[:3] + Pan[2:6]
        print()
        while Mismatch:
            ini_pass = getpass("Create a 8 unit Password\n")
            conf_pass = getpass("Confirm the Password\n")
            print() 

            if ini_pass == conf_pass:
                print(colored("🎉Account Created🎉", "green"))
                print("You can sign-in now!")
                print(f"Use the username: {new_username}")
                print(f"Account No. : {random.randint(1000000000, 9999999999)}")

                # Data Storing in Database
                try:
                    sql = """INSERT INTO BANK 
                            (Name, Phone, Address, City, State, `email id`, Aadhar, `Account No.`, Username, PAN, Password, TPIN)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

                    val = (name, phone, address, City, State, email, Aadhar_num, random.randint(1000000000, 9999999999), new_username, Pan, conf_pass, TPIN)
                
                    mycursor.execute(sql, val)

                    mydb.commit()
                except Exception:
                    print(Exception)

                want = input("Log-in?(Y/N): ")
                if want.upper() == 'Y':
                    super().existUser()
                else:
                    break
            else:
                print(colored("Password Mismatch!", "red"))
                Mismatch = False