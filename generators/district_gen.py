from entities.district import District
from generators.base_gen import BaseGenerator
from utils.tables import DISTRICT
from utils.utils import read_from_json


class DistrictGenerator(BaseGenerator):
    def __init__(self):
        self.districts = []

    def generate_samples(self):
        self.districts = read_from_json("sources/districts.json", ["id", "code", "name", "region"], District)

        generated_inserts = []

        for district in self.districts:
            insert_string = f"EXECUTE IMMEDIATE 'insert into {DISTRICT} values({district.id}, ''{district.code}'', ''{district.name}'', {district.region})';"
            generated_inserts.append(insert_string)

        return generated_inserts

    def generate_schema(self):
        district = District()
        return super().create_schema(district.table_name, district.columns)
