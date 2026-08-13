# Environment Variables

The project uses environment variables for configuration, managed via `.env` files locally or passed through Docker.

## Database (PostgreSQL)
- `POSTGRES_DB`: Name of the database (e.g., `events_db`)
- `POSTGRES_USER`: Database user (e.g., `events_user`)
- `POSTGRES_PASSWORD`: Database password
- `POSTGRES_HOST`: Database host (e.g., `db` in docker, `localhost` locally)
- `POSTGRES_PORT`: Database port (default: `5432`)

## Redis & Celery
- `REDIS_URL`: Redis connection string (e.g., `redis://redis:6379/0`)

## Django Core
- `DJANGO_SECRET_KEY`: Secret key for cryptographic operations.
- `DJANGO_DEBUG`: `True` for development, `False` for production.
- `DJANGO_ALLOWED_HOSTS`: Comma-separated list of allowed hosts (e.g., `localhost,127.0.0.1`).

## Email Settings (SMTP)
- `EMAIL_HOST`: SMTP server host
- `EMAIL_PORT`: SMTP server port
- `EMAIL_HOST_USER`: SMTP username
- `EMAIL_HOST_PASSWORD`: SMTP password
- `EMAIL_USE_TLS`: `True` / `False`
- `DEFAULT_FROM_EMAIL`: Sender email address
