---
name: wordpress-theme-development
description: 'Build custom WordPress block themes and classic themes adhering to the WordPress template hierarchy and theme.json specifications. Use when authoring custom themes, block patterns, and template parts.'
compatibility: 'Requires WordPress 6.0+ Full Site Editing (FSE).'
metadata:
  category: development
  type: execution-child
  source: custom
---

# WordPress Theme Development

Author custom WordPress block themes and hybrid themes following modern Full Site Editing (FSE) standards.

## When to Use

- Creating custom block themes using `theme.json` styling configurations
- Developing custom block patterns, template parts, and block variations
- Implementing classic template hierarchies with modern PHP practices

## `theme.json` Configuration

```json
{
  "$schema": "https://schemas.wp.org/trunk/theme.json",
  "version": 3,
  "settings": {
    "color": {
      "palette": [
        { "slug": "primary", "color": "#0066cc", "name": "Primary" },
        { "slug": "neutral-dark", "color": "#111827", "name": "Dark Neutral" }
      ]
    },
    "layout": {
      "contentSize": "800px",
      "wideSize": "1200px"
    }
  }
}
```

## Completion Evidence

- Validated `theme.json` schema and theme activation without fatal errors.
