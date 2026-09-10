---
name: wordpress-woocommerce
description: 'Customize WooCommerce e-commerce stores, custom product types, cart/checkout extensions, and payment gateway integrations. Use when building online stores or customizing WooCommerce functionality.'
compatibility: 'Requires WordPress 6.0+ and WooCommerce 8.0+.'
metadata:
  category: development
  type: execution-child
  source: custom
---

# WordPress WooCommerce Customization

Build and customize WooCommerce stores, checkout flows, and product data models.

## When to Use

- Customizing product displays, pricing rules, and inventory management
- Hooking into WooCommerce checkout steps and order processing
- Creating custom cart discount rules and payment gateway integrations

## Checkout Action Hook Example

```php
add_action('woocommerce_checkout_order_processed', 'custom_process_order', 10, 3);
function custom_process_order($order_id, $posted_data, $order) {
    // Custom post-checkout business logic
    $order->add_order_note('Processed via custom automation integration.');
}
```

## Completion Evidence

- Verified test transaction and error-free checkout workflow.
