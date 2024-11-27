import random

from entities.patient_allergy import PatientAllergy
from generators.base_gen import BaseGenerator
from utils.tables import PATIENT_ALLERGY


class PatientAllergyGenerator(BaseGenerator):
    def __init__(self, patients, allergies):
        self.patients = patients
        self.allergies = allergies

    def generate_samples(self):
        generated_inserts = []

        for patient in self.patients:
            allergy_count = random.randint(0, 4)
            allergies = []

            for _ in range(allergy_count):

                while True:
                    already_used = False
                    allergy_index = random.randint(0, len(self.allergies) - 1)
                    allergy_generated = self.allergies[allergy_index]

                    for allergy in allergies:
                        if allergy.id == allergy_generated.id:
                            already_used = True

                    if not already_used:
                        break

                patient_allergy = PatientAllergy(patient.id, allergy_generated.id)

                allergies.append(allergy_generated)

                insert_string = f"EXECUTE IMMEDIATE 'insert into {PATIENT_ALLERGY} values({patient_allergy.patient}, {patient_allergy.allergy})';"
                generated_inserts.append(insert_string)

        return generated_inserts

    def generate_schema(self):
        patient_allergy = PatientAllergy()
        return super().create_schema(patient_allergy.table_name, patient_allergy.columns)
