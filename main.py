from generators.allergy_gen import AllergyGenerator
from generators.city_gen import CityGenerator
from generators.district_gen import DistrictGenerator
from generators.doctor_patient_gen import DoctorPatientGenerator
from generators.examination_gen import ExaminationGenerator
from generators.insurance_gen import InsuranceGenerator
from generators.medicine_gen import MedicineGenerator
from generators.patient_allergy_gen import PatientAllergyGenerator
from generators.patient_insurance_gen import PatientInsuranceGenerator
from generators.recept_medicine_gen import RecipeMedicineGenerator
from generators.recipe_gen import RecipeGenerator
from generators.region_gen import RegionGenerator
from utils.utils import create_sql_file

from generators.person_gen import PersonGenerator
from generators.doctor_gen import DoctorGenerator
from generators.patient_gen import PatientGenerator

city_gen = CityGenerator()
city_gen_sample = city_gen.generate_samples()
city_gen_schema = city_gen.generate_schema()

region_gen = RegionGenerator()
region_gen_sample = region_gen.generate_samples()
region_gen_schema = region_gen.generate_schema()

district_gen = DistrictGenerator()
district_gen_sample = district_gen.generate_samples()
district_gen_schema = district_gen.generate_schema()

person_numbers = 12500
doctor_numbers = 500
patient_numbers = person_numbers - doctor_numbers

person_gen = PersonGenerator(city_gen.get_cities())
person_sample = person_gen.generate_samples(person_numbers)
person_schema = person_gen.generate_schema()

doctor_gen = DoctorGenerator(person_gen.get_persons())
doctor_sample = doctor_gen.generate_samples(doctor_numbers)
doctor_schema = doctor_gen.generate_schema()

patient_gen = PatientGenerator(doctor_gen.get_persons())
patient_sample = patient_gen.generate_samples(patient_numbers)
patient_schema = patient_gen.generate_schema()

doctor_patient_gen = DoctorPatientGenerator(doctor_gen.get_doctors(), patient_gen.get_patients())
doctor_patient_gen_sample = doctor_patient_gen.generate_samples()
doctor_patient_gen_schema = doctor_patient_gen.generate_schema()

medicine_gen = MedicineGenerator()
medicine_gen_sample = medicine_gen.generate_samples()
medicine_gen_schema = medicine_gen.generate_schema()

allergy_gen = AllergyGenerator()
allergy_gen_sample = allergy_gen.generate_samples()
allergy_gen_schema = allergy_gen.generate_schema()

patient_allergy_gen = PatientAllergyGenerator(patient_gen.get_patients(), allergy_gen.get_allergies())
patient_allergy_gen_sample = patient_allergy_gen.generate_samples()
patient_allergy_gen_schema = patient_allergy_gen.generate_schema()

examination_gen = ExaminationGenerator(doctor_patient_gen.get_doctor_patient())
examination_gen_sample = examination_gen.generate_samples()
examination_gen_schema = examination_gen.generate_schema()

recipe_gen = RecipeGenerator(examination_gen.get_examinations())
recipe_gen_sample = recipe_gen.generate_samples()
recipe_gen_schema = recipe_gen.generate_schema()

recipe_medicine_gen = RecipeMedicineGenerator(recipe_gen.get_recipes(), medicine_gen.get_medicine())
recipe_medicine_gen_sample = recipe_medicine_gen.generate_samples()
recipe_medicine_gen_schema = recipe_medicine_gen.generate_schema()

insurance_gen = InsuranceGenerator()
insurance_gen_sample = insurance_gen.generate_samples()
insurance_gen_schema = insurance_gen.generate_schema()

patient_insurance_gen = PatientInsuranceGenerator(patient_gen.get_patients(), insurance_gen.get_insurances())
patient_insurance_gen_sample = patient_insurance_gen.generate_samples()
patient_insurance_gen_schema = patient_insurance_gen.generate_schema()

# create_sql_file(person_sample, person_schema, "person")
# create_sql_file(doctor_sample, doctor_schema, "doctor")
# create_sql_file(patient_sample, patient_schema, "patient")
# create_sql_file(doctor_patient_gen_sample, doctor_patient_gen_schema, "doctor_patient")
# create_sql_file(medicine_gen_sample, medicine_gen_schema, "medicine")
# create_sql_file(city_gen_sample, city_gen_schema, "city")
# create_sql_file(region_gen_sample, region_gen_schema, "region")
# create_sql_file(district_gen_sample, district_gen_schema, "district")
# create_sql_file(allergy_gen_sample, allergy_gen_schema, "allergy")
# create_sql_file(patient_allergy_gen_sample, patient_allergy_gen_schema, "patient_allergy")
create_sql_file(examination_gen_sample, examination_gen_schema, "examination")
create_sql_file(recipe_gen_sample, recipe_gen_schema, "recipe")
create_sql_file(recipe_medicine_gen_sample, recipe_medicine_gen_schema, "recipe_medicine")
# create_sql_file(insurance_gen_sample, insurance_gen_schema, "insurance")
# create_sql_file(patient_insurance_gen_sample, patient_insurance_gen_schema, "patient_insurance")
