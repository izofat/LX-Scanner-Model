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
	@poetry run mypy lx_scanner_model
	@poetry run mypy tests

lint:
	@poetry run pylint lx_scanner_model
	@poetry run pylint tests
	@poetry run bandit -r lx_scanner_model

launch:
	@poetry run lx-scanner-model
