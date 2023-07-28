from pathlib import Path
from typing import Iterator

from src.file_manager import FileManager
from src.model import SynonymsEvaluator
from src.type_alias import Data

FILE = Path(f"{Path(__file__).parent.parent}/test/resources/example.in")
EXPORTED_FILE = Path(f"{Path(__file__).parent.parent}/test/resources/example.out.out")


def read_file(path_to_file: Path) -> Iterator[Data]:
    with FileManager(path_to_file) as file_manager:
        yield from file_manager.read_file()


def export_file(path_to_file: Path, data: list[list[str]]) -> None:
    with FileManager(path_to_file, "w") as file_manager:
        file_manager.export_file(data)


def main() -> None:
    raw_data = read_file(FILE)
    synonyms_evaluator = SynonymsEvaluator.process(raw_data)
    result = synonyms_evaluator.evaluate()
    export_file(EXPORTED_FILE, result)


if __name__ == "__main__":
    main()
