
from movement import Swimming, Walking, Flying, Digging
class Animal:
    def __init__(self,animal_name):
        self.owner= "Matthew McDevitt"
        self.farm = "McDevitt farm"
        self.animal_name = animal_name


class Invertebrates(Animal,  Digging):
    def __init__(self, animal_name):
      Animal.__init__(self, animal_name)
      Digging.__init__(self)
      self.animal_type = "Invertebrates"


class Fish (Animal, Swimming):
    def __init__(self, animal_name):
      Animal.__init__(animal_name)
      Swimming.__init__(self)
      self.animal_type = "Fish"

class Amphibians(Animal, Swimming):
     def __init__(self, animal_name):
      Animal.__init__(self, animal_name)
      Swimming.__init__(self)
      self.animal_type = "Amphibians"

class Reptiles(Animal, Walking):
     def __init__(self, animal_name):
        Animal.__init__(self, animal_name)
        Walking.__init__(self)
        self.animal_type = "Reptiles"

class Birds(Animal, Flying):
  def __init__(self, animal_name):
     Animal.__init__(self, animal_name)
     Flying.__init__(self)
     self.animal_type = "Birds"

class Mammals(Animal, Walking):
    def __init__(self, animal_name):
         Animal.__init__(self, animal_name)
         Walking.__init__(self)
         self.animal_type = "Mammals"


