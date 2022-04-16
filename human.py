from two_legged_animal import TwoLeggedAnimal

class Human(TwoLeggedAnimal):
  def __init__(self, name):
    super().__init__(name)
    self.species = "Human"

  def speak(self):
    print("Whatchootalkingboutwillis?!")


