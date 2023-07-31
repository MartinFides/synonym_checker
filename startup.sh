#!/usr/bin/env bash

function main() {
  pipenv shell
  pipenv install
  pipenv run python src/main.py
}

main
