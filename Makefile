.PHONY: build push

build:
	docker-compose build app

push:
	docker push joanfont/well-played-slack