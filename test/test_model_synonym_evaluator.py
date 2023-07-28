from typing import Iterator

import pytest

from src.model import SynonymsEvaluator


def given_data() -> Iterator:
    data = (
        (
            ["big large\n", "large huge\n", "small little\n", "apple banana\n"],
            ["same same\n", "big huge\n", "huge big\n", "apple peach\n", "big tall\n", "peach PEACH\n"],
        ),
        (
            ["wood FORest\n", "meadoW PrAirIe\n", "WOOD Lumber\n", "lumber forest\n", "lumber forest\n"],
            ["wood LUMBER\n", "mEADOw fire\n"],
        ),
    )
    yield from data


@pytest.fixture(scope="function")
def actual() -> SynonymsEvaluator:
    return SynonymsEvaluator.process(given_data())


class TestCase:
    EXPECTED_RESULT = [
        ["synonyms", "synonyms", "synonyms", "different", "different", "synonyms"],
        ["synonyms", "different"],
    ]

    def test_can_process_raw_data(self, actual: SynonymsEvaluator) -> None:
        assert len(actual.cases) == 2

    def test_can_evaluate(self, actual: SynonymsEvaluator) -> None:
        actual = actual.evaluate()

        assert actual == self.EXPECTED_RESULT
