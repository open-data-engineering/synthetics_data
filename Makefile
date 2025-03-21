.PHONY: create-env
create-env:
	@echo "Creating virtual environment..."
	@python3 -m venv venv

.PHONY: activate-env
activate-env:
	@echo "Activating virtual environment..."
	@source venv/bin/activate

.PHONY: install-reqs
install-reqs:
	@echo "Installing requirements..."
	@pip3 install -r requirements.txt
	@pip3 install -r requirements-dev.txt

.PHONY: tests
tests:
	@echo "Running tests..."
	@PYTHONPATH=. pytest tests -v

.PHONY: lint
lint:
	@echo "Running linter..."
	@mypy src/ --config-file mypy.ini

.PHONY: help
help:
	@echo "create-env:    --> Create virtual environment"
	@echo "activate-env:  --> Activate virtual environment"
	@echo "install-reqs:  --> Install requirements"
	@echo "tests:         --> Run tests"
	@echo "lint:          --> Run linter"
	@echo "help:          --> Show this help message"
