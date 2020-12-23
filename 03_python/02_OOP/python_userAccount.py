class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accountBalance = 0

    def makeDeposit(self, amount):
        self.accountBalance += amount
        return self

    def makeWithdrawal(self, amount):
        self.accountBalance -= amount
        return self

    def displayUserBalance(self):
        print(f"User:{self.name}, Current Balance: ${self.accountBalance}")
        return self

    def transferMoney(self, otherUser, amount):
        self.accountBalance -= amount        
        otherUser.accountBalance += amount
        return self

user1 = User("John Pike", "john@email.com")
user2 = User("RJ Pike", "rj@email.com")
user3 = User("Mike Holloway", "mike@email.com")

# print(user1.name, user1.email)
print()
print("---<<< Today's Deposits & Withdrawals  >>>---")
user1.makeDeposit(500).makeDeposit(100).makeDeposit(100).makeWithdrawal(50).displayUserBalance()

user2.makeDeposit(1000).makeDeposit(500).makeWithdrawal(100).makeWithdrawal(50).displayUserBalance()

user3.makeDeposit(12000).makeWithdrawal(4000).makeWithdrawal(175).makeWithdrawal(8000).displayUserBalance()

print()
print("---<<< Today's Funds transfers  >>>---")
print("---<<<", user2.name, "transferred $500 to", user3.name, ">>>---" )

user2.transferMoney(user3, 500).displayUserBalance()

print("---<<<", user3.name, "received a transfer of $500 from", user2.name, ">>>---" )
user3.displayUserBalance()





