PYTHON:=$(VIRTUAL_ENV)/bin/python

test:
	@$(PYTHON) -m doctest *.py
	@$(PYTHON) -m unittest *.py

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name __pycache__ | xargs rm -fr {}

.PHONY: test clean
