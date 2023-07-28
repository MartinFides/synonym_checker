from dataclasses import dataclass
from typing import Any
from typing import Iterator
from typing import Self

from src.base import BaseModel
from src.type_alias import Data
from src.type_alias import Synonyms
from src.util import merge_synonyms
from src.util import merge_synonyms_list


@dataclass
class Case(BaseModel):
    training_data: list[Synonyms]
    testing_data: list[Data]

    @classmethod
    def _compose_training_data(cls, data: Iterator[str]) -> list[Synonyms]:
        result: list[Synonyms] = []

        for x in data:
            entries = tuple(x.strip().lower().split())
            result = merge_synonyms(result, entries)

        return merge_synonyms_list(result)

    @staticmethod
    def _compose_testing_data(data: Iterator[str]) -> list[Data]:
        return [tuple(sorted(set(x.strip().lower().split()))) for x in data]

    @classmethod
    def process(cls, raw: Iterator[Any]) -> Self:
        raw_training_data, raw_testing_data = raw

        return cls(
            training_data=cls._compose_training_data(raw_training_data),
            testing_data=cls._compose_testing_data(raw_testing_data),
        )

    def evaluate(self) -> list[str]:
        result = []

        for x in self.testing_data:
            if len(x) == 1:
                result.append("synonyms")
                continue

            for y in self.training_data:
                if all(val in y for val in x):
                    result.append("synonyms")
                    break

            else:
                result.append("different")

        return result


@dataclass
class SynonymsEvaluator(BaseModel):
    cases: list[Case]

    @classmethod
    def process(cls, raw: Iterator[Any]) -> Self:
        return cls(cases=[Case.process(x) for x in raw])

    def evaluate(self) -> list[list[str]]:
        return [x.evaluate() for x in self.cases]
