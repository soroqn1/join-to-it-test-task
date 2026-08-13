# ADR 0002: PostgreSQL as Primary Database

**Date:** 2026-08-13
**Status:** Accepted

## Context
The application needs a reliable, ACID-compliant relational database to store users, events, and registrations.

## Decision
We will use PostgreSQL.

## Consequences
- **Pros:** Robust, excellent support in Django, supports advanced indexing, handles concurrency well.
- **Cons:** Requires a separate service in Docker Compose.
- **Implementation:** Handled via `psycopg` database adapter in Django.
