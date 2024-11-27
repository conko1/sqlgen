import random
import unicodedata

from datetime import datetime, timedelta, date

from entities.person import Person
from utils.tables import *
from faker import Faker
from generators.base_gen import BaseGenerator


class PersonGenerator(BaseGenerator):
    def __init__(self, cities):
        self.persons = []
        self.cities = cities
        self.faker = Faker('sk-SK')
        self.generated_phone_numbers = []
        self.generated_birth_numbers = []

    def generate_samples(self, number_of_samples):
        faker = Faker(['sk_SK'])

        generated_inserts = []

        for i in range(number_of_samples):
            gender = random.randint(0, 1)

            person = Person()

            person.birth_date = self.generate_birth_date()
            person.birth_number = self.generate_birth_number(person.birth_date, gender)
            person.telephone = self.generate_phone_number()

            city_index = random.randint(0, len(self.cities) - 1)
            city = self.cities[city_index]
            person.city = city.id

            person.street = self.faker.street_address()

            if gender == 1:
                # MUŽ
                person.first_name = faker.first_name_male()
                person.last_name = faker.last_name_male()
            else:
                # ŽENA
                person.first_name = faker.first_name_female()
                person.last_name = faker.last_name_female()

            person.email = self.generate_email(person.first_name, person.last_name)
            person.email = person.email.lower()
            person.email = self.remove_accents(person.email)

            insert_string = f"EXECUTE IMMEDIATE 'insert into {PERSON} values(''{person.birth_number}'', ''{person.first_name}'', ''{person.last_name}'', ''{person.telephone}'', ''{person.email}'', {person.city}, ''{person.street}'')';"
            generated_inserts.append(insert_string)

            self.persons.append(person)

        return generated_inserts

    def generate_schema(self):
        person = Person()
        return super().create_schema(person.table_name, person.columns)

    def generate_phone_number(self):
        while True:
            random_digits = [str(random.randint(0, 8)) for _ in range(9)]
            formatted_number = f"+421 9{random_digits[0]}{random_digits[1]} {random_digits[2]}{random_digits[3]}{random_digits[4]} {random_digits[5]}{random_digits[6]}{random_digits[7]}"

            if formatted_number not in self.generated_phone_numbers:
                self.generated_phone_numbers.append(formatted_number)
                return formatted_number

    def generate_birth_date(self):
        start_date = date(1955, 1, 1)
        end_date = date(1999, 1, 1)
        return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

    def generate_birth_number(self, date, gender):
        month = date.month
        year = date.year % 1900
        day = date.day

        if gender == 0:
            month += 50

        if month < 10:
            month = "0" + str(month)

        if day < 10:
            day = "0" + str(day)

        date_string = f"{year}{month}{day}"

        while True:
            random_numbers = str(random.randint(1000, 9999))

            result = date_string + "/" + random_numbers
            if result not in self.generated_birth_numbers:
                self.generated_birth_numbers.append(result)
                return result

    def get_persons(self):
        return self.persons

    def get_birth_numbers(self):
        return self.generated_birth_numbers

    def generate_email(self, first_name, last_name):
        emails = ["@gmail.com", "@azet.sk", "@pokec.sk", "@centrum.sk", "@zoznam.sk"]
        email_i = random.randint(0, len(emails) - 1)
        return f"{first_name}{last_name}{emails[email_i]}"

    def remove_accents(self, text):
        normalized = unicodedata.normalize('NFKD', text)
        return ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')
