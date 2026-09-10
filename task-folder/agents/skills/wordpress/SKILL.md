---
name: wordpress
description: 'Route WordPress development and administration tasks across core configuration, theme engineering, plugin development, WooCommerce customization, and performance optimization. Use when planning, building, extending, or tuning WordPress environments.'
compatibility: 'Requires WordPress 6.0+ or 7.0+, PHP 8.1+, and WP-CLI.'
metadata:
  category: development
  type: category-router
  source: custom
---

# WordPress Router

Coordinate WordPress engineering workflows across core administration, themes, plugins, e-commerce, and performance optimization.

## When to Use

- Installing, configuring, or administrating WordPress instances with WP-CLI -> [WordPress Core & Admin](./wordpress-core-admin/SKILL.md)
- Developing custom block themes, classic themes, or template hierarchies -> [WordPress Theme Development](./wordpress-theme-development/SKILL.md)
- Creating custom plugins, hooks, custom post types, and REST API endpoints -> [WordPress Plugin Development](./wordpress-plugin-development/SKILL.md)
- Customizing WooCommerce stores, checkout flows, and product data models -> [WordPress WooCommerce](./wordpress-woocommerce/SKILL.md)
- Tuning database queries, caching layers, and asset delivery -> [WordPress Performance Optimization](./wordpress-performance-optimization/SKILL.md)

## Workflow Decision Matrix

| User Goal | Focus Area | Specialized Child Skill |
|---|---|---|
| Core setup, multisite config, automated WP-CLI management | Administration | [WordPress Core & Admin](./wordpress-core-admin/SKILL.md) |
| Block themes, `theme.json`, template hierarchy, FSE styling | Theme Engineering | [WordPress Theme Development](./wordpress-theme-development/SKILL.md) |
| Custom plugins, action/filter hooks, custom tables, REST API | Plugin Engineering | [WordPress Plugin Development](./wordpress-plugin-development/SKILL.md) |
| WooCommerce catalog, custom cart/checkout, payment gateways | E-Commerce | [WordPress WooCommerce](./wordpress-woocommerce/SKILL.md) |
| Object caching (Redis), query profiling, asset minification | Performance | [WordPress Performance Optimization](./wordpress-performance-optimization/SKILL.md) |

## Quality Gates & Coding Standards

- **Coding Standards**: Enforce `WordPress-Core`, `WordPress-Docs`, and `WordPress-Extra` via PHP_CodeSniffer.
- **Security**: Sanitize all inputs (`sanitize_text_field`), validate nonces (`wp_verify_nonce`), and escape all outputs (`esc_html`, `esc_attr`).
- **Database**: Use `$wpdb->prepare()` for all SQL operations.
