import random

from resources.base import ResourceBase
from utils.fetch_data import hit_url


class Characters(ResourceBase):
    """
    Resource class (plural)
    """

    def __init__(self):
        super().__init__()
        self.__relative_url = "api/people/" # plural
        self.__character_range = [1, 82]

    @property
    def relative_url(self):
        return self.__relative_url

    @property
    def character_range(self):
        return self.__character_range

    @character_range.setter
    def character_range(self, new_range_):
        self.__character_range = new_range_

    def get_count(self):
        plural_character_url = self.home_url + self.relative_url
        response = hit_url(plural_character_url)
        result = response.json()
        return result.get("count")

    def get_resource_urls(self):
        resource_urls_data = []
        #resource_url = self.home_url + self.__relative_url
        for i in range(1, 4):
            resource_url = self.home_url + self.__relative_url
            j = random.randrange(self.__character_range[0], self.__character_range[1])
            print(j)
            resource_url = resource_url+f"{j}"
            print(resource_url)
            resource_urls_data.append(resource_url)
        print(resource_urls_data)
        return resource_urls_data

    def get_sample_data(self, id_="1"):
        complete_url = self.home_url + self.__relative_url + id_
        # response = hit_url(complete_url)
        # data = response.json()
        # return data
        return complete_url

