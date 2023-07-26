# BP_SYNONYMS

1. Initialise `pipenv` and install all the dependencies (if you omit `--dev` then only runtime dependencies will be installed):
    ```sh
    pipenv shell
    pipenv install --dev
    ```
    This will create a virtual environment in `~/.local/share/virtualenvs/`.

1. Install `pre-commit` hooks:
    ```sh
    pre-commit install -t pre-commit
    ```
