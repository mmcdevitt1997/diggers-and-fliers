from diggers_fliers import Invertebrates, Mammals, Reptiles, Fish, Amphibians, Birds
from container import Container_Dig, Container_Fly,Container_Ground, Container_Water

Parakeets = Birds("Parakeet")
Earthworms = Invertebrates("Earthworm")
Terrapin = Amphibians("Terrapin")
Timber_rattlesnake = Reptiles("Timber rattlesnake")

container_ground = Container_Ground()

container_ground.clean_animal(Timber_rattlesnake)