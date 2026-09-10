---
name: wordpress-core-admin
description: 'Install, configure, manage, and automate WordPress instances using WP-CLI, environment configuration, and database management. Use for core installation, multisite configuration, maintenance tasks, and CLI administration.'
compatibility: 'Requires PHP 8.1+, MySQL/MariaDB, and WP-CLI.'
metadata:
  category: development
  type: execution-child
  source: custom
---

# WordPress Core & Administration

Automate WordPress core installation, database configuration, multisite networks, and administrative tasks via WP-CLI.

## When to Use

- Installing new WordPress sites or setting up local development environments
- Managing multisite networks and site mappings
- Automating database backups, updates, and maintenance via WP-CLI

## Common Workflows

```bash
# Core installation
wp core download
wp config create --dbname=wp_db --dbuser=wp_user --dbpass=secret --dbhost=localhost
wp core install --url=example.com --title="My Site" --admin_user=admin --admin_email=admin@example.com

# User & option management
wp user create developer dev@example.com --role=administrator
wp option update blogname "Updated Site Title"
```

## Completion Evidence

- Verified site access via URL and successful response from `wp core is-installed`.
