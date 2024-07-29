SHELL := /bin/bash
PROJECT_NAME := "LX-Scanner-Model"

install:
    @poetry install
	@poetry run mypy --install-types

format:
	@poetry run autoflake --in-place --remove-all-unused-imports --recursive --remove-unused-variables \
		--ignore-init-module-imports .
	@poetry run isort .
	@poetry run black .

type-check:
	@poetry run mypy src
	@poetry run mypy tests

lint:
	@poetry run pylint src
	@poetry run pylint tests
	@poetry run bandit -r src
