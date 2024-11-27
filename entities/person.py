from dataclasses import dataclass
from datetime import date

from entities.entity import Entity
from utils.tables import PERSON, CITY


@dataclass
class Person(Entity):
    birth_number: str = ""
    first_name: str = ""
    last_name: str = ""
    telephone: str = ""
    email: str = ""
    city: int = 0
    street: str = ""

    birth_date: date = date.today()

    @property
    def table_name(self) -> str:
        return f"{PERSON}"

    @property
    def columns(self) -> list:
        return [
            "birth_number VARCHAR2(11) PRIMARY KEY",
            "first_name VARCHAR2(30)",
            "last_name VARCHAR2(30)",
            "telephone VARCHAR2(50)",
            "email VARCHAR2(50)",
            "city INTEGER",
            "street VARCHAR2(50)",
            f"CONSTRAINT fk_cit_per FOREIGN KEY (city) REFERENCES {CITY}(id)",
        ]
