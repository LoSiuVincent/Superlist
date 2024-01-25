runserver:
	poetry run python manage.py runserver

unit-test:
	poetry run python manage.py test

functional-test:
	poetry run python tests/functional_tests.py