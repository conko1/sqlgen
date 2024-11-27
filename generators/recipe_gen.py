import random

from entities.recipe import Recipe
from generators.base_gen import BaseGenerator
from utils.tables import RECIPE


class RecipeGenerator(BaseGenerator):
    def __init__(self, examinations):
        self.recipes = []
        self.examinations = examinations

    def generate_samples(self):
        generated_inserts = []
        i = 0

        for examination in self.examinations:
            recipe_issued = random.random() < 0.7

            if not recipe_issued:
                continue

            count_of_recipes = random.randint(1, 2)

            for _ in range(count_of_recipes):
                i += 1
                recipe = Recipe()

                recipe.id = i
                recipe.patient = examination.patient
                recipe.doctor = examination.doctor
                recipe.used = random.random() < 0.95
                recipe.examination = examination.id

                insert_string = f"EXECUTE IMMEDIATE 'insert into {RECIPE} values({recipe.id}, {recipe.doctor}, {recipe.patient}, ''{recipe.used}'', {recipe.examination})';"
                generated_inserts.append(insert_string)

                self.recipes.append(recipe)

        return generated_inserts

    def generate_schema(self):
        recipe = Recipe()
        return super().create_schema(recipe.table_name, recipe.columns)

    def get_recipes(self):
        return self.recipes
