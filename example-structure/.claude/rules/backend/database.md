# Database Rules

Guidelines for database design and queries.

## Schema Design

Standard table structure:

```sql
CREATE TABLE users (
  id          SERIAL PRIMARY KEY,
  email       VARCHAR(255) UNIQUE NOT NULL,
  name        VARCHAR(100) NOT NULL,
  role        VARCHAR(50) DEFAULT 'user',
  created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

| Column | Requirement |
|--------|-------------|
| `id` | Primary key (auto-increment or UUID) |
| `created_at` | Always include |
| `updated_at` | Always include |
| Foreign keys | Define constraints for integrity |

## Query Patterns

```typescript
// Good - parameterized query
const user = await db.query(
  'SELECT id, name, email FROM users WHERE id = $1',
  [userId]
)

// Bad - SQL injection risk
const user = await db.query(
  `SELECT * FROM users WHERE id = ${userId}`
)
```

**Rules:**
- Always parameterize user input
- Avoid `SELECT *`—list required columns
- Use indexes on WHERE, JOIN, ORDER BY columns
- Monitor slow query logs

## Migrations

| Rule | Description |
|------|-------------|
| Versioned | All changes via migration files |
| Reversible | Include up and down migrations |
| Atomic | One logical change per migration |
| Tested | Test on production data copy first |

```bash
# Migration naming convention
migrations/
├── 001_create_users_table.sql
├── 002_add_user_role_column.sql
└── 003_create_posts_table.sql
```

## Transactions

Use transactions for atomic operations:

```typescript
await db.transaction(async (tx) => {
  const order = await tx.insert(orders).values(orderData)
  await tx.insert(orderItems).values(itemsData)
  await tx.update(inventory).decrement('stock', quantity)
  // All succeed or all rollback
})
```

**Connection rules:**
- Use connection pooling
- Configure pool size for concurrency
- Implement retry logic for failures
- Always release connections properly