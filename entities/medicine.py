from dataclasses import dataclass

from entities.entity import Entity
from utils.tables import MEDICINE


@dataclass
class Medicine(Entity):
    code: str = ""
    name: str = ""
    active_substance: str = ""
    complement: str = ""
    dosage_unit: str = ""
    dosage_amount: float = 0.0

    @property
    def table_name(self) -> str:
        return f"{MEDICINE}"

    @property
    def columns(self) -> list:
        return [
            "code VARCHAR2(20) PRIMARY KEY",
            "name VARCHAR2(270)",
            "active_substance VARCHAR2(110)",
            "complement VARCHAR2(200)",
            "dosage_unit VARCHAR2(22)",
            "dosage_amount DECIMAL"
        ]
