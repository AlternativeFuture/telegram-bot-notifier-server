.PHONY: clean lint install devinstall

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROFILE = default
PROJECT_NAME = vehicle_fault_determination
PYTHON_INTERPRETER = python3

## Install Python Dependencies
install:
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt

devinstall: install
	$(PYTHON_INTERPRETER) -m pip install flake8 pytest pytest-cov

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using flake8
lint:
	flake8 src

test:
	pytest

test_report:
	pytest --cov src/

run:
	flask run --host=0.0.0.0



create_db:
	PGPASSWORD=postgres psql -h localhost -U postgres -w -c "CREATE DATABASE database;"

drop_db:
	PGPASSWORD=postgres psql -h localhost -U postgres -w -c "DROP DATABASE database;"

#create_table:
#	alembic revision -m "Create table"

migrate:
	alembic upgrade head

data_for_test:
	PGPASSWORD=postgres psql -h localhost -U postgres -w -d database -c "INSERT INTO identifier (product_id) VALUES (1234), (1200), (333), (4321);"
