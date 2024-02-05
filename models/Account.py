class Account:
    def __init__(self, name, account, balance):
        self.name = name
        self.account = account
        self.balance = balance
    
    def GetName(self):
        return self.name
    
    def GetBalance(self):
        return self.balance
    
    def GetAccount(self):
        return self.account

    def Entry(self, amount):
        self.balance += amount

    def Exit(self, amount):
        self.balance -= amount
    
    def CheckSufficientBalance(self, amount):
        if self.balance >= amount:
            return True
        return False