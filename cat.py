from four_legged_animal import FourLeggedAnimal

class Cat(FourLeggedAnimal):
  def __init__(self, name):
    super().__init__(name)
    self.species = "Cat"

  def speak(self):
    print("MEOW!")


