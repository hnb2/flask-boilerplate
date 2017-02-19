SHELL:=/bin/bash
APP_DIR=./src/
all: install test

server:
	source env/bin/activate && cd $(APP_DIR) && python manage.py runserver

install:
	virtualenv env
	source env/bin/activate && pip install -r src/requirements.txt && pip install -r src/requirements-extra.txt && pip install -r src/tests/requirements.txt

test: lint test-unit

test-unit:
	source env/bin/activate && nosetests --with-coverage --cover-package=src -w $(APP_DIR)

lint:
	source env/bin/activate && flake8 $(APP_DIR)
