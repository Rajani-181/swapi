from pprint import pprint
from typing import List, Optional

from pydantic import validator

from models.basemodel import Base


class Character_(Base):
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: str

    species: Optional[List[str]]
    starships: Optional[List[str]]
    films: Optional[List[str]]
    vehicles: Optional[List[str]]

    @validator("height")
    def height_validation(cls):
        if isinstance(cls.height, str):
            height = int(cls.height)
            height = height / 100
            cls.height = height
            return cls.height
        else:
            raise ValueError('height cannot be converted')


if __name__ == '__main__':
    data = {
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY",
        "gender": "male",
        "homeworld": "https://swapi.dev/api/planets/1/",
        "films": [
            "https://swapi.dev/api/films/2/",
            "https://swapi.dev/api/films/6/",
            "https://swapi.dev/api/films/3/",
            "https://swapi.dev/api/films/1/",
            "https://swapi.dev/api/films/7/"
        ],
        "species": [
            "https://swapi.dev/api/species/1/"
        ],
        "vehicles": [
            "https://swapi.dev/api/vehicles/14/",
            "https://swapi.dev/api/vehicles/30/"
        ],
        "starships": [
            "https://swapi.dev/api/starships/12/",
            "https://swapi.dev/api/starships/22/"
        ],
        "created": "2014-12-09T13:50:51.644000Z",
        "edited": "2014-12-20T21:17:56.891000Z",
        "url": "https://swapi.dev/api/people/1/"
    }

    char = Character_(**data)
    pprint(char)
    print(type(char))
