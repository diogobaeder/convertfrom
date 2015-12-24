build: test

test:
	nosetests tests

requirements:
	pip freeze > requirements.txt

dev:
	pip install -r requirements.txt
	pip install -e .
