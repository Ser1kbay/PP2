class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return f"Withdraw ${amount}. New balance: ${self.balance}"
            else:
                return "Insufficient funds."
        else:
            return "Invalid withdrawal amount."

owner = input("Enter account owner's name: ")
initial_balance = float(input("Enter initial balance: "))
account = Account(owner, initial_balance)

while True:
    action = input("Enter 'D' for deposit, 'W' for withdrawal, or 'Q' to quit: ").upper()
    
    if action == 'D':
        amount = float(input("Enter the deposit amount: "))
        print(account.deposit(amount))
    elif action == 'W':
        amount = float(input("Enter the withdrawal amount: "))
        print(account.withdraw(amount))
    elif action == 'Q':
        break
    else:
        print("I dont got it :(. Please enter 'D', 'W', or 'Q'.")

print(f"Final balance for {account.owner}: ${account.balance}")

