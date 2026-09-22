---
name: marketing-and-seo
description: Organic search (technical/on-page/local SEO), conversion rate optimization (CRO), and campaign marketing. Routes to 5 specialized subcategory routers.
type: category-router
version: 1.0.0
---

# `marketing-and-seo` Category Router

## Overview

This category router directs all requests within **`marketing-and-seo`** to the appropriate specialized subcategory router.

## When to Use

Use this router when the request involves organic search (technical/on-page/local seo), conversion rate optimization (cro), and campaign marketing.

## Scope Boundaries & Handoffs

| Adjacent Domain | Category Router | Handoff Trigger |
|---|---|---|
| business-and-operations | [`business-and-operations`](../business-and-operations/SKILL.md) | Requests primarily focused on business strategy, startup finance, product management, and legal/governance workflows. |
| content-and-documentation | [`content-and-documentation`](../content-and-documentation/SKILL.md) | Requests primarily focused on technical documentation, research synthesis, slide presentations, and copywriting. |
| data-and-ai | [`data-and-ai`](../data-and-ai/SKILL.md) | Requests primarily focused on data engineering, machine learning pipelines, llm/rag systems, analytics, and vector databases. |
| design-and-experience | [`design-and-experience`](../design-and-experience/SKILL.md) | Requests primarily focused on ui/ux design, visual design systems, aesthetic critique, and motion graphics. |
| development | [`development`](../development/SKILL.md) | Requests primarily focused on software development across frontend, backend, fullstack, mobile, systems, and architecture. |
| infrastructure-and-ops | [`infrastructure-and-ops`](../infrastructure-and-ops/SKILL.md) | Requests primarily focused on cloud hosting, ci/cd pipelines, container orchestration, observability, and server operations. |
| meta-and-agent-skills | [`meta-and-agent-skills`](../meta-and-agent-skills/SKILL.md) | Requests primarily focused on agent architecture, agent skill authoring, validation, and lifecycle management. |
| quality-and-security | [`quality-and-security`](../quality-and-security/SKILL.md) | Requests primarily focused on software testing, security vulnerability auditing, runtime debugging, and compliance governance. |
| workflow-and-automation | [`workflow-and-automation`](../workflow-and-automation/SKILL.md) | Requests primarily focused on workflow automation, mcp tool integrations, web scraping, and version control workflows. |

## Domain Policy & Shared Guidelines

- All workflows under `marketing-and-seo` adhere to standard industry best practices and strict validation standards.
- Select the most specific subcategory router below to dispatch to canonical execution skills.

## Subcategory Routing Index

| Subcategory Router | Scope & Capability | Skill Count | Direct Link |
|---|---|---|---|
| **`content-and-campaigns`** | Marketing copywriting, advertising creatives, lead magnets, social campaigns, and audience research. | 49 skills | [`content-and-campaigns/SKILL.md`](./content-and-campaigns/SKILL.md) |
| **`cro`** | Conversion rate optimization, landing page persuasion, A/B testing, user journey funnels, and marketing analytics. | 214 skills | [`cro/SKILL.md`](./cro/SKILL.md) |
| **`geo-and-local-seo`** | Local business search optimization, regional directory citations, Google Maps ranking, and local listings. | 47 skills | [`geo-and-local-seo/SKILL.md`](./geo-and-local-seo/SKILL.md) |
| **`on-page-seo`** | On-page content optimization, keyword targeting, meta tags, heading hierarchies, and search intent alignment. | 279 skills | [`on-page-seo/SKILL.md`](./on-page-seo/SKILL.md) |
| **`technical-seo`** | Search engine indexation, crawl budgeting, XML sitemaps, canonical tags, schema markup, and site speed. | 57 skills | [`technical-seo/SKILL.md`](./technical-seo/SKILL.md) |
