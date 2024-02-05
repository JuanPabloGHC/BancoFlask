from models.Account import Account
class Banco:
    def __init__(self, name):
        self.name = name
        self.users = []

    def AddUser(self, name, account, balance):
        self.users.append(Account(name, account, balance))

    
    def SearchUser(self, account):
        for user in self.users:
            if user.account == account:
                return user
        return None

    def Deposit(self, user, amount):
        index = self.users.index(user)
        self.users[index].Entry(amount)
    
    def Withdrawal(self, user, amount):
        index = self.users.index(user)
        self.users[index].Exit(amount)
    
    def Transfer(self, userW, userD, amount):
        self.Withdrawal(userW, amount)
        self.Deposit(userD, amount)