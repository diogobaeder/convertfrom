build: test lint

test:
	nosetests tests

lint:
	flake8 convertfrom tests

requirements:
	pip freeze | grep -v convertfrom > requirements.txt

dev:
	pip install -r requirements.txt
	pip install -e .
