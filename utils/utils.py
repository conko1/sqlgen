import json
import os
import random
from datetime import timedelta

import openpyxl

from typing import List, Callable, TypeVar

T = TypeVar('T')


def create_sql_file(inserts, schema=None, filename="output", file_index=1, row_limit=3000):
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../output")

    os.makedirs(output_dir, exist_ok=True)

    filepath = os.path.join(output_dir, f"{filename}.sql")

    with open(filepath, "w") as sql_file:
        sql_file.write("BEGIN" + "\n")
        if schema is not None:
            sql_file.write(schema + "\n")
        for row_num, insert in enumerate(inserts):
            sql_file.write(insert + "\n")
        sql_file.write("END" + "\n" + "/")

    print(f"SQL file '{filename}{file_index}.sql' has been created successfully.")

# def create_sql_file(inserts, schema=None, filename="output", file_index=1, max_file_size=500000):
#     output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../output")
#     os.makedirs(output_dir, exist_ok=True)
#
#     filepath = os.path.join(output_dir, f"{filename}{file_index}.sql")
#     with open(filepath, "w") as sql_file:
#         current_size = 0
#
#         if schema is not None:
#             sql_file.write(schema + "\n")
#             current_size += len(schema.encode("utf-8")) + 1
#
#         for insert in inserts:
#             insert_size = len(insert.encode("utf-8")) + 1
#             if current_size + insert_size > max_file_size:
#                 print(f"SQL file '{filename}{file_index}.sql' has been created successfully.")
#                 return create_sql_file(inserts[inserts.index(insert):], filename=filename,
#                                        file_index=file_index + 1, max_file_size=max_file_size)
#
#             sql_file.write(insert + "\n")
#             current_size += insert_size
#
#     print(f"SQL file '{filename}{file_index}.sql' has been created successfully.")


def read_from_xlsx(file_path: str, columns_to_retrieve: List[str], cls: Callable[..., T]) -> List[T]:
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    headers = [cell.value for cell in sheet[1]]

    column_indices = {col: headers.index(col) for col in columns_to_retrieve if col in headers}

    if len(column_indices) != len(columns_to_retrieve):
        missing_cols = set(columns_to_retrieve) - set(column_indices.keys())
        raise ValueError(f"Columns not found in file: {', '.join(missing_cols)}")

    objects = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        try:
            col_values = [row[column_indices[col]] for col in columns_to_retrieve]

            obj = cls(*col_values)
            objects.append(obj)
        except Exception as e:
            print(f"Error processing row {row}: {e}")

    return objects


def read_from_json(file_path: str, keys_to_retrieve: List[str], cls: Callable[..., T]) -> List[T]:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise ValueError("JSON data must be an array of objects.")

        objects = []
        for obj in data:
            try:
                values = [obj[key] for key in keys_to_retrieve]

                instance = cls(*values)
                objects.append(instance)
            except KeyError as e:
                print(f"Key {e} not found in object {obj}. Skipping this entry.")
            except Exception as e:
                print(f"Error processing object {obj}: {e}")

        return objects
    except Exception as e:
        print(f"An error occurred while reading from JSON: {e}")
        return []


def generate_random_number(nums, weights):
    return random.choices(nums, weights=weights)[0]


def split_timeframe(start_date, end_date, num_splits):
    if num_splits == 0:
        return [(start_date, end_date)]

    total_days = (end_date - start_date).days
    split_points = sorted(random.sample(range(1, total_days), num_splits))

    intervals = []
    previous_date = start_date
    for point in split_points:
        split_date = start_date + timedelta(days=point)
        intervals.append((previous_date, split_date))
        previous_date = split_date

    intervals.append((previous_date, end_date))

    return intervals
