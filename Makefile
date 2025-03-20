.PHONY: v-env
v-env:
	@echo "Creating virtual environment..."
	@python3 -m venv venv

.PHONY: install-reqs
install-reqs:
	@echo "Installing requirements..."
	@pip3 install -r requirements.txt

.PHONY: tests
tests:
	@echo "Running tests..."
	@python3 -m pytest tests

.PHONY: help
help:
	@echo "v-env:         --> Create virtual environment"
	@echo "install-reqs:  --> Install requirements"
	@echo "test:          --> Run tests"
	@echo "help:          --> Show this help message"
