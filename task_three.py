"""
# 1. TODO import all resource classes here
# 2. TODO get count of each resource
# 3. TODO get "singular" resource urls of each resource
# 4. TODO pull data from random 3 "singular" resource URLs
# 5. TODO convert swapi project into CLI application
      # task1 task2 task3

"""
# resource - classes
from resources.characters import Characters
from resources.films import Film
from resources.planets import Planet
from resources.species import Species
from resources.starship import Starship
from resources.vehicles import Vehicles

if __name__ == "__main__":

    characterP = Characters()
    print("Character count ", characterP.get_count())
    print("Character urls ",characterP.get_resource_urls())
    print("Character singular url ",characterP.get_sample_data())

    film = Film()
    print("Films count ", film.get_count())
    print("Films urls ", film.get_resource_urls())
    print("Film singular url ", film.get_sample_data())

    planet = Planet()
    print("Planet count ", planet.get_count())
    print("Planet urls ", planet.get_resource_urls())
    print("Planet singular url ", planet.get_sample_data())

    species = Species()
    print("Species count ", species.get_count())
    print("Species urls ", species.get_resource_urls())
    print("species singular url ", species.get_sample_data())

    starships = Starship()
    print("Starships count ", starships.get_count())
    print("Starships urls ", starships.get_resource_urls())
    print("Starships singular url ", starships.get_sample_data())

    vehicles = Vehicles()
    print("Vehicles count ", vehicles.get_count())
    print("Vehicles urls ", characterP.get_resource_urls())
    print("Vehicles singular url ", characterP.get_sample_data())





   # print(characterP.get_resource_urls())
   #  print(characterP.get_sample_data())
