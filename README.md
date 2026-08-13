# Event Management REST API

Production-ready Django REST Framework backend for organizing and registering for events.

## Features

- **Custom Email-based Authentication**: JWT authentication (`djangorestframework-simplejwt`).
- **Events Management**: Full CRUD operations with `IsOrganizerOrReadOnly` permissions.
- **Event Registrations**: Join/leave events with database-enforced unique constraints.
- **Search & Filtering**: Filter events by date, location, organizer, and search by keywords (`django-filter`).
- **Asynchronous Email Notifications**: Background email confirmation on registration powered by **Celery** and **Redis**.
- **Interactive API Documentation**: Auto-generated OpenAPI 3 schema and Swagger UI (`drf-spectacular`).
- **Dockerized Infrastructure**: Entire application stack (Django + PostgreSQL 16 + Redis 7 + Celery Worker) orchestrated via `docker-compose.yml`.

---

## Quick Start (Docker)

Run the entire application stack with a single command:

```bash
docker compose up --build
```

- **Swagger UI**: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)
- **OpenAPI Schema**: [http://localhost:8000/api/schema/](http://localhost:8000/api/schema/)
- **API Base URL**: `http://localhost:8000/api/v1/`

---

## Local Development (without Docker)

### Prerequisites

- Python 3.12+
- [Poetry](https://python-poetry.org/)
- [Just](https://github.com/casey/just)

### Installation

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Copy environment file:
   ```bash
   cp .env.example .env
   ```

3. Run migrations and dev server:
   ```bash
   just migrate
   just dev
   ```

---

## Useful Commands (via `just`)

- `just install` — Install dependencies.
- `just dev` — Run Django development server.
- `just migrate` — Apply database migrations.
- `just makemigrations` — Create new database migrations.
- `just ruff` — Run Ruff linter and formatter check.
- `just fix` — Auto-fix linting and formatting issues with Ruff.
- `just test` — Run pytest suite.
- `just pre-commit` — Run full pre-commit pipeline (`ruff` + `test`).
- `just docker-up` — Build and launch Docker Compose services.

---

## API Endpoints Overview

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| `POST` | `/api/v1/auth/register/` | Register new user | No |
| `POST` | `/api/v1/auth/login/` | Obtain JWT access/refresh tokens | No |
| `POST` | `/api/v1/auth/refresh/` | Refresh access token | No |
| `GET` / `PUT` | `/api/v1/users/me/` | User profile | Yes |
| `GET` | `/api/v1/events/` | List events (supports `?search=`, `?location=`, `?date=`, `?organizer=`) | Yes |
| `POST` | `/api/v1/events/` | Create new event | Yes |
| `GET` | `/api/v1/events/{id}/` | Retrieve event details | Yes |
| `PUT` / `PATCH` | `/api/v1/events/{id}/` | Update event (Organizer only) | Yes |
| `DELETE` | `/api/v1/events/{id}/` | Delete event (Organizer only) | Yes |
| `POST` | `/api/v1/events/{id}/register/` | Join event | Yes |
| `DELETE` | `/api/v1/events/{id}/register/` | Cancel registration | Yes |
