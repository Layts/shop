lint:
	isort -y
	flake8 --config=.flake8
	pylint src
	mypy -p src --config-file mypy.ini
