from entities.medicine import Medicine
from generators.base_gen import BaseGenerator
from utils.tables import *
from utils.utils import read_from_xlsx


class MedicineGenerator(BaseGenerator):
    def __init__(self):
        self.medicine = []

    def generate_samples(self):
        self.medicine = read_from_xlsx("sources/cast_I_abc_zoznam_liekov_N_k_01_12_2024.xlsx", ["Kód", "Názov", "Názov liečiva", "Doplnok", "JD", "ŠDL"], Medicine)

        generated_inserts = []

        for medicine in self.medicine:
            insert_string = f"EXECUTE IMMEDIATE 'insert into {MEDICINE} values(''{medicine.code}'', ''{medicine.name}'', ''{medicine.active_substance}'', ''{medicine.complement}'', ''{medicine.dosage_unit}'', {medicine.dosage_amount})';"
            generated_inserts.append(insert_string)

        return generated_inserts

    def generate_schema(self):
        medicine = Medicine()
        return super().create_schema(medicine.table_name, medicine.columns)

    def get_medicine(self):
        return self.medicine
