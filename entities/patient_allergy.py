from dataclasses import dataclass

from entities.entity import Entity
from utils.tables import PATIENT_ALLERGY, PATIENT, ALLERGY


@dataclass
class PatientAllergy(Entity):
    patient: int = 0
    allergy: int = 0

    @property
    def table_name(self) -> str:
        return f"{PATIENT_ALLERGY}"

    @property
    def columns(self) -> list:
        return [
            "patient INTEGER",
            "allergy INTEGER",
            "PRIMARY KEY (patient, allergy)",
            f"CONSTRAINT fk_doc_alg FOREIGN KEY (patient) REFERENCES {PATIENT}(id)",
            f"CONSTRAINT fk_alg_alg FOREIGN KEY (allergy) REFERENCES {ALLERGY}(id)"
        ]
