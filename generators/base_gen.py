from abc import ABC, abstractmethod


class BaseGenerator(ABC):
    @abstractmethod
    def generate_samples(self, *args):
        pass

    @abstractmethod
    def generate_schema(self, *args):
        pass

    def create_schema(self, table_name, columns, objects="", nested_table=""):
        sql = objects
        sql += f"EXECUTE IMMEDIATE 'CREATE TABLE {table_name} (\n"
        sql += ",\n".join(f"    {col}" for col in columns)
        sql += f"\n){nested_table}';\n"

        return sql
