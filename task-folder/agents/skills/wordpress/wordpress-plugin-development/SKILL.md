---
name: wordpress-plugin-development
description: 'Develop custom WordPress plugins with action/filter hooks, custom post types, custom REST API endpoints, and secure database schemas. Use when extending WordPress functionality or building integrations.'
compatibility: 'Requires PHP 8.1+ and WordPress 6.0+.'
metadata:
  category: development
  type: execution-child
  source: custom
---

# WordPress Plugin Development

Author robust, secure, and extensible custom WordPress plugins using standard hooks and REST endpoints.

## When to Use

- Registering custom post types and custom taxonomies
- Creating custom REST API endpoints under `register_rest_route`
- Hooking into WordPress lifecycle events (`init`, `wp_enqueue_scripts`, `save_post`)

## Custom REST API Route Example

```php
add_action('rest_api_init', function () {
    register_rest_route('custom/v1', '/data', [
        'methods'  => 'GET',
        'callback' => 'custom_get_data_handler',
        'permission_callback' => function () {
            return current_user_can('read');
        },
    ]);
});

function custom_get_data_handler(WP_REST_Request $request) {
    return new WP_REST_Response(['status' => 'success', 'data' => []], 200);
}
```

## Completion Evidence

- Plugin activation without PHP warnings/errors and passing `phpcs --standard=WordPress`.
