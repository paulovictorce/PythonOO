class Account:

    def __init__(self, conta):
        self.conta = conta
        self.__total = 0

    def deposit(self, value):
        self.__total += value

    def withdraw(self, value):
        self.__total -= value

    def getTotal(self):
        return self.__total