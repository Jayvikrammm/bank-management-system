#Project 2 (Bank management system)
"""""
🔹 1. Basic Understanding
1. What is the purpose of this project?

This project simulates a basic banking system where users can:

View account details
Create a new account
Deposit money
Withdraw money

It demonstrates Object-Oriented Programming (OOP) concepts along with real-world banking logic.

"""

class bank:
    def __init__(self):
        self.account = {}

    def view_account(self):
       if not self.account:
           print("no account has been found")
       else:
           for account,balance in self.account.items():
               print(account,":",balance)

    def new_account(self,new_account):
        if new_account in self.account:
            print("account already exists")
        else:
            self.account[new_account] = 0
            print("new account:",new_account)
    def deposit_money(self,account_name,deposit_money):
        if account_name not in self.account:
            print("invalid account")
        else:
            self.account[account_name] += deposit_money
            print("deposit money:",deposit_money,"account:",account_name)
    def withdraw_money(self,account_name,withdraw_money):
        if account_name not in self.account:
            print("invalid account")
        else:
            self.account[account_name]-= withdraw_money
            print({withdraw_money},"has been withdrawn from",{account_name})

o = bank()

print("\n1. View all accounts")
print("2. Create account")
print("3. Deposit money")
print("4. Withdraw money")
print("5. Exit")

while True:
    choice = int(input("Enter your choice:"))
    if choice == 1:
        o.view_account()

    if choice == 2:
        name = (input("Enter your new account:"))
        o.new_account(name)

    if choice == 3:
        name = input("Enter your name:")
        if name not in o.account:
            print("invalid account")
        money = int(input("Enter your deposit money:"))
        o.deposit_money(name,money)

    if choice == 4:
        name = input("Enter your name:")
        if name not in o.account:
            print("invalid account")
        money = int(input("Enter your withdraw money:"))
        o.withdraw_money(name,money)

    if choice == 5:
        exit()



