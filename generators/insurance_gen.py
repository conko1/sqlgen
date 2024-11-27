from entities.insurance import Insurance
from generators.base_gen import BaseGenerator
from utils.tables import INSURANCE


class InsuranceGenerator(BaseGenerator):
    def __init__(self):
        self.insurances = []
        self.insurances_options = [
            (27, 'Union zdravotná poisťovňa'),
            (25, 'Všeobecná zdravotná poisťovňa'),
            (24, 'Dôvera zdravotná poisťovňa')
        ]

    def generate_samples(self):
        generated_inserts = []

        for insurance_option in self.insurances_options:
            insurance = Insurance()

            insurance.code = insurance_option[0]
            insurance.name = insurance_option[1]

            insert_string = f"EXECUTE IMMEDIATE 'insert into {INSURANCE} values({insurance.code}, ''{insurance.name}'')';"
            generated_inserts.append(insert_string)

            self.insurances.append(insurance)

        return generated_inserts

    def generate_schema(self):
        insurance = Insurance()
        return super().create_schema(insurance.table_name, insurance.columns)

    def get_insurances(self):
        return self.insurances
