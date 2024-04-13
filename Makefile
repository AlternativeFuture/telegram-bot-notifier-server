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

run_db_for_tests:
	docker run --rm --name prediction_db --net host -e POSTGRES_PASSWORD=aswa -e POSTGRES_USER=aswa -d postgres:15.6 && \
	echo "waiting for postgresql to start..." && \
	timeout 120 sh -c 'until nc -w 1 -z 127.0.0.1 5432; do sleep 1; done' 2> /dev/null && \
	docker exec prediction_db psql -h localhost -U aswa -c "CREATE DATABASE aswa_accident" && \
	docker exec -i prediction_db psql -h localhost -U aswa -d aswa_accident < db/dump/aswa_accident.sql && \
	docker exec prediction_db psql -h localhost -U aswa -c "CREATE DATABASE aswa_fault_determination" && \
	docker exec -i prediction_db psql -h localhost -U aswa -d aswa_fault_determination < db/dump/aswa_fault_determination.sql && \
	docker exec -i prediction_db psql -h localhost -U aswa -d aswa_accident < db/dump/aswa_accident_accident.sql && \
	docker exec -i prediction_db psql -h localhost -U aswa -d aswa_fault_determination < db/dump/aswa_fault.sql && \
	docker exec prediction_db psql -h localhost -U aswa -c "CREATE DATABASE training" && \
	docker exec -i prediction_db psql -h localhost -U aswa -d training < db/dump/training_metrics.sql

