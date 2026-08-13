# ADR 0003: Background Email Processing with Celery & Redis

**Date:** 2026-08-13
**Status:** Accepted

## Context
When a user registers for an event, the system must send a confirmation email. Sending emails synchronously within the request-response cycle blocks the API response and degrades user experience.

## Decision
We will use Celery as the asynchronous task queue and Redis as the message broker.

## Consequences
- **Pros:** Fast API responses, fault tolerance (failed emails can be retried).
- **Cons:** Increases infrastructure complexity (requires Redis and Celery Worker containers).
- **Implementation:** Email tasks will be queued via `.delay()` when a registration record is created.
