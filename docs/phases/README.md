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

## ⚪ Phase 5: Background Tasks (Celery)
- [ ] Configure Celery in Django.
- [ ] Create email sending task.
- [ ] Trigger task on successful event registration.
- [ ] Add Celery worker to `docker-compose.yml`.
- [ ] Tests for task dispatching.

## ⚪ Phase 6: API Documentation
- [ ] Install and configure `drf-spectacular`.
- [ ] Annotate views and serializers where necessary.
- [ ] Ensure Swagger UI is accessible and correct.

## ⚪ Phase 7: Polish & CI
- [ ] Final code review and `ruff` pass.
- [ ] Ensure 80%+ test coverage.
- [ ] Document environment variables.
- [ ] Test clean Docker Compose up.

## ⚪ Phase 8: Delivery
- [ ] Complete `README.md` in project root with run instructions.
- [ ] Verify all requirements from the task are met.
