from dataclasses import dataclass

from entities.entity import Entity
from utils.tables import PATIENT, DOCTOR, EXAMINATION, RECIPE


@dataclass
class Recipe(Entity):
    id: int = 0
    patient: int = 0
    doctor: int = 0
    used: bool = False
    examination: int = 0

    @property
    def table_name(self) -> str:
        return f"{RECIPE}"

    @property
    def columns(self) -> list:
        return [
            "id INTEGER PRIMARY KEY",
            "doctor INTEGER",
            "patient INTEGER",
            "used VARCHAR2(5) CHECK (used IN (''True'', ''False''))",
            "examination INTEGER",
            f"CONSTRAINT fk_rec_pac FOREIGN KEY (patient) REFERENCES {PATIENT}(id)",
            f"CONSTRAINT fk_rec_doc FOREIGN KEY (doctor) REFERENCES {DOCTOR}(id)",
            f"CONSTRAINT fk_rec_exa FOREIGN KEY (examination) REFERENCES {EXAMINATION}(id)"
        ]

