import random

from entities.doctor import Doctor
from utils.tables import *
from generators.base_gen import BaseGenerator


class DoctorGenerator(BaseGenerator):
    def __init__(self, persons):
        self.doctors = []
        self.persons = persons

    def generate_samples(self, number_of_samples):
        generated_inserts = []

        for i in range(number_of_samples):
            doctor = Doctor()

            doctor.id = i + 1

            person_index = random.randint(0, len(self.persons) - 1)
            doctor.birth_number = self.persons[person_index].birth_number
            del self.persons[person_index]

            insert_string = f"EXECUTE IMMEDIATE 'insert into {DOCTOR} values({doctor.id}, ''{doctor.birth_number}'')';"
            generated_inserts.append(insert_string)

            self.doctors.append(doctor)

        return generated_inserts

    def generate_schema(self):
        doctor = Doctor()
        return super().create_schema(doctor.table_name, doctor.columns)

    def get_doctors(self):
        return self.doctors

    def get_persons(self):
        return self.persons
