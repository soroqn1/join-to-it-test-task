# ADR 0004: OpenAPI 3 Documentation with drf-spectacular

**Date:** 2026-08-13
**Status:** Accepted

## Context
The API needs interactive documentation for clients (frontend/mobile devs) and testing.

## Decision
We will use `drf-spectacular` to auto-generate OpenAPI 3 schemas and serve a Swagger UI interface.

## Consequences
- **Pros:** Auto-generated from DRF serializers, stays up-to-date with code, interactive Swagger UI out of the box.
- **Cons:** May require explicit decorators (`@extend_schema`) for complex endpoints.
- **Implementation:** Available at `/api/docs/` (Swagger UI) and `/api/schema/` (OpenAPI JSON/YAML).
