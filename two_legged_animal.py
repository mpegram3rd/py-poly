from animal import Animal

class TwoLeggedAnimal(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.legs = 4

    def legCount(self):
        print("I have {} legs".format(self.legs))

    def walk(self):
        self.legCount()
        print("Left foot forward")
        print("Right foot forward")
