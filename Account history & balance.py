from datetime import datetime
from typing import List, Dict

class Transaction:
    def __init__(self, amount: float, transaction_type: str, description: str):
        self.amount = amount
        self.transaction_type = transaction_type
        self.description = description
        self.timestamp = datetime.now()
        
    def __str__(self):
        return f"[{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}] {self.transaction_type.upper()}: ${self.amount:.2f} - {self.description}"

class Account:
    def __init__(self, account_number: str, account_holder: str):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions: List[Transaction] = []
        
    def credit(self, amount: float, description: str = ""):
        if amount <= 0:
            raise ValueError("Credit amount must be positive")
            
        transaction = Transaction(amount, "credit", description)
        self.balance += amount
        self.transactions.append(transaction)
        return transaction
        
    def debit(self, amount: float, description: str = ""):
        if amount <= 0:
            raise ValueError("Debit amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
            
        transaction = Transaction(amount, "debit", description)
        self.balance -= amount
        self.transactions.append(transaction)
        return transaction
        
    def get_balance(self) -> float:
        return self.balance
        
    def get_transaction_history(self) -> List[Transaction]:
        return self.transactions

def display_menu():
    print("\n=== Transaction Tracking System ===")
    print("1. Check Balance")
    print("2. Make a Deposit")
    print("3. Make a Payment")
    print("4. View Transaction History")
    print("5. Exit")
    return input("Choose an option (1-5): ")

def main():
    # Get user account details
    print("=== Create New Account ===")
    account_holder = input("Enter your name: ")
    account_number = input("Enter account number: ")
    
    account = Account(account_number, account_holder)
    print(f"\nWelcome, {account_holder}!")
    
    while True:
        choice = display_menu()
        
        try:
            if choice == "1":
                # Check Balance
                print(f"\nCurrent Balance: ${account.get_balance():.2f}")
                
            elif choice == "2":
                # Make a Deposit
                try:
                    amount = float(input("\nEnter deposit amount: $"))
                    description = input("Enter deposit description: ")
                    account.credit(amount, description)
                    print(f"Successfully deposited ${amount:.2f}")
                except ValueError as e:
                    print(f"Error: {e}")
                
            elif choice == "3":
                # Make a Payment
                try:
                    amount = float(input("\nEnter payment amount: $"))
                    description = input("Enter payment description: ")
                    account.debit(amount, description)
                    print(f"Successfully paid ${amount:.2f}")
                except ValueError as e:
                    print(f"Error: {e}")
                
            elif choice == "4":
                # View Transaction History
                print("\nTransaction History:")
                if not account.get_transaction_history():
                    print("No transactions found.")
                else:
                    for transaction in account.get_transaction_history():
                        print(transaction)
                
            elif choice == "5":
                # Exit
                print("\nThank you for using the Transaction Tracking System!")
                break
                
            else:
                print("\nInvalid option. Please choose 1-5.")
                
        except Exception as e:
            print(f"An error occurred: {e}")
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()