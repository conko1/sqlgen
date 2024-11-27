from entities.allergy import Allergy
from generators.base_gen import BaseGenerator
from utils.tables import ALLERGY


class AllergyGenerator(BaseGenerator):
    def __init__(self):
        self.allergies = []

        for i, allergy in enumerate(self.allergy_options()):
            id = i + 1
            self.allergies.append(Allergy(id, allergy))

    def generate_samples(self):
        generated_inserts = []

        for allergy in self.allergies:
            insert_string = f"EXECUTE IMMEDIATE 'insert into {ALLERGY} values({allergy.id}, ''{allergy.type}'')';"
            generated_inserts.append(insert_string)

        return generated_inserts

    def generate_schema(self):
        allergy = Allergy()
        return super().create_schema(allergy.table_name, allergy.columns)

    def get_allergies(self):
        return self.allergies

    def allergy_options(self):
        return [
            "Laktóza",
            "Kazeín",
            "Srvátka",
            "Bielok",
            "Žĺtok",
            "Losos",
            "Tuniak",
            "Krevety",
            "Mušle",
            "Homáre",
            "Arašidy",
            "Lieskové",
            "Mandle",
            "Vlašské",
            "Kešu",
            "Pekanové",
            "Tofu",
            "Sójové Mlieko",
            "Sójová Omáčka",
            "Celiakia",
            "Neceliakálna Gluténová Senzitivita",
            "Banány",
            "Jablká",
            "Kivi",
            "Broskyne",
            "Jahody",
            "Avokádo",
            "Škorica",
            "Cesnak",
            "Zázvor",
            "Aníz",
            "Kari",
            "Glutamát Sodný",
            "Siričitany",
            "Benzoany",
            "Tartrazín",
            "Breza",
            "Jelša",
            "Topoľ",
            "Javor",
            "Borovica",
            "Timotejka",
            "Kostrava",
            "Lipnica",
            "Ambrózia",
            "Palina",
            "Púpava",
            "Psi",
            "Mačky",
            "Hlodavce",
            "Perie",
            "Roztoče",
            "Papierový Prach",
            "Skladové Plesne",
            "Alternaria",
            "Cladosporium",
            "Aspergillus",
            "Penicillium",
            "Lieky",
            "Penicilín",
            "Amoxicilín",
            "Cefalosporíny",
            "Sulfónamidy",
            "Aspirín",
            "Ibuprofén",
            "Naproxén",
            "Lidokaín",
            "Prokaín",
            "Včely",
            "Osy",
            "Sršne",
            "Mravce",
            "Šváby",
            "Komáre",
            "Nikel",
            "Chróm",
            "Kobalt",
            "Rukavice",
            "Balóniky",
            "Kondómy",
            "Parabény",
            "Formaldehyd",
            "Benzofenóny",
            "Bielidlá",
            "Amoniak",
            "Surfaktanty",
            "Jedovatý Brečtan",
            "Žihľava",
            "Kaučukovník",
            "Potravinové Intolerancie",
            "Laktózová Intolerancia",
            "Fruktózová Malabsorpcia",
            "Salicyláty",
            "Latex",
            "Drevo",
            "Fotosenzitívna Dermatitída",
            "Ozón",
            "Smog",
            "Aquagenická Urtikária",
            "Cholinergická Urtikária",
            "Dermografizmus Alebo Tlaková Urtikária"
        ]
