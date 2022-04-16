class Animal:
  def __init__(self, name):
    self.name = name
    self.species = "Undefined"

  def printName(self):
    print("My name is {}".format(self.name))

  def printSpecies(self):
    print("I am a {}".format(self.species))

  def speak(self):
    pass

  def walk(self):
    pass

  def legCount(self):
    pass

  def doYourThing(self):
    print("----------------------------------------")
    self.printName()
    self.printSpecies()
    self.speak()
    self.walk()
    print("========================================")
    print()



