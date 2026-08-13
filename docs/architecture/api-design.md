# API Design

The API follows RESTful principles and is documented via OpenAPI 3.

## Endpoints

### Authentication (`/api/v1/auth/`)
- `POST /api/v1/auth/register/` - Register a new user (returns user details).
- `POST /api/v1/auth/login/` - Obtain JWT tokens (access, refresh).
- `POST /api/v1/auth/refresh/` - Refresh JWT access token.

### Events (`/api/v1/events/`)
- `GET /api/v1/events/` - List events (requires authentication). Supports search and filters.
- `POST /api/v1/events/` - Create a new event (requires authentication). Current user becomes the organizer.
- `GET /api/v1/events/{id}/` - Retrieve event details.
- `PUT/PATCH /api/v1/events/{id}/` - Update event (Must be organizer).
- `DELETE /api/v1/events/{id}/` - Delete event (Must be organizer).

### Registrations (`/api/v1/events/{id}/register/`)
- `POST /api/v1/events/{id}/register/` - Join an event. (Authenticated). Triggers email notification.
- `DELETE /api/v1/events/{id}/register/` - Cancel registration. (Authenticated).

## Search and Filtering (for `GET /api/v1/events/`)
- `?search=<query>` - Search by title or description.
- `?date=<YYYY-MM-DD>` - Filter by specific date.
- `?date__gte=<...>&date__lte=<...>` - Filter by date range.
- `?location=<query>` - Filter by location.
- `?organizer=<user_id>` - Filter by organizer.

## Standard Responses
- `200 OK` / `201 Created` - Success.
- `400 Bad Request` - Validation error (returns field-specific errors).
- `401 Unauthorized` - Missing or invalid JWT token.
- `403 Forbidden` - User is not the organizer (for edit/delete).
- `404 Not Found` - Resource does not exist.
