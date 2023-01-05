import random

from resources.base import ResourceBase
from utils.fetch_data import fetch_data, hit_url


class Species(ResourceBase):
    """
    Planet class related functionality

    """
    def __init__(self):
        super().__init__()
        self.__relative_url = "api/species/"
        self.__species_range = [1, 37]

    @property
    def relative_url(self):
        return self.__relative_url

    @property
    def range(self):
        self.__species_range

    @range.setter
    def range(self, new_range):
        start, end = new_range
        self.__species
        _range = [start, end]

    def get_count(self):
        plural_species_url = self.home_url + self.__relative_url
        response = hit_url(plural_species_url)
        result = response.json()
        return result.get("count")

    def get_resource_urls(self):
        resource_urls_data = []
        # resource_url = self.home_url + self.__relative_url
        for i in range(1, 4):
            resource_url = self.home_url + self.__relative_url
            j = random.randrange(self.__species_range[0],
                                 self.__species_range[1])
            print(j)
            resource_url = resource_url + f"{j}"
            print(resource_url)
            resource_urls_data.append(resource_url)
        print(resource_urls_data)
        return resource_urls_data

    def get_sample_data(self, id_="1"):
        sample_url = self.home_url + self.__relative_url + id_
        return sample_url
