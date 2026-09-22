---
name: workflow-and-automation
description: Workflow automation, MCP tool integrations, web scraping, and version control workflows. Direct category router indexing 19 canonical skills across 4 subcategories.
type: category-router
version: 1.0.0
---

# `workflow-and-automation` Category Router

## Overview

This category router directly indexes **19 canonical active skills** across **4 subcategories** in the `workflow-and-automation` domain.

## When to Use

Use this router when the request involves workflow automation, mcp tool integrations, web scraping, and version control workflows.

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
| meta-and-agent-skills | [`meta-and-agent-skills`](../meta-and-agent-skills/SKILL.md) | Requests primarily focused on agent architecture, agent skill authoring, validation, and lifecycle management. |
| quality-and-security | [`quality-and-security`](../quality-and-security/SKILL.md) | Requests primarily focused on software testing, security vulnerability auditing, runtime debugging, and compliance governance. |

## Domain Policy & Shared Guidelines

- All workflows under `workflow-and-automation` adhere to standard domain principles and deterministic execution standards.
- Select the matching canonical leaf skill below based on task outcome.

## Subcategory Routing Index

### `git-and-vcs` (1 skills)

- [`using-git-worktrees`](git-and-vcs/using-git-worktrees/SKILL.md): Git worktrees create isolated workspaces sharing the same repository, allowing work on multiple branches simultaneously without switching. Use when working with using git worktrees.

### `task-orchestration` (5 skills)

- [`go-rod-master`](task-orchestration/go-rod-master/SKILL.md): Comprehensive guide for browser automation and web scraping with go-rod (Chrome DevTools Protocol) including stealth anti-bot-detection patterns. Use when working with go rod master.
- [`hasdata`](task-orchestration/hasdata/SKILL.md): Use HasData APIs for web scraping and structured web data extraction. Use when working with hasdata.
- [`n8n-error-handling`](../business-and-operations/legal-and-governance/n8n-error-handling/SKILL.md): Configure error workflows, retry policies, and alert routing in n8n automation pipelines. Use when handling execution failures or building resilient n8n workflows.
- [`open-dynamic-workflows`](task-orchestration/open-dynamic-workflows/SKILL.md): Plan, orchestrate, and adversarially verify parallel AI coding agents with a dynamic multi-agent workflow engine. Use when working with open dynamic workflows.
- [`workflow-automation`](task-orchestration/workflow-automation/SKILL.md): Workflow automation is the infrastructure that makes AI agents. Use when working with workflow automation.

### `tool-integration` (11 skills)

- [`automated-triage`](tool-integration/automated-triage/SKILL.md): Triage, assess, score, and troubleshoot Monte Carlo data reliability alerts interactively or via automated scheduled workflows using Monte Carlo MCP tools. Use when investigating data freshness delays, volume anomalies, or schema incidents.
- [`bilig-workpaper`](tool-integration/bilig-workpaper/SKILL.md): Execute formula-backed spreadsheet calculations, verify computed cell readbacks, and persist WorkPaper JSON models using the @bilig/workpaper TypeScript API and MCP server. Use when modeling complex spreadsheet calculations without spreadsheet GUIs.
- [`mcp-builder-ms`](tool-integration/mcp-builder-ms/SKILL.md): Design, build, and package Model Context Protocol (MCP) servers in Python (FastMCP) or TypeScript (MCP SDK v2) across stdio and streamable HTTP transports. Use when exposing internal tools, data sources, and services to AI agents.
- [`n8n-code-python`](tool-integration/n8n-code-python/SKILL.md): Write, debug, and optimize Python transformations in n8n 2.x native Python Code nodes using _items and _item data structures, handling Cloud sandbox constraints and self-hosted runner environments. Use when writing Python transformations or debugging n8n 2.x Python Code nodes.
- [`n8n-code-tool`](tool-integration/n8n-code-tool/SKILL.md): Author, validate, and secure custom code tools callable by AI agents in n8n, defining input JSON schemas, sandbox execution parameters, and output contracts. Use when creating custom AI agent tools for LangChain and AI Agent nodes in n8n.
- [`n8n-mcp-tools-expert`](tool-integration/n8n-mcp-tools-expert/SKILL.md): Utilize n8n-mcp server tools to discover node definitions, validate workflow configurations, search template libraries, and manage n8n workflows programmatically. Use when inspecting node parameters, searching templates, or managing n8n workflows via MCP tools.
- [`n8n-node-configuration`](tool-integration/n8n-node-configuration/SKILL.md): Configure n8n node parameters, resolve operation dependencies, determine required properties, and apply expression syntax across core and community node families. Use when configuring node operations or authoring dynamic expression bindings in n8n.
- [`n8n-subworkflows`](tool-integration/n8n-subworkflows/SKILL.md): Design, build, and integrate modular n8n subworkflows with typed inputs, item-by-item vs all-item execution modes, error delegation, and agent tool exposure. Use when decomposing complex workflows into reusable subworkflows in n8n.
- [`n8n-validation-expert`](tool-integration/n8n-validation-expert/SKILL.md): Diagnose, interpret, and remediate n8n workflow validation errors, missing required properties, expression syntax failures, and node connection schema mismatches. Use when diagnosing n8n workflow validation errors or connection schema failures.
- [`n8n-workflow-patterns`](tool-integration/n8n-workflow-patterns/SKILL.md): Select, structure, and implement proven architectural patterns for n8n workflows including webhook ingestion, scheduled polling, queue processing, API integration, and AI sub-execution routing. Use when designing robust, idempotent workflow architectures in n8n.
- [`protect-mcp-governance`](tool-integration/protect-mcp-governance/SKILL.md): Govern AI agent Model Context Protocol (MCP) tool calls using Cedar access control policies, shadow-to-enforce rollout modes, and Ed25519 cryptographic receipt verification. Use when securing and auditing AI agent tool execution gateways with Cedar policies.

### `web-scraping` (2 skills)

- [`puppeteer-skill`](web-scraping/puppeteer-skill/SKILL.md): Generates Puppeteer scripts for browser automation, scraping, and PDF generation. Triggers on: \\"Puppeteer\\", \\"headless Chrome\\", \\"page.goto\\", \\"scrape\\", \\"PDF generation\\". Use when working with puppeteer skill.
- [`web-scraper`](web-scraping/web-scraper/SKILL.md): Web scraping inteligente multi-estrategia. Extrai dados estruturados de paginas web (tabelas, listas, precos). Paginacao, monitoramento e export CSV/JSON. Use when working with web scraper.
