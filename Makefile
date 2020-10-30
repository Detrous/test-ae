IMAGE = agileengine-test-task
TAG = latest

image:
	docker build -t $(IMAGE):$(TAG) .

run:
	docker run --rm -it -p 8080:8080 $(IMAGE):$(TAG)

style:
	isort src
	find src -name "*.py" -exec black -l 100 {} +

sync-req:
	pip3 freeze > requirements.txt