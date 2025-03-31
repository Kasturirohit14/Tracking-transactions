# Key method showing core transaction logic
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
