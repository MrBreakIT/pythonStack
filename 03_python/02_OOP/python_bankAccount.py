class User:
    def __init__(self, name, email, checkingAcct, savingsAcct):
        self.name = name
        self.email = email
        self.accountBalance = 0
        self.checkingAcct = BankAccount(0, 0)
        self.savingsAcct = BankAccount(0.05, 0)
        # self.account1 = BankAccount(0, 0)
        # self.account2 = BankAccount(0.05, 0)

    def makeDeposit(self, whichAcct):
        if whichAcct == "checkingAcct":
            self.checkingAcct.deposit(amount)
        self.accountBalance += amount        
        if whichAcct == "savingsAcct":
            self.savingsAcct += amount
        return self

    def makeWithdrawal(self, whichAmount):
        self.accountBalance -= amount
        return self

    def displayUserBalance(self, whichAcct):
        if whichAcct == "checkingAcct":
            print(f"User:{self.name}, Checking Balance: ${self.accountBalance}")
        if whichAcct == "savingsAcct":
            print(f"User:{self.name}, Savings Balance: ${self.accountBalance}")
        return self

    def transferMoney(self, otherUser, amount):
        self.accountBalance -= amount
        otherUser.accountBalance += amount
        return self


class BankAccount:
    def __init__(self, intRate, balance):
        self.intRate = intRate
        self.balance = balance
        # self.account1 = BankAccount(0, 0)
        # self.account2 = BankAccount(0.05, 0)

    def deposit(self, amount):
        print(f"depositing ${amount}...")
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance >= amount:
            print(f"Withdrawaling $-{amount}")
            self.balance -= amount
        else:
            print(f"Insufficient Funds,(Loser), deducting $5")
            self.balance -= 5
        return self

    def displayInfo(self, whichAcct):
        if whichAcct == "checkingAcct":
            print(f"Ending Checking Acct Balance: ${self.balance}")
        if whichAcct == "savingsAcct":
            print(f"Ending Savings Acct Balance: ${self.balance}")
        return self

    def yieldInterest(self):
        if self.balance > 0:
            self.balance = (self.intRate * self.balance) + self.balance
        return self



user1 = User("John Pike", "john@email.com", "checkingAcct", "savingsAcct")
checkingAcct = BankAccount(0.0, 0)
savingsAcct = BankAccount(0.035, 0)

user2 = User("RJ Pike", "rj@email.com","account1", "account2")
checkingAcct = BankAccount(0.0, 0)
savingsAcct = BankAccount(0.035, 0)

user3 = User("Mike Holloway", "mike@email.com", "account1", "account2")
checkingAcct = BankAccount(0.0, 0)
savingsAcct = BankAccount(0.035, 0)

# ---------------------------------  User 1 Bank Account Info  ----------------------------------------------------------------------
print("*"*100)
print()
print("---<<< ", user1.name, "bank account records >>>---")
print("-----------<<<<< Checking Acct >>>>>-----------")
user1.displayUserBalance("checkingAcct").displayUserBalance("savingsAcct")
user1.checkingAcct.deposit(500).deposit(500).deposit(1200)
print(user1.name, "made checking deposit(s) totaling: $", user1.checkingAcct.balance)
user1.checkingAcct.displayInfo("checking")
print()
print("-----------<<<<< Savings Acct >>>>>-----------")
user1.savingsAcct.displayInfo("savingsAcct")
user1.savingsAcct.deposit(1500)
print(user1.name, "made savings deposit(s) totaling: $", user1.savingsAcct.balance)
print("<<< Balance including interest on principle >>>")
user1.savingsAcct.yieldInterest().displayInfo("savingsAcct").yieldInterest().displayInfo("savingsAcct")
print("**********  Todays Totals **********")
user1.checkingAcct.displayInfo("checkingAcct")
user1.savingsAcct.displayInfo("savingsAcct")
print("*"*100)
print()

# ---------------------------------  User 2 Bank Account Info  ----------------------------------------------------------------------
print("---<<< ", user2.name, "bank account records >>>---")
print("-----------<<<<< Checking Acct >>>>>-----------")
user2.displayUserBalance("checkingAcct").displayUserBalance("savingsAcct")
user2.checkingAcct.deposit(1200).deposit(1200).deposit(3000)
print(user2.name, "made checking deposit(s) totaling: $", user2.checkingAcct.balance)
user2.checkingAcct.displayInfo("checking")
user2.checkingAcct.withdrawal(750).displayInfo("checking")                   #wont run correct displayInfo method after the withdrawal??? ... Also do a transfer too!!
user2.checkingAcct.displayInfo("checking")                                   #try to do a transfer with a user from checking to savings AND user => user
print()
print("-----------<<<<< Savings Acct >>>>>-----------")
user2.savingsAcct.displayInfo("savingsAcct")
user2.savingsAcct.deposit(1500)
print(user2.name, "made savings deposit(s) totaling: $", user2.savingsAcct.balance)
print("<<< Balance including interest on principle >>>")
user2.savingsAcct.yieldInterest().displayInfo("savingsAcct").yieldInterest().displayInfo("savingsAcct")
print("**********  Todays Totals **********")
user2.checkingAcct.displayInfo("checkingAcct")
user2.savingsAcct.displayInfo("savingsAcct")
print("*"*100)
print()
# print()
# print("---<<< ", user2.name, "bank account records >>>---")
# user2.displayUserBalance("checking").displayUserBalance("savings")
# account3.displayInfo().deposit(1200).deposit(1200).displayInfo()
# account4.deposit(500).displayInfo()
# print(user2.name, "made checking deposit(s) totaling: $", account3.balance)
# user2.transferMoney(user3, 500).displayUserBalance("checking")

# print()
# print("---<<< ", user3.name, "bank account records >>>---")
# user3.displayUserBalance("checking").displayUserBalance("savings")


# account1.withdrawal(750).displayInfo().yieldInterest().displayInfo()
# print("*"*100)
# print("*"*100)
# account2 = BankAccount(0.05, 0)
# account1.deposit(6000).deposit(6000).displayInfo().withdrawal(750).withdrawal(
#     750).withdrawal(750).withdrawal(750).displayInfo().yieldInterest().displayInfo()
# print()
# print("---<<<  User Balances   >>>---")
# print()
# print(user1.name, ": has a checking balance of $", account1.balance, "and savings balance of $", account2.balance)
# print(user2.name, ": has a checking balance of $", account3.balance, "and savings balance of $", account4.balance)
# print(user3.name, ": has a checking balance of $", account5.balance, "and savings balance of $", account6.balance)

