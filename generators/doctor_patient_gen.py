from entities.doctor_patient import DoctorPatient
from generators.base_gen import BaseGenerator
from utils.tables import *


class DoctorPatientGenerator(BaseGenerator):
    def __init__(self, doctors, patients):
        self.doctor_patients = []
        self.doctors = doctors
        self.patients = patients

    def generate_samples(self):
        generated_inserts = []

        doctors_len = len(self.doctors)
        patient_len = len(self.patients)

        blocks = int(patient_len / doctors_len)
        remainder = patient_len - (blocks * doctors_len)

        for i in range(doctors_len):
            for j in range(blocks):
                doctor_patient = DoctorPatient()

                patient_index = i * blocks + j

                doctor_patient.doctor = self.doctors[i].id
                doctor_patient.patient = self.patients[patient_index].id

                insert_string = f"EXECUTE IMMEDIATE 'insert into {DOCTOR_PATIENT} values({doctor_patient.doctor}, {doctor_patient.patient})';"
                generated_inserts.append(insert_string)

                self.doctor_patients.append(doctor_patient)

        for i in range(remainder):
            doctor_patient = DoctorPatient()

            doctor_patient.doctor = self.doctors[i].id
            doctor_patient.patient = self.patients[i].id

            insert_string = f"EXECUTE IMMEDIATE 'insert into {DOCTOR_PATIENT} values({doctor_patient.doctor}, {doctor_patient.patient})';"
            generated_inserts.append(insert_string)

            self.doctor_patients.append(doctor_patient)

        return generated_inserts

    def generate_schema(self):
        doctor_patient = DoctorPatient()
        return super().create_schema(doctor_patient.table_name, doctor_patient.columns)

    def get_doctor_patient(self):
        return self.doctor_patients
