import pytest

from src.type_alias import Synonyms
from src.util import merge_synonyms
from src.util import merge_synonyms_list

SYNONYMS = [
    ([("apple", "fruit"), ("big", "large")], ("banana", "fruit"), [("apple", "banana", "fruit"), ("big", "large")]),
    (
        [("apple", "fruit"), ("orange", "fruit", "citrus")],
        ("banana", "fruit"),
        [("apple", "banana", "fruit"), ("orange", "fruit", "citrus")],
    ),
]


class TestMergeSynonyms:
    @pytest.mark.parametrize("existing, new, expected", SYNONYMS)
    def test_can_merge_synonyms(self, existing: list[Synonyms], new: Synonyms, expected: list[Synonyms]) -> None:
        actual = merge_synonyms(existing, new)

        assert actual == expected


SYNONYMS_LIST = [
    (
        [("apple", "fruit"), ("orange", "fruit", "citrus"), ("banana", "fruit")],
        [("apple", "banana", "citrus", "fruit", "orange")],
    ),
    (
        [("big", "large", "huge"), ("small", "little"), ("apple", "banana")],
        [("big", "huge", "large"), ("little", "small"), ("apple", "banana")],
    ),
]


class TestMergeSynonymsList:
    @pytest.mark.parametrize("given, expected", SYNONYMS_LIST)
    def test_can_merge_synonyms(self, given: list[Synonyms], expected: list[Synonyms]) -> None:
        actual = merge_synonyms_list(given)

        assert actual == expected
