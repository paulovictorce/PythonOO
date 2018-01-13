class Bank1Account(object):

    def __init__(self, conta):
        self.conta = conta
        self.__total = 0

    def deposit(self, value):
        self.__total += value

    def withdraw(self, value):
        self.__total -= value

    def getTotal(self):
        return self.__total


class Bank2Account(Bank1Account):

    def __init__(self,conta, cvv):
        super(Bank2Account, self).__init__(conta)
        self.cvv = cvv

    def withdraw(self, value):
        self._Bank1Account__total -= value
        self._Bank1Account__total -= 2