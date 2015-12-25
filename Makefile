build: test lint

test:
	nosetests tests

lint:
	flake8 convertfrom

requirements:
	pip freeze > requirements.txt

dev:
	pip install -r requirements.txt
	pip install -e .
