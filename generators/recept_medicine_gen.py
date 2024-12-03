import copy
import random

from entities.recept_medicine import RecipeMedicine
from generators.base_gen import BaseGenerator
from utils.tables import RECIPE_MEDICINE


class RecipeMedicineGenerator(BaseGenerator):
    def __init__(self, recipe, medicine):
        self.recipe = recipe
        self.medicine = medicine

    def generate_samples(self):
        generated_inserts = []

        for recipe in self.recipe:
            medicine_copy = copy.deepcopy(self.medicine)
            medicine_count = random.randint(1, 3)

            for _ in range(medicine_count):
                medicine_index = random.randint(0, len(medicine_copy) - 1)
                medicine = medicine_copy[medicine_index]
                medicine_copy.pop(medicine_index)

                recipe_medicine = RecipeMedicine()

                recipe_medicine.recipe = recipe.id
                recipe_medicine.medicine = medicine.code

                insert_string = f"EXECUTE IMMEDIATE 'insert into {RECIPE_MEDICINE} values(''{recipe_medicine.medicine}'', {recipe_medicine.recipe})';"
                generated_inserts.append(insert_string)

        return generated_inserts

    def generate_schema(self):
        recipe_medicine = RecipeMedicine()
        return super().create_schema(recipe_medicine.table_name, recipe_medicine.columns)
