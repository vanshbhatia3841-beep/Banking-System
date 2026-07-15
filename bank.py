from termcolor import colored
from newacc import newAcc
from existing import existingacc

class bank:
    # Welcome page
    def __init__(self, bankName):
        self.bankName = bankName
        print(colored(f"Hi! Welcome to {self.bankName} bank.", "red"))
        self.operation = int(input("""What do you like to do? 
            1) Open Account
            2) Existing user? Sign in\n"""))

    def user_choice(self):
        match self.operation:
            case 1:
                newAccount = newAcc()
                newAccount.createAcc()
            case 2:
                existUser = existingacc()
                existUser.existUser()

bank = bank("ABC")
bank.user_choice()