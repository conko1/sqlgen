from dataclasses import dataclass
from datetime import date

from entities.entity import Entity
from utils.tables import PATIENT, PERSON


@dataclass
class Patient(Entity):
    id: int = 0
    birth_number: str = ""
    blood_type: str = ""

    birth_date: date = date.today()

    blood_type_options = [
        "A Pozitív",
        "A Negatív",
        "B Pozitív",
        "B Negatív",
        "AB Pozitív",
        "AB Negatív",
        "0 Pozitív",
        "0 Negatív"
    ]

    @property
    def table_name(self) -> str:
        return f"{PATIENT}"

    @property
    def columns(self) -> list:
        blood_type_values = ", ".join(f"''{option}''" for option in self.blood_type_options)
        return [
            "id INTEGER PRIMARY KEY",
            "birth_number VARCHAR2(11)",
            f"blood_type VARCHAR2(20) CHECK (blood_type IN ({blood_type_values}))",
            f"CONSTRAINT fk_bir_pat FOREIGN KEY (birth_number) REFERENCES {PERSON}(birth_number)",
        ]
