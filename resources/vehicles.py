import random

from resources.base import ResourceBase
from utils.fetch_data import fetch_data, hit_url


class Vehicles(ResourceBase):
    """
    Planet class related functionality

    """

    def __init__(self):
        super().__init__()
        self.__relative_url = "api/vehicles/"  # api/vehicles/
        self.__vehicals_range = [1, 39]

    @property
    def relative_url(self):
        return self.__relative_url

    @property
    def range(self):
        self.__vehicals_range

    @range.setter
    def range(self, new_range):
        start, end = new_range
        self.__vehicals_range = new_range

    def get_count(self):
        plural_vehicles_url = self.home_url + self.__relative_url
        response = hit_url(plural_vehicles_url)
        result = response.json()
        return result.get("count")

    def get_resource_urls(self):
        resource_urls_data = []
        # resource_url = self.home_url + self.__relative_url
        for i in range(1, 4):
            resource_url = self.home_url + self.__relative_url
            print(resource_url)
            j = random.randrange(self.__vehicals_range[0],
                                 self.__vehicals_range[1])
            print(j)
            resource_url = resource_url + f"{j}"
            print(resource_url)
            resource_urls_data.append(resource_url)
        print(resource_urls_data)
        return resource_urls_data

    def get_sample_data(self, id_="1"):
        sample_url = self.home_url + self.__relative_url + id_
        return sample_url


# v = Vehicles()
# print(v.get_count())
# print(v.get_resource_urls())
# print(v.get_sample_data())
