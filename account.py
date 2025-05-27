class Account:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.transactions = []
        self.frozen = False
        self.loan = 0
        self.minimum_balance = 0
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(amount)
            return f"Deposited amount is {amount}. Balance after deposit is {self.balance}"
        else:
            return "Deposit must be a positive amount."
    def withdraw(self, amount):
        if self.frozen:
            return "Account is frozen."
        elif amount > self.balance:
            return "Insufficient funds. Cannot withdraw."
        elif self.balance - amount < self.minimum_balance:
            return "Cannot withdraw below the minimum balance."
        self.balance -= amount
        self.transactions.append(amount)
        return f"New balance after withdrawal is {self.balance}"
    def transfer_funds(self, target_account, amount):
        if self.frozen or target_account.frozen:
            return "One of the accounts is frozen."
        elif amount > self.balance:
            return "Insufficient funds."
        elif self.balance - amount < self.minimum_balance:
            return "Cannot transfer below minimum balance."
        self.withdraw(amount)
        target_account.deposit(amount)
        return f"Transferred {amount} to {target_account.name}"
    def get_balance(self):
        return self.balance
    def request_loan(self, amount):
        self.loan += amount
        self.balance += amount
        self.transactions.append(amount)
        return f"Loan approved. New balance: {self.balance}"
    def repay_loan(self, amount):
        if amount > self.loan:
            return "Amount exceeds loan."
        self.loan -= amount
        self.balance -= amount
        self.transactions.append(amount)
        return f"Remaining loan: {self.loan}, New balance: {self.balance}"
    def view_account_details(self):
        return f"Name: {self.name}, Balance: {self.balance} Loan: {self.loan}"
    def change_account_name(self, new_name):
        self.name = new_name
        return f"Account name changed to {self.name}"
    def account_statement(self):
        return ",".join(self.transactions)
    def interest_calculation(self):
        interest = self.balance * 0.05
        self.balance += interest
        self.transactions.append(f"Interest added: {interest}")
        return f"New balance after interest: {self.balance}"
    def freeze_account(self):
        self.frozen = True
        return "Account frozen."
    def unfreeze_account(self):
        self.frozen = False
        return "Account unfrozen."
    def set_minimum_balance(self, amount):
        if amount >= 0:
            self.minimum_balance = amount
            return f"Minimum balance set to {amount}"
        return "Invalid minimum balance."
    def close_account(self):
        self.transactions.clear()
        self.balance = 0
        self.loan = 0
        return "Account closed. All balances set to zero and transcations cleard."