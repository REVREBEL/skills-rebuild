---
name: skills-rebuild
description: Master entry point and dispatch router for the rebuilt Agent Skills library. Routes requests across 10 top-level functional categories.
type: master-router
version: 1.0.0
---

# Rebuilt Agent Skills Library - Master Router

## Overview

Welcome to the canonical Agent Skills library. This master router directs all user requests to the appropriate functional category router across 10 core capability domains.

## Functional Category Dispatch

| Category Router | Functional Domain & Scope | Subcategories | Direct Routing Model |
|---|---|---|---|
| [`business-and-operations`](./business-and-operations/SKILL.md) | Business strategy, startup finance, product management, and legal/governance workflows. | 4-5 | Direct (routes directly to leaf skills) |
| [`content-and-documentation`](./content-and-documentation/SKILL.md) | Technical documentation, research synthesis, slide presentations, and copywriting. | 4-5 | Direct (routes directly to leaf skills) |
| [`data-and-ai`](./data-and-ai/SKILL.md) | Data engineering, machine learning pipelines, LLM/RAG systems, analytics, and vector databases. | 4-5 | Direct (routes directly to leaf skills) |
| [`design-and-experience`](./design-and-experience/SKILL.md) | UI/UX design, visual design systems, aesthetic critique, and motion graphics. | 4 | Deep (routes to 4 Subcategory Routers) |
| [`development`](./development/SKILL.md) | Software development across frontend, backend, fullstack, mobile, systems, and architecture. | 6 | Deep (routes to 6 Subcategory Routers) |
| [`infrastructure-and-ops`](./infrastructure-and-ops/SKILL.md) | Cloud hosting, CI/CD pipelines, container orchestration, observability, and server operations. | 4-5 | Direct (routes directly to leaf skills) |
| [`marketing-and-seo`](./marketing-and-seo/SKILL.md) | Organic search (technical/on-page/local SEO), conversion rate optimization (CRO), and campaign marketing. | 5 | Deep (routes to 5 Subcategory Routers) |
| [`meta-and-agent-skills`](./meta-and-agent-skills/SKILL.md) | Agent architecture, agent skill authoring, validation, and lifecycle management. | 4-5 | Direct (routes directly to leaf skills) |
| [`quality-and-security`](./quality-and-security/SKILL.md) | Software testing, security vulnerability auditing, runtime debugging, and compliance governance. | 4-5 | Direct (routes directly to leaf skills) |
| [`workflow-and-automation`](./workflow-and-automation/SKILL.md) | Workflow automation, MCP tool integrations, web scraping, and version control workflows. | 4-5 | Direct (routes directly to leaf skills) |

## Cross-Category Disambiguation & Boundary Matrix

| Ambiguous Intent / Keyword | Primary Functional Router | Secondary / Alternative Domain | Disambiguation Rationale |
|---|---|---|---|
| **CI/CD Build & Deployment** | [`infrastructure-and-ops`](./infrastructure-and-ops/SKILL.md) | `development` | Build pipelines and deployment hosting belong in infrastructure-and-ops. |
| **Automated E2E Test Suites** | [`quality-and-security`](./quality-and-security/SKILL.md) | `development` | Automated test verification and test harnesses belong in quality-and-security. |
| **Visual Design Tokens & Styling** | [`design-and-experience`](./design-and-experience/SKILL.md) | `development` | Visual aesthetics, spacing harmony, and color palettes belong in design. |
| **Vector Search & Embedding Stores** | [`data-and-ai`](./data-and-ai/SKILL.md) | `development` | Embedding distance metrics and vector retrieval belong in data-and-ai. |
| **Search Engine Indexation & Sitemaps** | [`marketing-and-seo`](./marketing-and-seo/SKILL.md) | `content-and-documentation` | Search engine acquisition and crawl optimization belong in marketing-and-seo. |
| **Headless Web Scraping** | [`workflow-and-automation`](./workflow-and-automation/SKILL.md) | `quality-and-security` | Automated data extraction pipelines belong in workflow-and-automation. |
| **MCP Server Integration & Tool Bridges** | [`workflow-and-automation`](./workflow-and-automation/SKILL.md) | `infrastructure-and-ops` | Tool adapters and JSON-RPC bridges belong in workflow-and-automation. |
| **Agent Skill Authoring & Validation** | [`meta-and-agent-skills`](./meta-and-agent-skills/SKILL.md) | `development` | Agent Skills ecosystem governance belongs in meta-and-agent-skills. |
| **Corporate Unit Economics & Financial Models** | [`business-and-operations`](./business-and-operations/SKILL.md) | `data-and-ai` | Corporate financial planning and cap table modeling belong in business-and-operations. |
| **Technical Documentation & API Manuals** | [`content-and-documentation`](./content-and-documentation/SKILL.md) | `marketing-and-seo` | Informational developer documentation belongs in content-and-documentation. |

## Core Library Routing Principles

1. **Single Canonical Destination**: Every user request resolves to exactly one canonical leaf skill.
2. **Parent Routes, Child Executes**: Routers provide routing rules, scope boundaries, and indexes; child skills contain execution workflows.
3. **Progressive Disclosure**: Agents navigate from Root -> Category Router -> (Subcategory Router) -> Canonical Leaf Skill.
