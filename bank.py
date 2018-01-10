class Account:

    def __init__(self, number):
        self.number = number
        self.total = 0

    def deposit(self, value):
        self.total += value

    def withdraw(self, value):
        self.total -= value

    def getTotal(self):
        return self.total