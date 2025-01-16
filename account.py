import random


class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: PLN {amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn: PLN {amount:.2f}")
            else:
                print("Insufficient funds on the account")
        else:
            print("Withdrawal amount must be positive.")

    def display_account_info(self):
        print(f"Bank Account No: {self.account_number}")
        print(f"Balance: PLN {self.balance:,.2f}")