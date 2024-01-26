runserver:
	poetry run python manage.py runserver

test: unit-test functional-test

unit-test:
	poetry run python manage.py test lists

functional-test:
	poetry run python manage.py test functional_tests