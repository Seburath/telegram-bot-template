test:
	pytest

dev:
	python3 -m bot

deploy:
	python3 -m bot

.PHONY: test, dev, deploy
