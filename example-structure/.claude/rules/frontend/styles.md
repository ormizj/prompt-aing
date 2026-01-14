# Styles Rules

Guidelines for CSS and styling conventions.

## Naming Conventions

Use BEM (Block Element Modifier) naming:

```css
/* Block */
.card { }

/* Element */
.card__title { }
.card__body { }

/* Modifier */
.card--featured { }
.card__title--large { }
```

| Pattern | Example | Use Case |
|---------|---------|----------|
| Block | `.user-profile` | Component root |
| Element | `.user-profile__avatar` | Child element |
| Modifier | `.user-profile--compact` | Variation |

## Property Order

Organize CSS properties in this order:

```css
.component {
  /* 1. Positioning */
  position: relative;
  top: 0;
  z-index: 1;

  /* 2. Box Model */
  display: flex;
  width: 100%;
  padding: 1rem;
  margin: 0;

  /* 3. Typography */
  font-size: 1rem;
  color: var(--text-primary);

  /* 4. Visual */
  background: var(--bg-surface);
  border-radius: 8px;

  /* 5. Misc */
  cursor: pointer;
  transition: opacity 0.2s;
}
```

## Responsive Design

| Principle | Implementation |
|-----------|----------------|
| Mobile-first | Base styles for mobile, add breakpoints up |
| Relative units | Use `rem`, `em`, `%` over `px` |
| Touch targets | Minimum 44x44px on mobile |
| Breakpoints | Define as CSS custom properties |

```css
:root {
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
}
```

## Design Tokens

Define all design values as CSS custom properties:

```css
:root {
  /* Colors - semantic names */
  --color-primary: #3b82f6;
  --color-text: #1f2937;
  --color-bg: #ffffff;

  /* Spacing scale */
  --space-xs: 0.25rem;
  --space-sm: 0.5rem;
  --space-md: 1rem;
  --space-lg: 1.5rem;

  /* Typography */
  --font-sans: system-ui, sans-serif;
  --font-size-base: 1rem;
}
```