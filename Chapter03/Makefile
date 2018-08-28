PYTHON:=$(VIRTUAL_ENV)/bin/python

test:
	@$(PYTHON) -m doctest *.py
	@$(PYTHON) -m unittest *.py

clean:
	find . -name "*.swp" -o -name "__pycache__" | xargs rm -fr

.PHONY: test clean
