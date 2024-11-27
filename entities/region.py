from dataclasses import dataclass

from entities.entity import Entity
from utils.tables import REGION


@dataclass
class Region(Entity):
    id: int = 0
    name: str = ""
    abbr: str = ""

    @property
    def table_name(self) -> str:
        return f"{REGION}"

    @property
    def columns(self) -> list:
        return [
            "id INTEGER PRIMARY KEY",
            "name VARCHAR2(21)",
            "abbr VARCHAR2(20)"
        ]

