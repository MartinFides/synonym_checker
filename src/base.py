from abc import abstractmethod
from typing import Any
from typing import Iterator
from typing import Self


class BaseModel:
    @classmethod
    @abstractmethod
    def process(cls, raw: Iterator[Any]) -> Self:
        ...

    @abstractmethod
    def evaluate(self) -> list[Any]:
        ...
