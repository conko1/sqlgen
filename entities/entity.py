from abc import abstractmethod
from dataclasses import dataclass


@dataclass
class Entity:
    @property
    @abstractmethod
    def table_name(self) -> str:
        pass

    @property
    @abstractmethod
    def columns(self) -> list:
        pass
