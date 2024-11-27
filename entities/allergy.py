from dataclasses import dataclass

from entities.entity import Entity
from utils.tables import ALLERGY


@dataclass
class Allergy(Entity):
    id: int = 0
    type: str = ""

    @property
    def table_name(self) -> str:
        return f"{ALLERGY}"

    @property
    def columns(self) -> list:
        return [
            "id INTEGER PRIMARY KEY",
            "type VARCHAR2(40)"
        ]
