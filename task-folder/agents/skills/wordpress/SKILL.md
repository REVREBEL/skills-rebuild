---
name: wordpress
description: 'Route WordPress development and administration tasks across core configuration, theme engineering, plugin development, WooCommerce customization, performance optimization, security hardening, testing, and deployment. Use when planning, building, extending, or tuning WordPress environments.'
compatibility: 'Requires WordPress 6.0+ or 7.0+, PHP 8.1+, and WP-CLI.'
metadata:
  category: development
  type: category-router
  source: custom
---

# WordPress Development Workflow Bundle

Coordinate WordPress engineering workflows across core administration, themes, plugins, e-commerce, performance optimization, security, testing, and deployment.

## Overview

WordPress powers modern web applications ranging from decoupled publishing systems to complex e-commerce platforms. This router coordinates specialized skills for core administration, theme engineering, custom plugin development, WooCommerce, and performance tuning.

## WordPress 7.0 Features (Backward Compatible)

- **Real-Time Collaboration (RTC)**: Native collaborative editing engine with RTC-compatible post meta.
- **AI Connectors API**: Standardized endpoint integration for LLM and GenAI services.
- **Abilities API**: Granular capability registration for plugin actions.
- **DataViews & DataForm**: Modern admin UI components for dataset management.
- **PHP-Only Block Registration**: Streamlined server-side block registration.
- **Interactivity API Updates**: Declarative frontend reactive directives.
- **Admin Refresh & Pattern Editing**: Next-generation WordPress administrative UI.

## When to Use This Workflow & Decision Matrix

| User Goal | Focus Area | Specialized Child Skill |
|---|---|---|
| Core setup, multisite config, WP-CLI automation, deployment, security hardening | Core & Admin | [WordPress Core & Admin](./wordpress-core-admin/SKILL.md) |
| Block themes, `theme.json`, template hierarchy, FSE styling, PHP block registration | Theme Engineering | [WordPress Theme Development](./wordpress-theme-development/SKILL.md) |
| Custom plugins, action/filter hooks, REST API routes, AI Connectors, Abilities API | Plugin Engineering | [WordPress Plugin Development](./wordpress-plugin-development/SKILL.md) |
| WooCommerce catalog, custom cart/checkout, payment gateways, product data models | E-Commerce | [WordPress WooCommerce](./wordpress-woocommerce/SKILL.md) |
| Object caching (Redis), query profiling, asset minification, database indexing | Performance | [WordPress Performance Optimization](./wordpress-performance-optimization/SKILL.md) |

## Quality Gates & Coding Standards

- **Coding Standards**: Enforce `WordPress-Core`, `WordPress-Docs`, and `WordPress-Extra` via PHP_CodeSniffer.
- **Security Hardening**: Sanitize all inputs (`sanitize_text_field`), validate nonces (`wp_verify_nonce`), escape all outputs (`esc_html`, `esc_attr`), and use `$wpdb->prepare()`.
- **Testing Priorities**: Unit testing with PHPUnit, integration testing with WP-CLI test runner, and Playwright for frontend block interactions.
- **Deployment**: Zero-downtime database migrations with WP-CLI search-replace.

## Related Workflow Bundles & Limitations

- **Related Bundles**: PHP backend engineering, React/Gutenberg frontend development, Redis caching infrastructure.
- **Limitations**: Requires PHP 8.1+ and MySQL 8.0+ / MariaDB 10.5+ for WordPress 7.0 features.
