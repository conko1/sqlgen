from entities.city import City
from generators.base_gen import BaseGenerator
from utils.tables import CITY
from utils.utils import read_from_json


class CityGenerator(BaseGenerator):
    def __init__(self):
        self.cities = []

    def generate_samples(self):
        self.cities = read_from_json("sources/villages.json", ["id", "zip", "fullname", "shortname", "district"], City)

        generated_inserts = []

        for city in self.cities:
            insert_string = f"EXECUTE IMMEDIATE 'insert into {CITY} values({city.id}, ''{city.zip}'', ''{city.name}'', ''{city.short_name}'', {city.district})';"
            generated_inserts.append(insert_string)

        return generated_inserts

    def generate_schema(self):
        city = City()
        return super().create_schema(city.table_name, city.columns)

    def get_cities(self):
        return self.cities
