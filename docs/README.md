# Documentation Index

Welcome to the project documentation. This repository follows an architecture-first approach.

## Structure

- [`CONTEXT.md`](./CONTEXT.md) - **Read this first.** Contains agent rules, tech stack, current phase, and DoD.
- [`architecture/`](./architecture/) - System design and technical architecture.
  - [`overview.md`](./architecture/overview.md) - High-level components and Django apps.
  - [`data-model.md`](./architecture/data-model.md) - Database schema, models, indexes, and constraints.
  - [`api-design.md`](./architecture/api-design.md) - REST API endpoints, search/filters, and responses.
- [`decisions/`](./decisions/) - Architecture Decision Records (ADRs).
  - [`0001-jwt-auth.md`](./decisions/0001-jwt-auth.md) - JWT Auth
  - [`0002-postgresql.md`](./decisions/0002-postgresql.md) - PostgreSQL
  - [`0003-email-celery.md`](./decisions/0003-email-celery.md) - Celery Emails
  - [`0004-drf-spectacular.md`](./decisions/0004-drf-spectacular.md) - OpenAPI & Swagger
  - [`TEMPLATE.md`](./decisions/TEMPLATE.md) - Template for new ADRs.
- [`phases/`](./phases/) - Implementation roadmap and phases.
  - [`README.md`](./phases/README.md) - Master plan from Phase 0 to 8 with DoD and status.
- [`reference/`](./reference/) - Reference materials.
  - [`task.md`](./reference/task.md) - Original test task description and interpretation.
  - [`environment.md`](./reference/environment.md) - Environment variables configuration.
