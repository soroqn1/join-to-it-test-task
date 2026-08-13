FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VERSION=2.0.0 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="$POETRY_HOME/bin:$PATH"

# Create non-root user for security
RUN addgroup --system appgroup && adduser --system --group appuser

WORKDIR /app

# Copy dependency files
COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN poetry install --no-interaction --no-ansi

# Copy project files
COPY . /app/

# Set ownership
RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
