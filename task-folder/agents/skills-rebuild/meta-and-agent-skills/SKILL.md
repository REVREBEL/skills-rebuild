---
name: meta-and-agent-skills
description: Agent architecture, agent skill authoring, validation, and lifecycle management. Direct category router indexing 9 canonical skills across 3 subcategories.
type: category-router
version: 1.0.0
---

# `meta-and-agent-skills` Category Router

## Overview

This category router directly indexes **9 canonical active skills** across **3 subcategories** in the `meta-and-agent-skills` domain.

## When to Use

Use this router when the request involves agent architecture, agent skill authoring, validation, and lifecycle management.

## Scope Boundaries & Handoffs

| Adjacent Domain | Category Router | Handoff Trigger |
|---|---|---|
| business-and-operations | [`business-and-operations`](../business-and-operations/SKILL.md) | Requests primarily focused on business strategy, startup finance, product management, and legal/governance workflows. |
| content-and-documentation | [`content-and-documentation`](../content-and-documentation/SKILL.md) | Requests primarily focused on technical documentation, research synthesis, slide presentations, and copywriting. |
| data-and-ai | [`data-and-ai`](../data-and-ai/SKILL.md) | Requests primarily focused on data engineering, machine learning pipelines, llm/rag systems, analytics, and vector databases. |
| design-and-experience | [`design-and-experience`](../design-and-experience/SKILL.md) | Requests primarily focused on ui/ux design, visual design systems, aesthetic critique, and motion graphics. |
| development | [`development`](../development/SKILL.md) | Requests primarily focused on software development across frontend, backend, fullstack, mobile, systems, and architecture. |
| infrastructure-and-ops | [`infrastructure-and-ops`](../infrastructure-and-ops/SKILL.md) | Requests primarily focused on cloud hosting, ci/cd pipelines, container orchestration, observability, and server operations. |
| marketing-and-seo | [`marketing-and-seo`](../marketing-and-seo/SKILL.md) | Requests primarily focused on organic search (technical/on-page/local seo), conversion rate optimization (cro), and campaign marketing. |
| quality-and-security | [`quality-and-security`](../quality-and-security/SKILL.md) | Requests primarily focused on software testing, security vulnerability auditing, runtime debugging, and compliance governance. |
| workflow-and-automation | [`workflow-and-automation`](../workflow-and-automation/SKILL.md) | Requests primarily focused on workflow automation, mcp tool integrations, web scraping, and version control workflows. |

## Domain Policy & Shared Guidelines

- All workflows under `meta-and-agent-skills` adhere to standard domain principles and deterministic execution standards.
- Select the matching canonical leaf skill below based on task outcome.

## Subcategory Routing Index

### `agent-architecture` (3 skills)

- [`aria`](../business-and-operations/legal-and-governance/aria/SKILL.md): Autonomous agent coordination and squad orchestration for multi-step task execution. Use when orchestrating collaborative multi-agent workflows or task delegation squads.
- [`subagent-driven-development`](agent-architecture/subagent-driven-development/SKILL.md): Use when executing implementation plans with independent tasks in the current session.
- [`subagent-orchestrator`](agent-architecture/subagent-orchestrator/SKILL.md): Coordinate quota-aware parallel subagents for large, multi-file Antigravity tasks. Use when working with subagent orchestrator.

### `skill-lifecycle` (4 skills)

- [`agent-creator`](skill-lifecycle/agent-creator/SKILL.md): Create custom AI subagents with proper plugin structure, persona generation, and companion routing skills. Use when working with agent creator.
- [`codex-subagent`](skill-lifecycle/codex-subagent/SKILL.md): Launch Codex CLI as an isolated subagent for bounded coding, review, or verification tasks. Use when working with codex subagent.
- [`effective-agent-skills`](skill-lifecycle/effective-agent-skills/SKILL.md): Author and review high-quality agent skills with triggers, progressive disclosure, and safety notes. Use when working with effective agent skills.
- [`orchestrate`](skill-lifecycle/orchestrate/SKILL.md): Coordinate focused subagents on substantial work, keep their ownership non-overlapping, and integrate verified results. Use for large-scope Codex tasks; keep trivial work with the coordinator. Use when working with orchestrate.

### `skill-validation` (2 skills)

- [`llm-prompt-optimizer`](skill-validation/llm-prompt-optimizer/SKILL.md): Use when improving prompts for any LLM. Applies proven prompt engineering techniques to boost output quality, reduce hallucinations, and cut token usage.
- [`project-skill-audit`](skill-validation/project-skill-audit/SKILL.md): Audit a project and recommend the highest-value skills to add or update. Use when working with project skill audit.
