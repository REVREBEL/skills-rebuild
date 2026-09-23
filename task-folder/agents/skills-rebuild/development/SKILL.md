---
name: development
description: Software development across frontend, backend, fullstack, mobile, systems, and architecture. Routes to 6 specialized subcategory routers.
type: category-router
version: 1.0.0
---

# `development` Category Router

## Overview

This category router directs all requests within **`development`** to the appropriate specialized subcategory router.

## When to Use

Use this router when the request involves software development across frontend, backend, fullstack, mobile, systems, and architecture.

## Scope Boundaries & Handoffs

| Adjacent Domain | Category Router | Handoff Trigger |
|---|---|---|
| business-and-operations | [`business-and-operations`](../business-and-operations/SKILL.md) | Requests primarily focused on business strategy, startup finance, product management, and legal/governance workflows. |
| content-and-documentation | [`content-and-documentation`](../content-and-documentation/SKILL.md) | Requests primarily focused on technical documentation, research synthesis, slide presentations, and copywriting. |
| data-and-ai | [`data-and-ai`](../data-and-ai/SKILL.md) | Requests primarily focused on data engineering, machine learning pipelines, llm/rag systems, analytics, and vector databases. |
| design-and-experience | [`design-and-experience`](../design-and-experience/SKILL.md) | Requests primarily focused on ui/ux design, visual design systems, aesthetic critique, and motion graphics. |
| infrastructure-and-ops | [`infrastructure-and-ops`](../infrastructure-and-ops/SKILL.md) | Requests primarily focused on cloud hosting, ci/cd pipelines, container orchestration, observability, and server operations. |
| marketing-and-seo | [`marketing-and-seo`](../marketing-and-seo/SKILL.md) | Requests primarily focused on organic search (technical/on-page/local seo), conversion rate optimization (cro), and campaign marketing. |
| meta-and-agent-skills | [`meta-and-agent-skills`](../meta-and-agent-skills/SKILL.md) | Requests primarily focused on agent architecture, agent skill authoring, validation, and lifecycle management. |
| quality-and-security | [`quality-and-security`](../quality-and-security/SKILL.md) | Requests primarily focused on software testing, security vulnerability auditing, runtime debugging, and compliance governance. |
| workflow-and-automation | [`workflow-and-automation`](../workflow-and-automation/SKILL.md) | Requests primarily focused on workflow automation, mcp tool integrations, web scraping, and version control workflows. |

## Domain Policy & Shared Guidelines

- All workflows under `development` adhere to standard industry best practices and strict validation standards.
- Select the most specific subcategory router below to dispatch to canonical execution skills.

## Subcategory Routing Index

| Subcategory Router | Scope & Capability | Skill Count | Direct Link |
|---|---|---|---|
| **`backend`** | Server-side logic, database access, APIs, microservices, background queues, and cloud backend patterns. | 157 skills | [`backend/SKILL.md`](./backend/SKILL.md) |
| **`frontend`** | Client-side web development, React/Vue/Svelte components, state management, client routing, and DOM manipulation. | 56 skills | [`frontend/SKILL.md`](./frontend/SKILL.md) |
| **`fullstack`** | Fullstack web applications, frameworks (Next.js, Remix, Astro), CRUD architectures, and end-to-end features. | 407 skills | [`fullstack/SKILL.md`](./fullstack/SKILL.md) |
| **`mobile`** | Native iOS (Swift), Android (Kotlin), and cross-platform (React Native/Flutter) mobile applications. | 8 skills | [`mobile/SKILL.md`](./mobile/SKILL.md) |
| **`software-architecture`** | Clean code patterns, Domain-Driven Design, microservice architectures, refactoring, and ADRs. | 36 skills | [`software-architecture/SKILL.md`](./software-architecture/SKILL.md) |
| **`systems`** | CLI tooling, runtime performance, low-level networking, authentication protocols, and OS-level systems. | 24 skills | [`systems/SKILL.md`](./systems/SKILL.md) |
