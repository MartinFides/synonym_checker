from typing import Iterator

import pytest

from src.model import Case


def given_data() -> Iterator:
    data = (
        [
            "magic WaTCH\n",
            "uNdeRDog EartH\n",
            "EArTh caKE\n",
            "UnIforM baLance\n",
            "BALancE ABILity\n",
            "UnifORM uNIfORM\n",
            "maNagER WaTcH\n",
            "MaNagER MaNAGeR\n",
            "FaKe EaRth\n",
            "BAlance CAKe\n",
            "AbIliTY uNiFOrm\n",
            "UNdErdoG magiC\n",
        ],
        [
            "Magic MagIc\n",
            "Cake eArth\n",
            "aBIlITy abiLiTY\n",
            "watCh UniFoRM\n",
            "CAke FaKe\n",
            "FAkE watCh\n",
            "MagIC abIlitY\n",
            "uNIfoRm AbIlITY\n",
            "baLAnCe eaRtH\n",
            "bAlANCE MANAGER\n",
        ],
    )
    yield from data


@pytest.fixture(scope="function")
def actual() -> Case:
    return Case.process(given_data())


class TestCase:
    EXPECTED_DATA = Case(
        training_data=[
            ("ability", "balance", "cake", "earth", "fake", "magic", "manager", "underdog", "uniform", "watch")
        ],
        testing_data=[
            ("magic",),
            ("cake", "earth"),
            ("ability",),
            ("uniform", "watch"),
            ("cake", "fake"),
            ("fake", "watch"),
            ("ability", "magic"),
            ("ability", "uniform"),
            ("balance", "earth"),
            ("balance", "manager"),
        ],
    )

    def test_can_process_raw_data(self, actual: Case) -> None:
        assert actual == self.EXPECTED_DATA

    EXPECTED_RESULT = [
        "synonyms",
        "synonyms",
        "synonyms",
        "synonyms",
        "synonyms",
        "synonyms",
        "synonyms",
        "synonyms",
        "synonyms",
        "synonyms",
    ]

    def test_can_evaluate(self, actual: Case) -> None:
        actual = actual.evaluate()

        assert actual == self.EXPECTED_RESULT
