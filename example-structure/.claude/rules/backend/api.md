# API Rules

Guidelines for backend API development.

## Endpoint Design

Follow RESTful conventions:

| Method | Purpose | Example |
|--------|---------|---------|
| GET | Retrieve resources | `GET /api/users` |
| POST | Create resource | `POST /api/users` |
| PUT | Replace resource | `PUT /api/users/123` |
| PATCH | Partial update | `PATCH /api/users/123` |
| DELETE | Remove resource | `DELETE /api/users/123` |

**URL conventions:**
- Lowercase with hyphens: `/api/user-profiles`
- Plural nouns for collections: `/api/users`
- Version prefix: `/api/v1/users`

## Response Format

Standard success response:

```json
{
  "data": { ... },
  "meta": {
    "total": 100,
    "page": 1,
    "limit": 20
  }
}
```

Standard error response:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "details": { "field": "email" }
  }
}
```

## Status Codes

| Code | Usage |
|------|-------|
| 200 | Success |
| 201 | Created |
| 204 | No content (successful delete) |
| 400 | Bad request / validation error |
| 401 | Unauthorized (not logged in) |
| 403 | Forbidden (no permission) |
| 404 | Not found |
| 500 | Server error |

## Authentication

```typescript
// Protect routes with middleware
export default defineEventHandler(async (event) => {
  const user = await requireAuth(event)  // throws 401 if invalid

  // User is authenticated
  return { user }
})
```

**Rules:**
- Protect all non-public endpoints
- Use JWT with appropriate expiration
- Validate permissions at route level
- Never trust client-provided identity