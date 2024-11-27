from dataclasses import dataclass

from entities.entity import Entity
from utils.tables import INSURANCE


@dataclass
class Insurance(Entity):
    code: int = 0
    name: str = ""

    @property
    def table_name(self) -> str:
        return f"{INSURANCE}"

    @property
    def columns(self) -> list:
        return [
            "code INTEGER PRIMARY KEY",
            "name VARCHAR2(50)"
        ]

