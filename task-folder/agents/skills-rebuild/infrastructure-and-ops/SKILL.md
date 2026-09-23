---
name: infrastructure-and-ops
description: Cloud hosting, CI/CD pipelines, container orchestration, observability, and server operations. Direct category router indexing 60 canonical skills across 5 subcategories.
type: category-router
version: 1.0.0
---

# `infrastructure-and-ops` Category Router

## Overview

This category router directly indexes **60 canonical active skills** across **5 subcategories** in the `infrastructure-and-ops` domain.

## When to Use

Use this router when the request involves cloud hosting, ci/cd pipelines, container orchestration, observability, and server operations.

## Scope Boundaries & Handoffs

| Adjacent Domain | Category Router | Handoff Trigger |
|---|---|---|
| business-and-operations | [`business-and-operations`](../business-and-operations/SKILL.md) | Requests primarily focused on business strategy, startup finance, product management, and legal/governance workflows. |
| content-and-documentation | [`content-and-documentation`](../content-and-documentation/SKILL.md) | Requests primarily focused on technical documentation, research synthesis, slide presentations, and copywriting. |
| data-and-ai | [`data-and-ai`](../data-and-ai/SKILL.md) | Requests primarily focused on data engineering, machine learning pipelines, llm/rag systems, analytics, and vector databases. |
| design-and-experience | [`design-and-experience`](../design-and-experience/SKILL.md) | Requests primarily focused on ui/ux design, visual design systems, aesthetic critique, and motion graphics. |
| development | [`development`](../development/SKILL.md) | Requests primarily focused on software development across frontend, backend, fullstack, mobile, systems, and architecture. |
| marketing-and-seo | [`marketing-and-seo`](../marketing-and-seo/SKILL.md) | Requests primarily focused on organic search (technical/on-page/local seo), conversion rate optimization (cro), and campaign marketing. |
| meta-and-agent-skills | [`meta-and-agent-skills`](../meta-and-agent-skills/SKILL.md) | Requests primarily focused on agent architecture, agent skill authoring, validation, and lifecycle management. |
| quality-and-security | [`quality-and-security`](../quality-and-security/SKILL.md) | Requests primarily focused on software testing, security vulnerability auditing, runtime debugging, and compliance governance. |
| workflow-and-automation | [`workflow-and-automation`](../workflow-and-automation/SKILL.md) | Requests primarily focused on workflow automation, mcp tool integrations, web scraping, and version control workflows. |

## Domain Policy & Shared Guidelines

- All workflows under `infrastructure-and-ops` adhere to standard domain principles and deterministic execution standards.
- Select the matching canonical leaf skill below based on task outcome.

## Subcategory Routing Index

### `ci-cd` (6 skills)

- [`actions-debugger`](ci-cd/actions-debugger/SKILL.md): Specialized skill for diagnosing, analyzing, and fixing failing GitHub Actions workflows by parsing run logs and pipeline definitions. Use when working with actions debugger.
- [`ci-cd-and-automation`](ci-cd/ci-cd-and-automation/SKILL.md): Automates CI/CD pipeline setup. Use when setting up or modifying build and deployment pipelines. Use when you need to automate quality gates, configure test runners in CI, or establish deployment strategies.
- [`cicd-automation-workflow-automate`](ci-cd/cicd-automation-workflow-automate/SKILL.md): You are a workflow automation expert specializing in creating efficient CI/CD pipelines, GitHub Actions workflows, and automated development processes. Design and implement automation that reduces manual work, improves consistency, and accelerates delivery while maintaining quality and security. Use when working with cicd automation workflow automate.
- [`monorepo-architect`](ci-cd/monorepo-architect/SKILL.md): Expert in monorepo architecture, build systems, and dependency management at scale. Masters Nx, Turborepo, Bazel, and Lerna for efficient multi-project development. Use PROACTIVELY for monorepo setup,. Use when working with monorepo architect.
- [`security-review`](ci-cd/security-review/SKILL.md): Find exploitable vulnerabilities in GitHub Actions workflows. Every finding MUST include a concrete exploitation scenario — if you can't build the attack, don't report it. Use when working with security review.
- [`turborepo-caching`](ci-cd/turborepo-caching/SKILL.md): Configure Turborepo for efficient monorepo builds with local and remote caching. Use when setting up Turborepo, optimizing build pipelines, or implementing distributed caching.

