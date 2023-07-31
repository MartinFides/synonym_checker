import json
import logging.config
from pathlib import Path
from typing import Iterator

from config import Settings
from config import get_file_path
from file_manager import FileManager
from model import SynonymsEvaluator
from type_alias import Data

logger = logging.getLogger(__name__)
CONFIG = "config.env"
LOGGING_SETTINGS = "logging.json"


def configure_logging(config: Path) -> None:
    if config.exists():
        with config.open() as f:
            loaded_config = json.load(f)
            logging.config.dictConfig(loaded_config)
    else:
        raise FileNotFoundError(f"Couldn't configure the logger using {config!r}")


def read_file(path_to_file: Path) -> Iterator[Data]:
    with FileManager(path_to_file) as file_manager:
        yield from file_manager.read_file()


def export_file(path_to_file: Path, data: list[list[str]]) -> None:
    with FileManager(path_to_file, "w") as file_manager:
        file_manager.export_file(data)


def main() -> None:
    logger.info(f"Reading configuration file: {CONFIG}")
    settings = Settings(_env_file=get_file_path(CONFIG), _env_file_encoding="utf-8")  # type: ignore[call-arg]

    logger.info(f"Reading data from file on path: {settings.resource_file_path}")
    raw_data = read_file(get_file_path(settings.resource_file_path))

    logger.info("Processing data")
    synonyms_evaluator = SynonymsEvaluator.process(raw_data)

    logger.info("Evaluating data")
    result = synonyms_evaluator.evaluate()

    logger.info(f"Exporting data to: {settings.export_file_path}")
    export_file(get_file_path(settings.export_file_path), result)


if __name__ == "__main__":
    configure_logging(get_file_path(LOGGING_SETTINGS))
    main()
