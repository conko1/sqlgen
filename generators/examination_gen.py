import random
import textwrap
from datetime import datetime, timedelta, date

from entities.examination import Examination
from generators.base_gen import BaseGenerator
from utils.tables import EXAMINATION, T_SYMPTOM_TABLE, T_SYMPTOM, T_TREATMENT_TABLE, T_TREATMENT
from utils.utils import generate_random_number, split_timeframe


class ExaminationGenerator(BaseGenerator):
    def __init__(self, doctor_patient):
        self.examinations = []
        self.doctor_patient = doctor_patient

    def generate_samples(self):
        generated_inserts = []
        i = 0

        for doctor_patient in self.doctor_patient:
            count_of_examinations = random.randint(1, 3)

            for _ in range(count_of_examinations):
                i += 1
                examination = Examination()

                examination.id = i
                examination.patient = doctor_patient.patient
                examination.doctor = doctor_patient.doctor
                generated_date = self.random_past_datetime_within_hours()
                examination.examination_date = generated_date.strftime('%Y-%m-%d %H:%M:%S')

                examination_formatted = f"TO_DATE(''{examination.examination_date}'', ''YYYY-MM-DD HH24:MI:SS'')"

                symptom_changes = generate_random_number([1, 2], [80, 20])

                symptoms_history_entries = []
                for _ in range(symptom_changes):
                    days_delta = random.randint(3, 7)

                    from_date = f"TO_DATE(''{(generated_date - timedelta(days=days_delta)).strftime('%Y-%m-%d')}'', ''YYYY-MM-DD'')"
                    to_date = f"TO_DATE(''{generated_date.strftime('%Y-%m-%d')}'', ''YYYY-MM-DD'')"

                    symptom_index = random.randint(0, len(self.symptoms()) - 1)
                    symptom = self.symptoms()[symptom_index]

                    history_entry = f"{T_SYMPTOM}(''{symptom}'', {from_date}, {to_date})"

                    symptoms_history_entries.append(history_entry.rstrip())

                symptoms_history_list = ", ".join(symptoms_history_entries)
                symptoms_history_list = textwrap.dedent(f"""{symptoms_history_list}""")

                treatment_changes = generate_random_number([1, 2], [90, 10])

                treatments_history_entries = []
                for _ in range(treatment_changes):
                    days_delta = random.randint(3, 6)

                    from_date = f"TO_DATE(''{generated_date.strftime('%Y-%m-%d')}'', ''YYYY-MM-DD'')"
                    to_date = f"TO_DATE(''{(generated_date + timedelta(days=days_delta)).strftime('%Y-%m-%d')}'', ''YYYY-MM-DD'')"

                    treatment_index = random.randint(0, len(self.treatments()) - 1)
                    treatment = self.treatments()[treatment_index]

                    history_entry = f"{T_TREATMENT}(''{treatment}'', {from_date}, {to_date})"
                    treatments_history_entries.append(history_entry.rstrip())

                treatments_history_list = ", ".join(treatments_history_entries)
                treatments_history_list = textwrap.dedent(f"""{treatments_history_list}""")

                insert_string = textwrap.dedent(
                    f"""EXECUTE IMMEDIATE 'insert into {EXAMINATION} values({examination.id}, {examination.doctor}, {examination.patient}, {examination_formatted}, 
                                            {T_SYMPTOM_TABLE}(
                                                {symptoms_history_list}
                                            ),
                                            {T_TREATMENT_TABLE}(
                                                {treatments_history_list}
                                            ))';""")
                generated_inserts.append(insert_string)

                self.examinations.append(examination)

        return generated_inserts

    def generate_schema(self):
        examination = Examination()

        nested_table = " NESTED TABLE symptoms STORE AS symptoms_table\nNESTED TABLE treatments STORE AS symptoms_history_table"

        return super().create_schema(
            examination.table_name,
            examination.columns,
            examination.generate_object(),
            nested_table
        )

    def get_examinations(self):
        return self.examinations

    def random_past_datetime_within_hours(self, start_hour=8, end_hour=16):
        now = datetime.now()

        time_delta = timedelta(days=365 * 3)

        random_seconds = random.randint(0, int(time_delta.total_seconds()))

        random_past_date = now - timedelta(seconds=random_seconds)

        random_hour = random.randint(start_hour, end_hour)
        random_minute = random.randint(0, 59)

        random_past_date = random_past_date.replace(hour=random_hour, minute=random_minute, second=0, microsecond=0)

        return random_past_date

    def symptoms(self):
        return [
            "Horúčka",
            "Bolesť hlavy",
            "Kašeľ",
            "Dýchavičnosť",
            "Únava",
            "Zimnica",
            "Potenie (nočné potenie)",
            "Bolesť svalov (myalgia)",
            "Bolesť kĺbov (artralgia)",
            "Nevoľnosť",
            "Zvracanie",
            "Hnačka",
            "Zápcha",
            "Bolesť brucha",
            "Pálenie záhy",
            "Nadúvanie",
            "Strata chuti do jedla",
            "Strata hmotnosti",
            "Priberanie na hmotnosti",
            "Vyrážky",
            "Svrbenie kože",
            "Suchá koža",
            "Žlté sfarbenie kože (žltačka)",
            "Modriny bez zjavnej príčiny",
            "Opuchy (edém)",
            "Bledosť kože",
            "Zrýchlený tep (tachykardia)",
            "Pomalý tep (bradykardia)",
            "Bolesť na hrudi",
            "Pískanie pri dýchaní",
            "Krvácanie z nosa",
            "Zápach z úst",
            "Zmeny v chuti alebo čuchu",
            "Bolesti hrdla",
            "Zväčšené lymfatické uzliny",
            "Krvácanie z ďasien",
            "Zvonenie v ušiach (tinnitus)",
            "Poruchy sluchu",
            "Závraty",
            "Poruchy rovnováhy",
            "Rozmazané videnie",
            "Citlivosť na svetlo (fotofóbia)",
            "Dvojité videnie",
            "Očné začervenanie",
            "Svrbenie očí",
            "Poruchy spánku (insomnia)",
            "Nadmerná spavosť (hypersomnia)",
            "Nervozita",
            "Depresia",
            "Úzkosť",
            "Zmätenosť",
            "Halucinácie",
            "Pamäťové problémy",
            "Poruchy koncentrácie",
            "Brnenie (parestézia)",
            "Necitlivosť končatín",
            "Slabosť končatín",
            "Svalové kŕče",
            "Svalová stuhnutosť",
            "Tras (tremor)",
            "Problémy s močením (časté alebo bolestivé močenie)",
            "Krv v moči (hematúria)",
            "Zápach moču",
            "Hnis v moči",
            "Sexuálna dysfunkcia",
            "Nepravidelný menštruačný cyklus",
            "Bolestivá menštruácia (dysmenorea)",
            "Nadmerné krvácanie počas menštruácie",
            "Návaly horúčavy",
            "Nočné potenie (najmä u menopauzy)",
            "Bolesti krížov",
            "Bolesť v oblasti panvy",
            "Citlivosť prsníkov",
            "Zmeny tvaru alebo veľkosti prsníkov",
            "Výtok z prsníkov",
            "Krvácanie z konečníka",
            "Hemoroidy",
            "Svrbenie konečníka",
            "Neschopnosť prehĺtať (dysfágia)",
            "Bolesti v hornej časti brucha po jedle",
            "Kyselina v ústach",
            "Krvácanie z tráviaceho traktu (meléna alebo hemateméza)",
            "Tuhé stolice",
            "Tukové stolice (steatorhea)",
            "Nadmerný smäd",
            "Nadmerné močenie (polyúria)",
            "Sucho v ústach",
            "Rýchle chudnutie",
            "Zmeny vo farbe kože (napr. tmavé škvrny pri Addisonovej chorobe)",
            "Zväčšenie štítnej žľazy (struma)",
            "Nadmerné potenie",
            "Problémy s termoreguláciou (studené ruky/nohy)",
            "Znížená odolnosť voči chladu",
            "Znížená odolnosť voči teplu",
            "Kŕče po fyzickej aktivite",
            "Kožné vredy",
            "Náhla slabosť alebo ochrnutie jednej strany tela (príznaky mŕtvice)",
            "Krvácanie mimo menštruácie",
            "Zhoršenie sluchu s bolesťou",
            "Modré pery alebo nechty (cyanóza)"
        ]

    def treatments(self):
        return [
            "Odpočinok",
            "Zlepšenie spánkového režimu",
            "Zvýšenie príjmu vody",
            "Obmedzenie stresu",
            "Relaxačné techniky (napr. meditácia, joga)",
            "Dýchacie cvičenia",
            "Pravidelné cvičenie (podľa fyzickej kondície)",
            "Krátke prechádzky na čerstvom vzduchu",
            "Používanie ergonomického nábytku",
            "Vyhýbanie sa nadmernej fyzickej námahe",
            "Pravidelné prestávky pri práci s počítačom",
            "Správne držanie tela",
            "Zlepšenie stravovacích návykov",
            "Zvýšenie príjmu vlákniny",
            "Zníženie príjmu cukru",
            "Obmedzenie mastných jedál",
            "Vyhýbanie sa koreneným jedlám",
            "Zníženie príjmu soli",
            "Konzumácia viac ovocia a zeleniny",
            "Zaradenie orechov a semien do stravy",
            "Dodržiavanie pravidelného stravovacieho režimu",
            "Pomalé a dôkladné žuvanie jedla",
            "Vyhýbanie sa jedeniu tesne pred spaním",
            "Obmedzenie konzumácie alkoholu",
            "Zákaz fajčenia",
            "Vyhýbanie sa pasívnemu fajčeniu",
            "Pravidelné umývanie rúk",
            "Používanie dezinfekčných prostriedkov",
            "Zabezpečenie dostatočného vetrania miestností",
            "Zníženie vystavenia alergénom",
            "Používanie zvlhčovača vzduchu",
            "Vyhýbanie sa klimatizovaným priestorom",
            "Nosové výplachy fyziologickým roztokom",
            "Denný pobyt na slnku (ale s ochranou pred UV žiarením)",
            "Používanie opaľovacieho krému",
            "Používanie ochranných pomôcok (napr. rúško v prašnom prostredí)",
            "Nosenie pohodlného a vhodného oblečenia",
            "Dodržiavanie hygieny nôh",
            "Pravidelná návšteva stomatológa",
            "Pravidelné očné prehliadky",
            "Kontrola sluchu",
            "Vyhýbanie sa hlučnému prostrediu",
            "Používanie ochranných štupľov do uší",
            "Dodržiavanie pracovných prestávok",
            "Vyhýbanie sa nočnej práci (ak je to možné)",
            "Pravidelné strečingové cvičenia",
            "Znižovanie hmotnosti (ak je potrebné)",
            "Monitorovanie krvného tlaku",
            "Udržiavanie normálnej hladiny cukru v krvi",
            "Udržiavanie primeranej hladiny cholesterolu",
            "Samovyšetrenie prsníkov alebo semenníkov",
            "Zapisovanie symptómov do denníka",
            "Obmedzenie používania mobilných zariadení pred spaním",
            "Nastavenie pravidelného denného režimu",
            "Pravidelný kontakt s rodinou a priateľmi",
            "Hľadanie podporných skupín alebo terapie",
            "Dobrovoľníctvo (ako spôsob znižovania stresu)",
            "Zapojenie sa do záľub a koníčkov",
            "Obmedzenie sledovania negatívnych správ",
            "Plánovanie dovolenky alebo oddychového času",
            "Vyhýbanie sa rizikovým činnostiam (napr. skákanie z výšok)",
            "Používanie bezpečnostných pásov",
            "Používanie prilby pri jazde na bicykli",
            "Dodržiavanie dopravných predpisov",
            "Pravidelné kontrolné návštevy u lekára",
            "Dávkovanie času stráveného na slnku",
            "Vyhýbanie sa zdvíhaniu ťažkých bremien",
            "Používanie správnej techniky zdvíhania",
            "Cvičenia na posilnenie panvového dna",
            "Vyhýbanie sa dlhodobému státiu",
            "Používanie protišmykovej obuvi",
            "Dodržiavanie bezpečnosti pri práci s chemikáliami",
            "Ochrana pred hmyzom (napr. repelenty)",
            "Používanie hydratačných krémov na pokožku",
            "Vyhýbanie sa parfumovaným výrobkom (pri citlivej koži)",
            "Minimalizácia používania plastových fliaš",
            "Pitná voda z overených zdrojov",
            "Vyhýbanie sa surovým potravinám (ak sú rizikové)",
            "Pravidelné sledovanie hmotnosti",
            "Používanie prírodných sladidiel",
            "Dodržiavanie pitného režimu pri fyzickej aktivite",
            "Používanie ergonomického batohu",
            "Vyhýbanie sa multitaskingu pri riadení",
            "Záznam rodinnej anamnézy",
            "Upravenie prostredia na zníženie rizika pádu",
            "Obmedzenie kofeínu",
            "Používanie teplých alebo studených obkladov",
            "Zlepšenie osvetlenia pracovného priestoru",
            "Dodržiavanie pauz pri čítaní",
            "Využívanie masáže na uvoľnenie svalov",
            "Používanie výplachov úst pri problémoch s ďasnami",
            "Zníženie používania hlasu pri bolesti hrdla",
            "Minimalizácia času stráveného v hlučnom prostredí",
            "Cvičenie jemnej motoriky (napr. písanie, skladanie)",
            "Pravidelný pohyb na zlepšenie cirkulácie",
            "Udržiavanie správnej telesnej teploty (vyhýbanie sa prechladeniu)",
            "Zlepšenie domácich bezpečnostných opatrení",
            "Udržiavanie optimistického prístupu",
            "Vyhľadanie odbornej psychologickej pomoci (ak treba)",
            "Zúčastňovanie sa na preventívnych prehliadkach a skríningoch"
        ]
