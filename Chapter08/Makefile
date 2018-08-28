CASE:=1
PYTHON:=$(VIRTUAL_ENV)/bin/python

setup:
	$(VIRTUAL_ENV)/bin/pip install -r requirements.txt

test:
	@$(PYTHON) -m doctest *.py
	@$(VIRTUAL_ENV)/bin/pytest .

clean:
	find . -type d -name __pycache__ | xargs rm -fr {}
	rm -fr .coverage .pytest_cache/ .hypothesis/

coverage:
	bash run-coverage.sh $(CASE)

mutation:
	bash mutation-testing.sh $(CASE)


.PHONY: test clean mutation coverage setup
