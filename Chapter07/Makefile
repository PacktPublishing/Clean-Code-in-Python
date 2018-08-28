PYTHON:=$(VIRTUAL_ENV)/bin/python

clean:
	find . -name "*.swp" -o -name "__pycache__" | xargs rm -fr

test:
	@$(PYTHON) -m doctest *.py
	@$(PYTHON) -m unittest *.py

typehint:
	@mypy *.py

.PHONY: clean test
