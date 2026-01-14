# General Rules

Guidelines that apply across all code in this repository.

## Code Style

- Write clear, self-documenting code that prioritizes readability
- Use descriptive variable and function names that convey intent
- Keep functions small and focused on a single task
- Follow the principle of least surprise: code should behave as readers expect

```typescript
// Good
function calculateOrderTotal(items: OrderItem[]): number

// Bad
function calc(arr: any[]): number
```

## Version Control

| Action | Rule |
|--------|------|
| Commits | Atomic, focused on single logical changes |
| Messages | Explain why, not just what |
| Branches | Feature branches for new development |
| Main | Always deployable |

**Never commit:** secrets, credentials, `.env` files, or environment-specific configuration.

## Documentation

- Document the **why**, not the what—code shows what happens, comments explain reasoning
- Maintain up-to-date README with setup instructions
- Use JSDoc for public APIs and complex functions
- Delete outdated documentation rather than letting it mislead

## Testing

| Type | Quantity | Purpose |
|------|----------|---------|
| Unit | Many | Test individual functions and logic |
| Integration | Fewer | Test component interactions |
| E2E | Minimal | Test critical user flows |

- Test behavior, not implementation details
- Use descriptive test names: `should return null when user not found`
- Run tests before committing