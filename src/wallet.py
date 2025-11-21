class Wallet:
    def __init__(self, balance, size, isOpen , color):
        self.balance = balance
        self.size = size
        self.isOpen = isOpen
        self.color = color

    def addMoney(self, amount):
        self.balance += amount

    def checkMoney(self):
        self.isOpen = True
        print(f'you have a {self.balance} $')

    def getMoney(self, amount):
        if self.balance >= amount:
            self.isOpen = True
            self.balance -= amount
        else:
            print("money not enough")
