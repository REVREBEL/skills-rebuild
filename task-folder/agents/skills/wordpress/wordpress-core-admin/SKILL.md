---
name: wordpress-core-admin
description: 'Install, configure, manage, secure, test, and deploy WordPress instances using WP-CLI, environment configuration, database management, security hardening, and deployment scripts. Use for core setup, multisite, maintenance, and deployment workflows.'
compatibility: 'Requires PHP 8.1+, MySQL/MariaDB, and WP-CLI.'
metadata:
  category: development
  type: execution-child
  source: custom
---

# WordPress Core, Administration, Security & Deployment

Automate WordPress core installation, database configuration, multisite networks, security hardening, testing, and deployment via WP-CLI.

## When to Use

- Installing new WordPress sites or setting up local development environments (Phase 1)
- Managing multisite networks and site mappings
- Automating database maintenance and options via WP-CLI
- Hardening site security (Phase 6)
- Running administrative integration tests (Phase 7)
- Executing production deployments and database migrations (Phase 8)

## Phase 1: WordPress Setup & Configuration

```bash
# Download and configure core
wp core download
wp config create --dbname=wp_db --dbuser=wp_user --dbpass=secret --dbhost=localhost
wp core install --url=example.com --title="Production Site" --admin_user=admin --admin_email=admin@example.com

# Configure multisite
wp core multisite-convert --subdomains
```

## Phase 6: Security Hardening

- **File Permissions**: Set directories to `755` and files to `644`. `wp-config.php` set to `600` or `440`.
- **Security Keys**: Generate unique salts via `wp config shuffle-salts`.
- **XML-RPC & File Editing**: Add `define('DISALLOW_FILE_EDIT', true);` in `wp-config.php`.
- **Database Prefix**: Use non-default table prefix (e.g. `wp_secure_`).

## Phase 7: Testing

- Run WP-CLI automated test suite: `wp eval-file tests/run-health-check.php`.
- Verify database integrity: `wp db check`.

## Phase 8: Deployment & Database Migrations

```bash
# Database export & migration
wp db export backup.sql
wp search-replace 'https://dev.example.com' 'https://example.com' --all-tables --dry-run
wp search-replace 'https://dev.example.com' 'https://example.com' --all-tables
```

## Completion Evidence

- Verified site access via URL and successful response from `wp core is-installed`.
- Passing security audit and clean database migration report.
