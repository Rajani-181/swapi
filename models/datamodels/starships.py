from pprint import pprint
from typing import List

from pydantic import validator

from models.basemodel import Base


class Starships(Base):
    name: str
    model: str
    manufacturer: str
    cost_in_credits: str
    length: str
    max_atmosphering_speed: str
    crew: str
    passengers: str
    cargo_capacity: str
    consumables: str
    hyperdrive_rating: float
    MGLT: int
    starship_class: str
    pilots: List[str]
    films: List[str]

    @validator("crew")
    def crew_validation(cls, crew):

        if isinstance(crew, str):
            crew_ = ""
            for i in crew:
                if i.isdigit():
                    crew_ += i

                if not crew_:  # return null if crew doesn't have any digit
                    return 'Null'

                return int(crew_)
        elif isinstance(crew, int):
            return crew

    @validator("hyperdrive_rating")
    def hyperdrive_rating_validation(cls, hyperdrive_rating):
        if isinstance(hyperdrive_rating, float):
            return int(hyperdrive_rating)



if __name__ == '__main__':
    star_data = {
        "name": "Death Star",
        "model": "DS-1 Orbital Battle Station",
        "manufacturer": "Imperial Department of Military Research, Sienar Fleet Systems",
        "cost_in_credits": "1000000000000",
        "length": "120000",
        "max_atmosphering_speed": "n/a",
        "crew": "342,953",
        "passengers": "843,342",
        "cargo_capacity": "1000000000000",
        "consumables": "3 years",
        "hyperdrive_rating": "4.0",
        "MGLT": "10",
        "starship_class": "Deep Space Mobile Battlestation",
        "pilots": [],
        "films": [
            "https://swapi.dev/api/films/1/"
        ],
        "created": "2014-12-10T16:36:50.509000Z",
        "edited": "2014-12-20T21:26:24.783000Z",
        "url": "https://swapi.dev/api/starships/9/"
    }

    star_obj = Starships(**star_data)
    pprint(dict(star_obj))

