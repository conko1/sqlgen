import random

from entities.patient import Patient
from utils.tables import *
from generators.base_gen import BaseGenerator


class PatientGenerator(BaseGenerator):
    def __init__(self, persons):
        self.patients = []
        self.persons = persons

    def generate_samples(self, number_of_samples):
        generated_inserts = []

        for i in range(number_of_samples):
            patient = Patient()

            patient.id = i + 1

            blood_type_index = random.randint(0, len(patient.blood_type_options) - 1)
            blood_type = patient.blood_type_options[blood_type_index]

            patient.blood_type = blood_type

            person_index = random.randint(0, len(self.persons) - 1)
            person = self.persons[person_index]
            patient.birth_number = person.birth_number
            patient.birth_date = person.birth_date
            del person

            insert_string = f"EXECUTE IMMEDIATE 'insert into {PATIENT} values({patient.id}, ''{patient.birth_number}'', ''{patient.blood_type}'')';"
            generated_inserts.append(insert_string)

            self.patients.append(patient)

        return generated_inserts

    def generate_schema(self):
        patient = Patient()
        return super().create_schema(patient.table_name, patient.columns)

    def get_patients(self):
        return self.patients
