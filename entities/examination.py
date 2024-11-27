import textwrap
from dataclasses import dataclass
from datetime import datetime

from entities.entity import Entity
from utils.tables import EXAMINATION, PATIENT, DOCTOR, T_SYMPTOM, T_SYMPTOM_TABLE, T_TREATMENT, T_TREATMENT_TABLE


@dataclass
class Examination(Entity):
    id: int = 0
    patient: int = 0
    doctor: int = 0
    examination_date: datetime = datetime.now()

    @property
    def table_name(self) -> str:
        return f"{EXAMINATION}"

    @property
    def columns(self) -> list:
        return [
            "id INTEGER PRIMARY KEY",
            "doctor INTEGER",
            "patient INTEGER",
            "examination_date TIMESTAMP NOT NULL",
            f"symptoms {T_SYMPTOM_TABLE}",
            f"treatments {T_TREATMENT_TABLE}",
            f"CONSTRAINT fk_pac_exa FOREIGN KEY (patient) REFERENCES {PATIENT}(id)",
            f"CONSTRAINT fk_doc_exa FOREIGN KEY (doctor) REFERENCES {DOCTOR}(id)"
        ]

    def generate_object(self):
        return textwrap.dedent(f"""\
            EXECUTE IMMEDIATE 'CREATE TYPE {T_SYMPTOM} AS OBJECT (
                symptom VARCHAR2(100),
                date_from DATE,
                date_to DATE
            )';
            
            EXECUTE IMMEDIATE 'CREATE TYPE {T_SYMPTOM_TABLE} AS TABLE OF {T_SYMPTOM}';
        
            
            EXECUTE IMMEDIATE 'CREATE TYPE {T_TREATMENT} AS OBJECT (
                treatment VARCHAR2(100),
                date_from DATE,
                date_to DATE
            )';
            
            EXECUTE IMMEDIATE 'CREATE TYPE {T_TREATMENT_TABLE} AS TABLE OF {T_TREATMENT}';
            \n\n""")

