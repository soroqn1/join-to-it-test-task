# Justfile for join-to-it-test-task

default:
    @just --list

# Install dependencies
install:
    poetry install

# Run Django development server
dev:
    poetry run python manage.py runserver

# Database migrations
migrate:
    poetry run python manage.py migrate

# Make database migrations
makemigrations:
    poetry run python manage.py makemigrations

# Run linter and formatter check
ruff:
    poetry run ruff check .
    poetry run ruff format --check .

# Auto-fix linting and formatting issues
fix:
    poetry run ruff check --fix .
    poetry run ruff format .

# Run pytest suite
test:
    poetry run pytest

# Pre-commit pipeline (lint + test)
pre-commit: ruff test

# Start Docker environment
docker-up:
    docker compose up --build

# Stop Docker environment
docker-down:
    docker compose down -v
