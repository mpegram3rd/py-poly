from animal import Animal
from cat import Cat
from dog import Dog
from chicken import Chicken
from human import Human

def runner(animal):
    animal.doYourThing()

# Press the green button in the gutter to run the script.
obj_cat = Cat("Puss in Boots")
obj_dog = Dog("Rover")
obj_chicken = Chicken("Plucky Clucker")
obj_human = Human("John Deere")

runner(obj_cat)
runner(obj_dog)
runner(obj_chicken)
runner(obj_human)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
