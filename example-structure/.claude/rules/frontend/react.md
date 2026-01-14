# React Rules

Guidelines for React component development.

## Component Structure

Standard file structure for components:

```tsx
// 1. Imports
import {useState} from 'react'
import type {UserProps} from './types'

// 2. Types (if not in separate file)
interface Props {
    user: User
    onSave: (user: User) => void
}

// 3. Component
export function UserCard({user, onSave}: Props) {
    // hooks first
    // handlers next
    // render last
}
```

## State Management

| Scenario                | Solution                        |
|-------------------------|---------------------------------|
| Component-specific data | `useState`                      |
| Complex state logic     | `useReducer`                    |
| Shared between siblings | Lift state up                   |
| Deep prop drilling      | Context API                     |
| Global app state        | Pinia (Nuxt) or dedicated store |

**Rules:**

- Never store derived state—compute during render
- Initialize state with appropriate defaults
- Avoid syncing state with props (use key prop instead)

## Hooks Guidelines

```tsx
// Good - dependencies are correct
const filtered = useMemo(() =>
        items.filter(i => i.active),
    [items]
)

// Bad - missing dependency
const filtered = useMemo(() =>
        items.filter(i => i.status === status),
    [items]  // missing 'status'
)
```

| Hook          | When to Use                                |
|---------------|--------------------------------------------|
| `useMemo`     | Expensive computations                     |
| `useCallback` | Callbacks passed to memoized children      |
| `useRef`      | DOM refs, mutable values without re-render |
| `useEffect`   | Side effects, subscriptions                |

## Props

- Define explicit TypeScript interfaces for all props
- Destructure in function signature
- Provide sensible defaults where appropriate
- Use children prop for composition
