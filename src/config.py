import subprocess
from pathlib import Path

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


def get_file_path(path_and_file_name: str) -> Path:
    """
    The function can be only run in a git repo or locally.
    """
    # Use git command to determine repo root.
    git_cmd_proc = subprocess.run(["git", "rev-parse", "--show-toplevel"], stdout=subprocess.PIPE)
    git_cmd_proc.check_returncode()
    repo_root = git_cmd_proc.stdout.decode().strip()

    return Path(f"{repo_root}/{path_and_file_name}")


class SettingsModel(BaseSettings):
    class Config:
        extra = "forbid"


class Settings(SettingsModel):
    resource_file_path: str = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")  # type: ignore[assignment]
    export_file_path: str = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")  # type: ignore[assignment]
