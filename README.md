# Synonym Checker
## Description
This program is designed to determine whether two words are synonyms or not, based on a given synonym dictionary.
The program follows specific rules to make this decision.

### Rules for Synonym Determination
1. If the pair of words is declared synonymous in the input, then they are synonyms.
2. Being synonyms doesn’t depend on order, e.g. if big is a synonym for large then large is a
synonym for big.
3. We can derive the synonymous relationship indirectly: if big is a synonym for large and large is a
synonym for huge then big is a synonym for huge.
4. If two words differ only by case, they are synonyms, e.g. same is a synonym for both SAmE and
SAME.
5. If none of the above rules can be used to decide whether two words are synonyms, then they
are not.

## Prerequisites
Before running the Synonym Checker program, ensure you have a supported system and the following prerequisites installed:

- `Ubuntu`: The program is developed and tested on Ubuntu, and it should work on other Linux distributions as well.
Ensure you have Ubuntu installed on your machine.

- `Python 3.11`: The program requires Python 3.11 to run.

- `pipenv`: The recommended way to manage dependencies for this project is using pipenv.
To install the latest version of pipenv, you can use pipx (recommended) or install it using your system Python.

Using pipx (recommended):
```shell
sudo apt-get -y install pipx
pipx install pipenv
```

## Installation
To install and run the app, follow these steps:
- Clone the repository:
```shell
  git clone https://github.com/MartinFides/synonym_checker.git
```
- Change project directory:
```shell
  cd synonym_checker
```
- Setup paths in `config.env` file if necessary (default):
```env
RESOURCE_FILE_PATH = "/test/resources/test.in"
EXPORT_FILE_PATH = "/result/test.out"
```
- Make sure install.sh and startup.sh are executable:
```shell
chmod +x install.sh
chmod +x startup.sh
```
- Run the installation script:
```shell
  ./install.sh
```
- Run the startup script:
```shell
  ./startup.sh
```

This will execute the main script and export the results into the `result` folder.

## License
This project is licensed under the [MIT License](LICENSE).

## Author
Martin Fides
