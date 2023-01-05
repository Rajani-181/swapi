"""The Star Wars API lists 82 main characters in the Star Wars saga. For the
first task, we would like you to use a random number generator that picks a
number between 1-82. Using these random numbers you will be pulling 15
characters from the API using Python."""
import requests
from utils.randgen import ProduceRanNum


class Swapi:
    def __init__(self):
        self.home_url = "https://swapi.dev"
        self.resource = ["planets", "starships", "vehicles", "peoples", "films",
                         "species"]

    # function for single planet details
    def get_planet(self, num_):
        print("printing single url data")
        print(num_)
        rsc_url = self.home_url + f"/api/planets/{num_}"
        print(f"fetching data from {rsc_url}")
        res = requests.get(rsc_url)
        return res.json()

    # function for 15 random planets details
    def get_planets(self, num_list_):
        for items_ in num_list_:
            print(items_)
            rsc_url = self.home_url + f"/api/planets/{items_}"
            print(f"fetching data from {rsc_url}")
            res = requests.get(rsc_url)
            res = res.json()
            print(res)
            print("%%%%%%%%%%%" * 10)


# creating object of rangen.py file class
ran_produce_obj = ProduceRanNum(1, 82)
# single planet number {num}
num = ran_produce_obj.ran_num()
print(num)


num_list = []
# Generating list of planets from rangen
for items in range(1, 16):
    nums_ = ran_produce_obj.ran_num()
    num_list.append(nums_)
print(num_list)

# creating object of swapi class
swapi = Swapi()

# calling single planet function get_planet
single_planet = swapi.get_planet(num)
print(single_planet)

# calling list of 15 planet function get_planets
swapi.get_planets(num_list)
