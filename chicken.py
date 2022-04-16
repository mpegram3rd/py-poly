from two_legged_animal import TwoLeggedAnimal

class Chicken(TwoLeggedAnimal):
  def __init__(self, name):
    super().__init__(name)
    self.species = "Chicken"

  def speak(self):
    print("Cock-a-doodle-doo!")


