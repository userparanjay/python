class Car:
    def __init__(self,type):
        self.type=type

    def start():
        print("start car")
    def printType(self):
        print(self.type)

class Toyota(Car):
    def __init__(self,type):
        super().__init__(type)

c=Toyota("xuv")
c.printType()