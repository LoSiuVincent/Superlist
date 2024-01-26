runserver:
	poetry run python manage.py runserver 0.0.0.0:8000

test: unit-test functional-test

unit-test:
	poetry run python manage.py test lists

functional-test:
	poetry run python manage.py test functional_tests