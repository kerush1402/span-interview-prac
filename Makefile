# Makefile

# Define your targets here
.PHONY: lint test install clean

# Linting
lint:
	@pylint src --max-line-length=88

# Testing (assuming you use pytest for testing)
test:
	@python3 -m pytest

# Clean generated files (e.g., bytecode, cache files, etc.)
clean:
	@find . -name "*.pyc" -exec rm -f {} \;
	@find . -name "__pycache__" -exec rm -r {} \;

run:
	@python3 main.py $(file)
