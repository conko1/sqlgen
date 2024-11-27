from dataclasses import dataclass

from entities.entity import Entity
from utils.tables import CITY, DISTRICT


@dataclass
class City(Entity):
    id: int = 0
    zip: str = ""
    name: str = ""
    short_name: str = ""
    district: int = 0

    @property
    def table_name(self) -> str:
        return f"{CITY}"

    @property
    def columns(self) -> list:
        return [
            "id INTEGER PRIMARY KEY",
            "zip VARCHAR2(20)",
            "name VARCHAR2(50)",
            "short_name VARCHAR2(50)",
            "district INTEGER",
            f"CONSTRAINT fk_dist_city FOREIGN KEY (district) REFERENCES {DISTRICT}(id)",
        ]
