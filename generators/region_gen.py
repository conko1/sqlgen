from entities.region import Region
from generators.base_gen import BaseGenerator
from utils.tables import REGION
from utils.utils import read_from_json


class RegionGenerator(BaseGenerator):
    def __init__(self):
        self.regions = []

    def generate_samples(self):
        self.regions = read_from_json("sources/regions.json", ["id", "name", "shortcut"], Region)

        generated_inserts = []

        for region in self.regions:
            insert_string = f"EXECUTE IMMEDIATE 'insert into {REGION} values({region.id}, ''{region.name}'', ''{region.abbr}'')';"
            generated_inserts.append(insert_string)

        return generated_inserts

    def generate_schema(self):
        region = Region()
        return super().create_schema(region.table_name, region.columns)
