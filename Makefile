SHELL=/bin/bash

docker:
	@echo "Building docker image"
	@docker build -t igorgov/auto-inc-ver:latest .

push:
	$(MAKE) docker
	@echo "Pushing docker image"
	@docker push igorgov/auto-inc-ver:latest

test:
	@pytest test_version.py
