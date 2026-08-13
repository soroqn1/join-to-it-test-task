# Data Model

## Entity Relationship Diagram

```mermaid
erDiagram
    User ||--o{ Event : "organizes"
    User ||--o{ Registration : "registers for"
    Event ||--o{ Registration : "has"

    User {
        int id PK
        string email UK
        string password
        string first_name
        string last_name
        datetime date_joined
    }

    Event {
        int id PK
        string title
        text description
        datetime date
        string location
        int organizer_id FK
        datetime created_at
        datetime updated_at
    }

    Registration {
        int id PK
        int user_id FK
        int event_id FK
        datetime registered_at
    }
```

## Models & Constraints

### User
Custom user model using `email` as the unique identifier (`USERNAME_FIELD`).
- **Indexes**: `email` (unique, b-tree).

### Event
Represents a conference, meetup, or other gathering.
- `organizer`: ForeignKey to `User`, `on_delete=CASCADE`.
- **Indexes**:
  - `date` (for sorting and filtering).
  - `location` (for filtering).
  - `organizer` (for filtering).
  - Standard b-tree indexes for basic lookups.

### Registration
Mapping table linking Users to Events they are participating in.
- `user`: ForeignKey to `User`, `on_delete=CASCADE`.
- `event`: ForeignKey to `Event`, `on_delete=CASCADE`.
- **Constraints**: 
  - `UniqueConstraint` on `(user, event)` to prevent double registration.