### `cloud-platforms` (14 skills)

- [`auri-core`](cloud-platforms/auri-core/SKILL.md): Auri: assistente de voz inteligente (Alexa + modelo-inteligente). Visao do produto, persona Vitoria Neural, stack AWS, modelo Free/Pro/Business/Enterprise, roadmap 4 fases, GTM, north star WAC e analise competitiva. Use when working with auri core.
- [`bigquery-table-creator`](cloud-platforms/bigquery-table-creator/SKILL.md): Execute bigquery-table-creator tasks, workflows, and automated procedures. Use when working with bigquery table creator.
- [`bigquery-view-generator`](cloud-platforms/bigquery-view-generator/SKILL.md): Execute bigquery-view-generator tasks, workflows, and automated procedures. Use when working with bigquery view generator.
- [`cdk-patterns`](cloud-platforms/cdk-patterns/SKILL.md): Common AWS CDK patterns and constructs for building cloud infrastructure with TypeScript, Python, or Java. Use when designing reusable CDK stacks and L3 constructs.
- [`cloud-architect`](cloud-platforms/cloud-architect/SKILL.md): Expert cloud architect specializing in AWS/Azure/GCP multi-cloud infrastructure design, advanced IaC (Terraform/OpenTofu/CDK), FinOps cost optimization, and modern architectural patterns. Use when working with cloud architect.
- [`deploy-to-vercel`](cloud-platforms/deploy-to-vercel/SKILL.md): Deploy applications and websites to Vercel. Use when the user requests deployment actions like \\\"deploy my app\\\", \\\"deploy and give me the link\\\", \\\"push this live\\\", or \\\"create a preview deployment\\\".
- [`remote-gpu-trainer`](cloud-platforms/remote-gpu-trainer/SKILL.md): Deploy, monitor, and debug long GPU jobs on RENTED/remote instances (AutoDL, RunPod, vast.ai, Lambda, Slurm, K8s): teardown/billing safety, spot resilience, resumable checkpointing, OOM/NaN triage. Use when working with remote gpu trainer.
- [`sandbox-sdk`](cloud-platforms/sandbox-sdk/SKILL.md): Build sandboxed applications for secure code execution. Load when building AI code execution, code interpreters, CI/CD systems, interactive dev environments, or executing untrusted code. Covers Sandbox SDK lifecycle, commands, files, code interpreter, and preview URLs. Biases towards retrieval from Cloudflare docs over pre-trained knowledge. Use when working with sandbox sdk.
- [`turnstile-spin`](cloud-platforms/turnstile-spin/SKILL.md): Set up Cloudflare Turnstile end-to-end in a project — scan the codebase, create the widget via the Cloudflare API, deploy the managed siteverify Worker, write the frontend snippets, validate, and persist the skill. Load this when a user asks to add Turnstile, set up CAPTCHA, protect a form from bots, or fix a Turnstile integration. Mirrors developers.cloudflare.com/turnstile/spin. Use when working with turnstile spin.
- [`vercel-ai-sdk-expert`](cloud-platforms/vercel-ai-sdk-expert/SKILL.md): Expert in the Vercel AI SDK. Covers Core API (generateText, streamText), UI hooks (useChat, useCompletion), tool calling, and streaming UI components with React and Next.js. Use when working with vercel ai sdk expert.
- [`vercel-automation`](cloud-platforms/vercel-automation/SKILL.md): Automate Vercel tasks via Rube MCP (Composio): manage deployments, domains, DNS, env vars, projects, and teams. Always search tools first for current schemas. Use when working with vercel automation.
- [`vercel-deployment`](cloud-platforms/vercel-deployment/SKILL.md): Expert knowledge for deploying to Vercel with Next.js. Use when working with vercel deployment.
- [`vercel-optimize`](cloud-platforms/vercel-optimize/SKILL.md): Audit deployed Vercel apps for cost and performance issues using metrics, project config, code scans, and version-aware recommendations. Use when working with vercel optimize.
- [`workflow-automation`](cloud-platforms/workflow-automation/SKILL.md): Patterns for automating GitHub workflows with AI assistance, inspired by [Gemini CLI](https://github.com/google-gemini/gemini-cli) and modern DevOps practices. Use when working with workflow automation.

### `containers-and-orchestration` (18 skills)

- [`1password`](containers-and-orchestration/1password/SKILL.md): Route 1Password secrets management requests across CLI retrieval, Developer Environments, Kubernetes integrations, and Service Account CI/CD workflows. Use when determining the correct 1Password workflow for local development, environment variable sync, Kubernetes secret injection, or automated deployments.
- [`1password-cli`](containers-and-orchestration/1password-cli/SKILL.md): Execute 1Password CLI (op) operations for local development, secret retrieval, item/vault CRUD, configuration injection, shell plugins, and git credential workflows. Use when running op read, op run, op inject, managing items/vaults/documents, or configuring developer shell plugins.
- [`1password-developer-environments`](containers-and-orchestration/1password-developer-environments/SKILL.md): Manage 1Password Developer Environments for project environment variables using TypeScript (Bun) and Python SDK tools. Use when creating, updating, exporting, or resolving project secrets programmatically across development environments.
- [`1password-kubernetes`](containers-and-orchestration/1password-kubernetes/SKILL.md): Configure and deploy Kubernetes secret synchronization using the native 1Password Operator and External Secrets Operator (ESO). Use when injecting 1Password secrets into Kubernetes cluster secrets, CRDs, or pod volumes.
- [`1password-service-accounts`](containers-and-orchestration/1password-service-accounts/SKILL.md): Configure 1Password Service Accounts for CI/CD automation, GitHub Actions, GitLab CI, CircleCI, and container environments. Use when provisioning service account tokens and configuring automated secret injection.
- [`agents-v2-py`](containers-and-orchestration/agents-v2-py/SKILL.md): Build container-based Foundry Agents with Azure AI Projects SDK (ImageBasedHostedAgentDefinition). Use when creating hosted agents with custom container images in Azure AI Foundry.
- [`apple-container`](containers-and-orchestration/apple-container/SKILL.md): Build, run, and manage OCI/Linux containers as lightweight per-container VMs on Apple-silicon macOS using Apple's open-source container CLI, no Docker daemon required. Use when working with apple container.
- [`cloud-devops`](containers-and-orchestration/cloud-devops/SKILL.md): Cloud infrastructure and DevOps workflow covering AWS, Azure, GCP, Kubernetes, Terraform, CI/CD, monitoring, and cloud-native development. Use when working with cloud devops.
- [`container-security-hardening`](containers-and-orchestration/container-security-hardening/SKILL.md): Execute container-security-hardening tasks, workflows, and automated procedures. Use when working with container security hardening.
- [`docker-expert`](containers-and-orchestration/docker-expert/SKILL.md): You are an advanced Docker containerization expert with comprehensive, practical knowledge of container optimization, security hardening, multi-stage builds, orchestration patterns, and production deployment strategies based on current industry best practices. Use when working with docker expert.
- [`gcp-cloud-run`](containers-and-orchestration/gcp-cloud-run/SKILL.md): Specialized skill for building production-ready serverless. Use when working with gcp cloud run.
- [`hosted-agents-v2-py`](containers-and-orchestration/hosted-agents-v2-py/SKILL.md): Build hosted agents using Azure AI Projects SDK with ImageBasedHostedAgentDefinition. Use when creating container-based agents in Azure AI Foundry.
- [`istio-traffic-management`](containers-and-orchestration/istio-traffic-management/SKILL.md): Comprehensive guide to Istio traffic management for production service mesh deployments. Use when working with istio traffic management.
- [`linkerd-patterns`](containers-and-orchestration/linkerd-patterns/SKILL.md): Production patterns for Linkerd service mesh - the lightweight, security-first service mesh for Kubernetes. Use when working with linkerd patterns.
- [`service-mesh-expert`](containers-and-orchestration/service-mesh-expert/SKILL.md): Expert service mesh architect specializing in Istio, Linkerd, and cloud-native networking patterns. Masters traffic management, security policies, observability integration, and multi-cluster mesh con. Use when working with service mesh expert.
- [`service-mesh-observability`](containers-and-orchestration/service-mesh-observability/SKILL.md): Complete guide to observability patterns for Istio, Linkerd, and service mesh deployments. Use when working with service mesh observability.
- [`sshepherd`](containers-and-orchestration/sshepherd/SKILL.md): Zero-knowledge SSH ops CLI — server health checks, docker/systemd control, log tailing, Postgres introspection, and declarative deploys, without ever exposing credentials to the agent. Use when working with sshepherd.
- [`wrangler`](containers-and-orchestration/wrangler/SKILL.md): Cloudflare Workers CLI for deploying, developing, and managing Workers, KV, R2, D1, Vectorize, Hyperdrive, Workers AI, Containers, Queues, Workflows, Pipelines, and Secrets Store. Load before running wrangler commands to ensure correct syntax and best practices. Biases towards retrieval from Cloudflare docs over pre-trained knowledge. Use when working with wrangler.

### `observability` (16 skills)

- [`bugs-are-annoying`](observability/bugs-are-annoying/SKILL.md): Adversarial code auditor that hunts down bugs, logic errors, and security flaws. Use for deep correctness passes, not style reviews. Use when working with bugs are annoying.
- [`build-dashboard`](observability/build-dashboard/SKILL.md): Build an interactive HTML dashboard with charts, filters, and tables. Use when creating an executive overview with KPI cards, turning query results into a shareable self-contained report, building a team monitoring snapshot, or needing multiple charts with filters in one browser-openable file.
- [`competitor-monitor`](observability/competitor-monitor/SKILL.md): Set up ongoing competitor monitoring. Use when: defining tracked competitors, scan frequency, change detection alerts.
- [`database-migrations-migration-observability`](observability/database-migrations-migration-observability/SKILL.md): Migration monitoring, CDC, and observability infrastructure. Use when working with database migrations migration observability.
- [`grpc-golang`](observability/grpc-golang/SKILL.md): Build production-ready gRPC services in Go with mTLS, streaming, and observability. Use when designing Protobuf contracts with Buf or implementing secure service-to-service transport.
- [`incident-responder`](observability/incident-responder/SKILL.md): Expert SRE incident responder specializing in rapid problem resolution, modern observability, and comprehensive incident management. Use when working with incident responder.
- [`multi-agent-task-orchestrator`](observability/multi-agent-task-orchestrator/SKILL.md): Route tasks to specialized AI agents with anti-duplication, quality gates, and 30-minute heartbeat monitoring. Use when working with multi agent task orchestrator.
- [`observability-and-instrumentation`](observability/observability-and-instrumentation/SKILL.md): Instruments code so production behavior is visible and diagnosable. Use when adding logging, metrics, tracing, or alerting. Use when shipping any feature that runs in production and you need evidence it works. Use when production issues are reported but you can't tell what happened.
- [`observability-monitoring-monitor-setup`](observability/observability-monitoring-monitor-setup/SKILL.md): You are a monitoring and observability expert specializing in implementing comprehensive monitoring solutions. Set up metrics collection, distributed tracing, log aggregation, and create insightful da. Use when working with observability monitoring monitor setup.
- [`observability-monitoring-slo-implement`](observability/observability-monitoring-slo-implement/SKILL.md): You are an SLO (Service Level Objective) expert specializing in implementing reliability standards and error budget-based engineering practices. Design comprehensive SLO frameworks, establish meaningful SLIs, and create monitoring systems that balance reliability with feature velocity. Use when working with observability monitoring slo implement.
- [`performance-engineer`](observability/performance-engineer/SKILL.md): Expert performance engineer specializing in modern observability,. Use when working with performance engineer.
- [`risk-metrics-calculation`](observability/risk-metrics-calculation/SKILL.md): Calculate portfolio risk metrics including VaR, CVaR, Sharpe, Sortino, and drawdown analysis. Use when measuring portfolio risk, implementing risk limits, or building risk monitoring systems.
- [`shipping-and-launch`](observability/shipping-and-launch/SKILL.md): Prepares production launches. Use when preparing to deploy to production. Use when you need a pre-launch checklist, when setting up monitoring, when planning a staged rollout, or when you need a rollback strategy.
- [`site-activity`](observability/site-activity/SKILL.md): Query and summarize site activity logs for a Webflow enterprise site. Surfaces recent changes, identifies who made them, and generates human-readable activity reports. Use for site monitoring, change tracking, publish preparation, or weekly activity summaries. Enterprise plans only. Use when working with site activity.
- [`vercel-cli-with-tokens`](observability/vercel-cli-with-tokens/SKILL.md): Deploy and manage projects on Vercel using token-based authentication. Use when working with Vercel CLI using access tokens rather than interactive login — e.g. \\\"deploy to vercel\\\", \\\"set up vercel\\\", \\\"add environment variables to vercel\\\".
- [`workers-best-practices`](observability/workers-best-practices/SKILL.md): Reviews and authors Cloudflare Workers code against production best practices. Load when writing new Workers, reviewing Worker code, configuring wrangler.jsonc, or checking for common Workers anti-patterns (streaming, floating promises, global state, secrets, bindings, observability). Biases towards retrieval from Cloudflare docs over pre-trained knowledge. Use when working with workers best practices.

### `server-management` (6 skills)

- [`agents-sdk`](server-management/agents-sdk/SKILL.md): Build AI agents on Cloudflare Workers using the Agents SDK. Load when creating stateful agents, durable workflows, real-time WebSocket apps, scheduled tasks, MCP servers, chat applications, voice agents, or browser automation. Covers Agent class, state management, callable RPC, Workflows, durable execution, queues, retries, observability, and React hooks. Biases towards retrieval from Cloudflare docs over pre-trained knowledge. Use when working with agents sdk.
- [`bash-linux`](server-management/bash-linux/SKILL.md): Bash/Linux terminal patterns. Critical commands, piping, error handling, scripting. Use when working on macOS or Linux systems.
- [`linux-privilege-escalation`](server-management/linux-privilege-escalation/SKILL.md): Execute systematic privilege escalation assessments on Linux systems to identify and exploit misconfigurations, vulnerable services, and security weaknesses that allow elevation from low-privilege user access to root-level control. Use when working with linux privilege escalation.
- [`pm2`](server-management/pm2/SKILL.md): Execute pm2 tasks, workflows, and automated procedures. Use when working with pm2.
- [`react-best-practices`](server-management/react-best-practices/SKILL.md): Comprehensive performance optimization guide for React and Next.js applications, maintained by Vercel. Use when writing new React components or Next.js pages, implementing data fetching (client or server-side), or reviewing code for performance issues.
- [`server-management`](server-management/server-management/SKILL.md): Server management principles and decision-making. Process management, monitoring strategy, and scaling decisions. Teaches thinking, not commands. Use when working with server management.
