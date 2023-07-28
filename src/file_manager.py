import itertools
from pathlib import Path
from typing import Any
from typing import Iterator
from typing import Self


class FileManager:
    def __init__(self, filename: Path, mode: str = "r") -> None:
        """
        Initialize the FileManager.

        Parameters:
            filename (Path): The path to the file to be managed.
            mode (str, optional): The file opening mode. Defaults to 'r'.
        """
        self.filename = filename
        self.mode = mode

    def __enter__(self) -> Self:
        """
        Enter the context of the FileManager.
        """
        self.file = open(self.filename, self.mode)  # noqa: SIM115
        return self

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None:
        """
        Exit the context of the FileManager and close the file.
        """
        self.file.close()

    def read_file(self) -> Iterator[Any]:
        """
        Read the file and yield data for each test case.

        Yields:
            Iterator[Any]: An iterator that produces a tuple of data for each test case,
                           where each tuple contains two lists of strings.
        """
        test_cases = int(self.file.readline().strip())

        for _ in range(test_cases):
            yield self._get_data(), self._get_data()

    def export_file(self, data: list[list[str]]) -> None:
        """
        Export data to the file.

        Parameters:
            data (List[List[str]]): A list of lists of strings to be written to the file.
        """
        for entries in data:
            for entry in entries:
                line = "".join(entry) + "\n"
                self.file.write(line)

    # Private method
    def _get_data(self) -> list[str]:
        """
        Read data from the file.

        Returns:
            List[str]: A list of strings representing the data read from the file.
        """
        num_lines = int(self.file.readline().strip())
        return list(itertools.islice(self.file, num_lines))
