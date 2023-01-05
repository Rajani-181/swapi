from pprint import pprint
from typing import List, Dict
from utils.fetch_data import fetch_data
import requests


def get_all_char_of_film_people(result_: Dict) -> List:
    """
       pick only names from film data.

       :param result: data fetched from first film
       :return: names of chars in movie 1
       """

    char_url = result_.get("characters")
    char_data = fetch_data(char_url) if char_url else []
    char_names_ = [char.get("name") for char in char_data if char_data]
    print(char_names_)
    return char_names_


def get_all_veh_of_film_people(result_: Dict) -> List:
    """
       pick all vehicle names
       :param result_: data from first film
       :return: names of vehicles
       """

    veh_url = result_.get("vehicles")
    veh_data = fetch_data(veh_url) if veh_url else []
    veh_names_ = [vehicle.get("name") for vehicle in veh_data if veh_data]
    return veh_names_


if __name__ == "__main__":
    url = "https://swapi.dev/api/films/1/"
    response = requests.request("GET", url)
    # response = requests.get(url)
    result = response.json()

    char_names = get_all_char_of_film_people(result)
    veh_names = get_all_veh_of_film_people(result)

    print(char_names)
    print("****" * 20)
    pprint(veh_names)
