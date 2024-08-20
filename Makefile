SHELL := /bin/bash
PROJECT_NAME := LX-Scanner-API
CURDIR := $(shell pwd)
PATH_IMAGE ?= $(CURDIR)/tests/data/testocr.png
LANGUAGE_IMAGE ?= en

POETRY := ~/.local/bin/poetry

launch:
	@poetry run lx-scanner-model

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

test:
	@echo $(PATH) $(LANG)
	@$(POETRY) run lx-scanner-model-test -p "$(PATH_IMAGE)" -l "$(LANGUAGE_IMAGE)"
