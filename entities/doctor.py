from dataclasses import dataclass

from entities.entity import Entity
from utils.tables import DOCTOR, PERSON


@dataclass
class Doctor(Entity):
    id: int = 0
    birth_number: str = ""

    @property
    def table_name(self) -> str:
        return f"{DOCTOR}"

    @property
    def columns(self) -> list:
        return [
            "id INTEGER PRIMARY KEY",
            "birth_number VARCHAR2(11)",
            f"CONSTRAINT fk_bir_doc FOREIGN KEY (birth_number) REFERENCES {PERSON}(birth_number)",
        ]
