from four_legged_animal import FourLeggedAnimal

class Dog(FourLeggedAnimal):
  def __init__(self, name):
    super().__init__(name)
    self.species = "Dog"

  def speak(self):
    print("WOOF!")


