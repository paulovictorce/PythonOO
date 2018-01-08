class Car:

    def __init__(self, name, maker, year, color):
        self.name = name
        self.maker = maker
        self.year = year
        self.color = color

    def drive(self):
        print(self.name + ' started')

    @staticmethod
    def hello():
        print('Hello World1')
