from typing import List

from Tools.i18n.makelocalealias import pprint

from models.basemodel import Base


class Vehicles(Base):
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
    vehicle_class: str
    pilots: List[str]
    films: List[str]


if __name__ == '__main__':
    vehicles_data = {
        "name": "Sand Crawler",
        "model": "Digger Crawler",
        "manufacturer": "Corellia Mining Corporation",
        "cost_in_credits": "150000",
        "length": "36.8 ",
        "max_atmosphering_speed": "30",
        "crew": "46",
        "passengers": "30",
        "cargo_capacity": "50000",
        "consumables": "2 months",
        "vehicle_class": "wheeled",
        "pilots": [],
        "films": [
            "https://swapi.dev/api/films/1/",
            "https://swapi.dev/api/films/5/"
        ],
        "created": "2014-12-10T15:36:25.724000Z",
        "edited": "2014-12-20T21:30:21.661000Z",
        "url": "https://swapi.dev/api/vehicles/4/"
    }

vehicles_obj = Vehicles(**vehicles_data)
pprint(dict(vehicles_obj))
