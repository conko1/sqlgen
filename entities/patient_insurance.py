import textwrap
from dataclasses import dataclass

from entities.entity import Entity
from utils.tables import PATIENT_INSURANCE, PATIENT, INSURANCE, T_INSURANCE_HISTORY, T_INSURANCE_TABLE


@dataclass
class PatientInsurance(Entity):
    id: int = 0
    patient: int = 0
    insurance: int = 0

    @property
    def table_name(self) -> str:
        return f"{PATIENT_INSURANCE}"

    @property
    def columns(self) -> list:
        return [
            "id INTEGER PRIMARY KEY",
            "patient INTEGER",
            "insurance INTEGER",
            f"history {T_INSURANCE_TABLE}",
            f"CONSTRAINT fk_pac_ins FOREIGN KEY (patient) REFERENCES {PATIENT}(id)",
            f"CONSTRAINT fk_doc_ins FOREIGN KEY (insurance) REFERENCES {INSURANCE}(code)"
        ]

    def generate_object(self):
        return textwrap.dedent(f"""\
            EXECUTE IMMEDIATE 'CREATE TYPE {T_INSURANCE_HISTORY} AS OBJECT (
                insurance INTEGER,
                date_from DATE,
                date_to DATE
            )';
            EXECUTE IMMEDIATE 'CREATE TYPE {T_INSURANCE_TABLE} AS TABLE OF {T_INSURANCE_HISTORY}';
            """)
