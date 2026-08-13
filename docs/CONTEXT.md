# Project Context

## Agent Rules & Development Workflow
- **Code Quality & Philosophy**: Code must be light, elegant, and modular ("всё по полочкам"). Scalability in mind. Zero bloat & zero speculation. Minimalist English comments.
- **Verification & Testing**: Run `just pre-commit` (or `just ruff` and `just test`) before committing. Ensure 0 errors.
- **Git Rules**: Local commits only. Stage only specific files. Do NOT push.
- **Closure**: Execute `/closetask` protocol on request.

## Stack Context
- **Framework**: Django, Django REST Framework (DRF)
- **Database**: PostgreSQL
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Background Tasks**: Celery + Redis (for email sending)
- **Documentation**: OpenAPI 3 + Swagger (drf-spectacular)
- **Infrastructure**: Docker & Docker Compose
- **Tooling**: Python `poetry`, `ruff`, `pytest`, `justfile`

## Project Description
A REST API backend for event management (conferences, meetups). 
Core functionality:
- User registration and JWT-based authentication.
- Event management (CRUD operations by the organizer).
- Event registration (users can participate in events).
- Search and filtering for events.
- Background email notifications upon event registration.

## Current Phase
**Phase 0: Project Initialization & Architecture Design** (See `docs/phases/README.md`)

## Definition of Done (DoD)
- Feature is implemented without speculative code.
- Covered by tests (80%+ coverage).
- Passed `ruff` linting and formatting.
- Documented in Swagger.
- Environment variables are defined.
- Works correctly in Docker.
