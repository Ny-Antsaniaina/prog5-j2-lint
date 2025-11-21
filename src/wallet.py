class Wallet:
    def __init__(self, balance, size, isOpen):
        self.balance = balance
        self.size = size
        self.isOpen = isOpen

    def addMoney(self, amount):
        self.balance += amount

    def checkMoney(self):
        print(f'you have a {self.balance} $')

    def getMoney(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("money not enough")
