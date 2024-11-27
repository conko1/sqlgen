from dataclasses import dataclass

from entities.entity import Entity
from utils.tables import DOCTOR_PATIENT, PATIENT, DOCTOR


@dataclass
class DoctorPatient(Entity):
    doctor: int = 0
    patient: int = 0

    @property
    def table_name(self) -> str:
        return f"{DOCTOR_PATIENT}"

    @property
    def columns(self) -> list:
        return [
            "doctor INTEGER",
            "patient INTEGER",
            f"CONSTRAINT fk_pac_id FOREIGN KEY (patient) REFERENCES {PATIENT}(id)",
            f"CONSTRAINT fk_doc_id FOREIGN KEY (doctor) REFERENCES {DOCTOR}(id)",
        ]
