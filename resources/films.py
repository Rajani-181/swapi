from resources.base import ResourceBase
from utils.fetch_data import fetch_data, hit_url
import random


class Film(ResourceBase):
    """
    Planet class related functionality

    """
    def __init__(self):
        super().__init__()
        self.__relative_url = "api/films/" #https://swapi.dev/api/films/
        self.__films_range = [1, 6]

    @property
    def relative_url(self):
        return self.__relative_url

    @property
    def range(self):
        self.__films_range

    @range.setter
    def range(self, new_range):
        start, end = new_range
        self.__films_range = [start, end]

    def get_count(self):
        plural_films_url = self.home_url + self.relative_url
        print(plural_films_url)
        response = hit_url(plural_films_url)
        result = response.json()
        return result.get("count")

    def get_resource_urls(self):
        resource_urls_data = []
        # resource_url = self.home_url + self.__relative_url
        for i in range(1, 4):
            resource_url = self.home_url + self.__relative_url
            j = random.randrange(self.__films_range[0], self.__films_range[1])
            #print(j)
            resource_url = resource_url + f"{j}"
            #print(resource_url)
            resource_urls_data.append(resource_url)
        return resource_urls_data

    def get_sample_data(self, id_="1"):
        sample_url = self.home_url + self.__relative_url + id_
        return sample_url
