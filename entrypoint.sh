#!/bin/sh

# Install dependencies
poetry install --no-dev

# Run the FastAPI application with --reload
exec poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
