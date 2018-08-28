typehint:
	mypy --ignore-missing-imports src/

test:
	pytest tests/

lint:
	pylint src/

checklist: lint typehint test

black:
	black -l 79 *.py

setup:
	$(VIRTUAL_ENV)/bin/pip install -r requirements.txt

.PHONY: typehint test lint checklist black
