# ADR 0001: JSON Web Token (JWT) Authentication

**Date:** 2026-08-13
**Status:** Accepted

## Context
The API needs a stateless authentication mechanism suitable for various clients (SPA, Mobile apps, Postman).

## Decision
We will use JWT (JSON Web Tokens) via the `djangorestframework-simplejwt` package for authentication.

## Consequences
- **Pros:** Stateless, easily scalable, supported by all major clients, built-in expiration.
- **Cons:** Cannot be invalidated easily before expiration (requires token blocklisting if strict invalidation is needed).
- **Implementation:** Clients must include `Authorization: Bearer <token>` in headers.
