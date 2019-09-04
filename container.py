from diggers_fliers import Invertebrates, Mammals, Reptiles, Fish, Amphibians, Flying


class Container_Ground:
    def __init__(self):
        self.__container_ground = []
    def clean_animal(self, animal):
        if animal.animal_type == "Reptiles" or animal.animal_type == "Mammals":
            self.__container_ground.append(animal)
        else:
             print(f'You can"t put that animal there')


class Container_Dig:
    def __init__(self):
        self.__container_dig = []
    def clean_animal(self, animal):
        if animal.animal_type == "Invertebrates":
            self.__container_dig.append(animal)
        else:
             print(f'You can"t put that animal there')



class Container_Water:
    def __init__(self):
        self.__container_water = []
    def clean_animal(self, animal):
        if animal.animal_type == "Fish" or animal.animal_type == "Amphibians" :
            self.__container_water.append(animal)
        else:
             print(f'You can"t put that animal there')

class Container_Fly:
    def __init__(self):
        self.__container_fly = []
    def clean_animal(self, animal):
        if animal.animal_type == "Flying"  :
            self.__container_fly.append(animal)
        else:
             print(f'You can"t put that animal there')


