from dataclasses import dataclass

from entities.entity import Entity
from utils.tables import RECIPE_MEDICINE


@dataclass
class RecipeMedicine(Entity):
    medicine: int = 0
    recipe: int = 0

    @property
    def table_name(self) -> str:
        return f"{RECIPE_MEDICINE}"

    @property
    def columns(self) -> list:
        return [
            "medicine VARCHAR2(20)",
            "recipe INTEGER",
            "PRIMARY KEY (medicine, recipe)",
        ]
