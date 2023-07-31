#!/usr/bin/env bash

function main() {
  pipenv install
  pipenv run python src/main.py
}

main
