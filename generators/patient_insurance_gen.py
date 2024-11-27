import random
import textwrap
from datetime import date

from entities.patient_insurance import PatientInsurance
from generators.base_gen import BaseGenerator
from utils.tables import PATIENT_INSURANCE, T_INSURANCE_TABLE, T_INSURANCE_HISTORY
from utils.utils import generate_random_number, split_timeframe


class PatientInsuranceGenerator(BaseGenerator):
    def __init__(self, patients, insurances):
        self.patients = patients
        self.insurances = insurances

    def generate_samples(self):
        generated_inserts = []

        for i, patient in enumerate(self.patients):
            patient_insurance = PatientInsurance()

            insurance_index = random.randint(0, len(self.insurances) - 1)
            insurance = self.insurances[insurance_index]

            patient_insurance.id = i + 1
            patient_insurance.patient = patient.id
            patient_insurance.insurance = insurance.code

            insurance_changes = generate_random_number([0, 1], [85, 15])
            insurance_periods = split_timeframe(patient.birth_date, date.today(), insurance_changes)

            used_insurances = [insurance]

            insurance_history_entries = []
            for j, period in enumerate(insurance_periods):
                start, end = period
                start_formatted = f"TO_DATE(''{start}'', ''YYYY-MM-DD'')"
                end_formatted = f"TO_DATE(''{end}'', ''YYYY-MM-DD'')"

                insurance_history = insurance
                if j != 0:
                    while True:
                        insurance_history_index = random.randint(0, len(self.insurances) - 1)
                        tmp_insurance_history = self.insurances[insurance_history_index]

                        if tmp_insurance_history not in used_insurances:
                            insurance_history = tmp_insurance_history
                            used_insurances.append(insurance_history)
                            break

                history_entry = f"{T_INSURANCE_HISTORY}({insurance_history.code}, {start_formatted}, {end_formatted})"

                insurance_history_entries.append(history_entry.rstrip())

            insurance_history_list = ", ".join(insurance_history_entries)
            insurance_history_list = textwrap.dedent(f"""{insurance_history_list}""")

            insert_string = textwrap.dedent(
                f"""EXECUTE IMMEDIATE 'insert into {PATIENT_INSURANCE} values({patient_insurance.id}, {patient_insurance.patient}, {patient_insurance.insurance}, 
                            {T_INSURANCE_TABLE}(
                                {insurance_history_list}
                            ))';""")

            generated_inserts.append(insert_string)

        return generated_inserts

    def generate_schema(self):
        patient_insurance = PatientInsurance()

        nested_table = " NESTED TABLE history STORE AS insurance_history_table"

        return super().create_schema(
            patient_insurance.table_name,
            patient_insurance.columns,
            patient_insurance.generate_object(),
            nested_table
        )
