from pathlib import Path
from typing import Iterator

from config import Settings
from config import get_file_path
from file_manager import FileManager
from model import SynonymsEvaluator
from type_alias import Data


def read_file(path_to_file: Path) -> Iterator[Data]:
    with FileManager(path_to_file) as file_manager:
        yield from file_manager.read_file()


def export_file(path_to_file: Path, data: list[list[str]]) -> None:
    with FileManager(path_to_file, "w") as file_manager:
        file_manager.export_file(data)


def main() -> None:
    settings = Settings(_env_file=get_file_path("config.env"), _env_file_encoding="utf-8")

    raw_data = read_file(get_file_path(settings.resource_file_path))
    synonyms_evaluator = SynonymsEvaluator.process(raw_data)
    result = synonyms_evaluator.evaluate()
    export_file(get_file_path(settings.export_file_path), result)


if __name__ == "__main__":
    main()
