# Base image with Python and Poetry
FROM python:3.10-slim AS base

# Copy the project files
COPY pyproject.toml poetry.lock ./

# Install project dependencies with Poetry
RUN pip install --no-cache-dir --disable-pip-version-check --root-user-action=ignore poetry>=1.5.1 \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

ENTRYPOINT ["poetry", "run", "python" "main.py"]
