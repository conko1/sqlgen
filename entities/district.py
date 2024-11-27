from dataclasses import dataclass

from entities.entity import Entity
from utils.tables import DISTRICT, REGION


@dataclass
class District(Entity):
    id: int = 0
    code: int = 0
    name: str = ""
    region: int = 0

    @property
    def table_name(self) -> str:
        return f"{DISTRICT}"

    @property
    def columns(self) -> list:
        return [
            "id INTEGER PRIMARY KEY",
            "code INTEGER",
            "name VARCHAR2(22)",
            "region INTEGER",
            f"CONSTRAINT fk_reg_dist FOREIGN KEY (region) REFERENCES {REGION}(id)",
        ]
