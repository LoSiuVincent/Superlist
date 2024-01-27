runserver:
	poetry run python manage.py runserver 0.0.0.0:8000

test: unit-test functional-test

unit-test:
	poetry run python manage.py test lists

functional-test:
	poetry run python manage.py test functional_tests

stage-functional-test:
	STAGING_SERVER=ec2-3-27-169-52.ap-southeast-2.compute.amazonaws.com poetry run python manage.py test functional_tests