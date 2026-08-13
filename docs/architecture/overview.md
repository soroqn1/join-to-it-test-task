# Architecture Overview

## Components

The system is a monolithic Django application providing a RESTful API, backed by PostgreSQL, with background processing via Celery and Redis.

- **Django Application**: Core API logic, DRF views, serializers, and models.
- **PostgreSQL**: Relational database for persistent storage.
- **Redis**: Message broker for Celery and caching (if needed).
- **Celery Worker**: Background task processor (primarily for email sending).

## Django Apps

The project is divided into focused Django apps:

### 1. `users`
Handles custom user model, authentication, and registration.
- Custom User model (email as primary identifier).
- JWT token generation and validation.

### 2. `events`
Core domain logic for events and registrations.
- `Event` model (title, description, date, location, organizer).
- `Registration` model (user, event, registration date).
- API endpoints for CRUD operations on events.
- API endpoints for joining/leaving events.
- Search and filtering logic.

## Cross-Cutting Solutions

- **Authentication**: JWT token attached to `Authorization: Bearer <token>` header.
- **Permissions**: DRF permission classes to ensure only organizers can edit/delete their events.
- **Pagination & Filtering**: Standard DRF pagination and `django-filter` for querying events.
- **Background Tasks**: Celery tasks triggered via Django signals or view logic when a user registers for an event.
- **Containerization**: Everything is packaged into Docker containers orchestrated via `docker-compose.yml`.
