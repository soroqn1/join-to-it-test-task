# Development Phases

This document outlines the step-by-step implementation plan.

## 🟢 Phase 0: Project Initialization & Architecture (Completed)
- [x] Define docs structure and architecture.
- [x] Initialize Python environment (`poetry`).
- [x] Install base dependencies (Django, DRF, Ruff, Just).
- [x] Setup initial Django project (`config`).
- [x] Setup Docker & `docker-compose.yml` with PostgreSQL 16 and Redis 7.
- [x] Setup `just pre-commit` pipeline.

## 🟢 Phase 1: Custom User & Authentication (Completed)
- [x] Create `users` app.
- [x] Implement custom User model (email-based).
- [x] Configure `simplejwt`.
- [x] Build `/auth/register/` and `/auth/login/` endpoints.
- [x] Tests for auth.

## 🟢 Phase 2: Events Core (Completed)
- [x] Create `events` app.
- [x] Implement `Event` model.
- [x] Build CRUD API endpoints for events.
- [x] Implement organizer permissions (only organizer can edit/delete).
- [x] Tests for event CRUD and permissions.

## 🟢 Phase 3: Registrations (Completed)
- [x] Implement `Registration` model with unique constraint.
- [x] Build join/leave API endpoints.
- [x] Tests for registration logic (prevent double join).

## 🟢 Phase 4: Search & Filtering (Completed)
- [x] Configure `django-filter`.
- [x] Add filters to event list (date, location, organizer).
- [x] Add search by title/description.
- [x] Tests for filtering.

## 🟢 Phase 5: Background Tasks (Celery) (Completed)
- [x] Configure Celery in Django.
- [x] Create email sending task.
- [x] Trigger task on successful event registration.
- [x] Add Celery worker to `docker-compose.yml`.
- [x] Tests for task dispatching.

## 🟢 Phase 6: API Documentation (Completed)
- [x] Install and configure `drf-spectacular`.
- [x] Annotate views and serializers where necessary.
- [x] Ensure Swagger UI is accessible and correct.

## 🟢 Phase 7: Polish & CI (Completed)
- [x] Final code review and `ruff` pass.
- [x] Ensure 80%+ test coverage.
- [x] Document environment variables.
- [x] Test clean Docker Compose up.

## 🟢 Phase 8: Delivery (Completed)
- [x] Complete `README.md` in project root with run instructions.
- [x] Verify all requirements from the task are met.
