from animal import Animal

class FourLeggedAnimal(Animal):
  def __init__(self, name):
    super().__init__(name)
    self.legs = 4

  def legCount(self):
    print("I have {} legs".format(self.legs))

  def walk(self):
    self.legCount()
    print("Left Front foot forward, Right Back foot forward")
    print("Right Front foot forward, Left Back forward")


