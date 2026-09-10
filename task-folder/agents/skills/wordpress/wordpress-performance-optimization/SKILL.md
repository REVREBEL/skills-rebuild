---
name: wordpress-performance-optimization
description: 'Optimize WordPress performance, database queries, Redis/Memcached object caching, asset loading, and CDN integration. Use when tuning slow WordPress sites, reducing TTFB, or optimizing Core Web Vitals.'
compatibility: 'Requires WordPress 6.0+, Redis/Memcached server, and WP-CLI.'
metadata:
  category: development
  type: execution-child
  source: custom
---

# WordPress Performance Optimization

Tune WordPress site speed, query performance, object caching, and Core Web Vitals.

## When to Use

- Configuring Redis or Memcached persistent object caching
- Profiling slow database queries with Query Monitor
- Optimizing script enqueueing and critical CSS delivery

## Optimization Techniques

1. **Persistent Object Caching**: Enable Redis cache drop-in (`wp-content/object-cache.php`).
2. **Database Optimization**: Clean transients and revisions via `wp db optimize` and `wp transient delete --all`.
3. **Asset Deferral**: Defer non-critical JavaScript using `wp_enqueue_script` with `['strategy' => 'defer']`.

## Completion Evidence

- Measurable reduction in TTFB and database query count.
