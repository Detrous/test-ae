style:
	isort src
	find src -name "*.py" -exec black -l 100 {} +

sync-req:
	pip3 freeze > requirements.txt