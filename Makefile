SHELL=/bin/bash

export SEM_VER?=v0.0.0

docker:
	@echo "Building docker image"
	@docker build -t igorgov/auto-inc-ver:$(SEM_VER) -t igorgov/auto-inc-ver:latest .

push:
	$(MAKE) docker
	@echo "Pushing docker image"
	@docker push igorgov/auto-inc-ver:latest
	@docker push igorgov/auto-inc-ver:$(SEM_VER)

test:
	@pytest test_version.py
