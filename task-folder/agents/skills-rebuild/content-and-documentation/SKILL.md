---
name: content-and-documentation
description: Technical documentation, research synthesis, slide presentations, and copywriting. Direct category router indexing 62 canonical skills across 4 subcategories.
type: category-router
version: 1.0.0
---

# `content-and-documentation` Category Router

## Overview

This category router directly indexes **62 canonical active skills** across **4 subcategories** in the `content-and-documentation` domain.

## When to Use

Use this router when the request involves technical documentation, research synthesis, slide presentations, and copywriting.

## Scope Boundaries & Handoffs

| Adjacent Domain | Category Router | Handoff Trigger |
|---|---|---|
| business-and-operations | [`business-and-operations`](../business-and-operations/SKILL.md) | Requests primarily focused on business strategy, startup finance, product management, and legal/governance workflows. |
| data-and-ai | [`data-and-ai`](../data-and-ai/SKILL.md) | Requests primarily focused on data engineering, machine learning pipelines, llm/rag systems, analytics, and vector databases. |
| design-and-experience | [`design-and-experience`](../design-and-experience/SKILL.md) | Requests primarily focused on ui/ux design, visual design systems, aesthetic critique, and motion graphics. |
| development | [`development`](../development/SKILL.md) | Requests primarily focused on software development across frontend, backend, fullstack, mobile, systems, and architecture. |
| infrastructure-and-ops | [`infrastructure-and-ops`](../infrastructure-and-ops/SKILL.md) | Requests primarily focused on cloud hosting, ci/cd pipelines, container orchestration, observability, and server operations. |
| marketing-and-seo | [`marketing-and-seo`](../marketing-and-seo/SKILL.md) | Requests primarily focused on organic search (technical/on-page/local seo), conversion rate optimization (cro), and campaign marketing. |
| meta-and-agent-skills | [`meta-and-agent-skills`](../meta-and-agent-skills/SKILL.md) | Requests primarily focused on agent architecture, agent skill authoring, validation, and lifecycle management. |
| quality-and-security | [`quality-and-security`](../quality-and-security/SKILL.md) | Requests primarily focused on software testing, security vulnerability auditing, runtime debugging, and compliance governance. |
| workflow-and-automation | [`workflow-and-automation`](../workflow-and-automation/SKILL.md) | Requests primarily focused on workflow automation, mcp tool integrations, web scraping, and version control workflows. |

## Domain Policy & Shared Guidelines

- All workflows under `content-and-documentation` adhere to standard domain principles and deterministic execution standards.
- Select the matching canonical leaf skill below based on task outcome.

## Subcategory Routing Index

### `copywriting` (4 skills)

- [`copywriting`](copywriting/copywriting/SKILL.md): Write rigorous, conversion-focused marketing copy for landing pages and emails. Enforces brief confirmation and strict no-fabrication rules. Use when working with copywriting.
- [`copywriting-psychologist`](copywriting/copywriting-psychologist/SKILL.md): One sentence - what this skill does and when to invoke it. Use when working with copywriting psychologist.
- [`devrel-content`](copywriting/devrel-content/SKILL.md): When the user wants to create technical content for developers including blog posts, tutorials, and documentation. Trigger phrases include \\"write a blog post,\\" \\"technical article,\\" \\"developer content,\\" \\"tutorial,\\" \\"devrel content,\\" \\"dev blog,\\" \\"technical writing,\\" or \\"content for. Use when working with devrel content.
- [`professional-proofreader`](copywriting/professional-proofreader/SKILL.md): Execute professional-proofreader tasks, workflows, and automated procedures. Use when working with professional proofreader.

### `presentations` (13 skills)

- [`2slides-ppt-generator`](presentations/2slides-ppt-generator/SKILL.md): AI-powered presentation generation via the 2slides API — create slides from text, match a reference image style, summarize documents into decks, add AI voice narration, and export pages/audio. Use for any \\\"make slides\\\", \\\"create a deck\\\", or \\\"slides from this document\\\" request. Use when working with 2slides ppt generator.
- [`client-proposal`](presentations/client-proposal/SKILL.md): Draft agency proposals. Use when: pitch deck, scope of work, SLA, capabilities presentation for prospects or clients.
- [`google-slides-automation`](presentations/google-slides-automation/SKILL.md): Lightweight Google Slides integration with standalone OAuth authentication. No MCP server required. Full read/write access. Use when working with google slides automation.
- [`mdpr-skill`](presentations/mdpr-skill/SKILL.md): Review MDPR Markdown presentation workflows with semantic hints, visual checks, and deterministic renderer boundaries. Use when working with mdpr skill.
- [`nanobanana-ppt-skills`](presentations/nanobanana-ppt-skills/SKILL.md): AI-powered PPT generation with document analysis and styled images. Use when working with nanobanana ppt skills.
- [`narrative-tracker`](presentations/narrative-tracker/SKILL.md): Track AI engine brand narratives. Use when: detecting narrative drift, misrepresentation, or competitor narrative gains over time.
- [`notebooklm`](presentations/notebooklm/SKILL.md): Execute notebooklm tasks, workflows, and automated procedures. Use when working with notebooklm.
- [`notebooklm-create`](presentations/notebooklm-create/SKILL.md): Execute notebooklm-create tasks, workflows, and automated procedures. Use when working with notebooklm create.
- [`pdf-conversion-router`](presentations/pdf-conversion-router/SKILL.md): Use when converting a PDF into another format such as Markdown, HTML, text, JSON, DOCX, or structured notes and the agent must choose the best extraction route, settings, and cleanup strategy for maximum fidelity and readability.
- [`pptx-deck-creation`](presentations/pptx-deck-creation/SKILL.md): Create editable, production-ready PPTX decks with narrative planning, explicit layout specs, asset guidance, and quality checks. Use when working with pptx deck creation.
- [`pptx-official`](presentations/pptx-official/SKILL.md): A user may ask you to create, edit, or analyze the contents of a .pptx file. A .pptx file is essentially a ZIP archive containing XML files and other resources that you can read or edit. You have different tools and workflows available for different tasks. Use when working with pptx official.
- [`python-pptx-generator`](presentations/python-pptx-generator/SKILL.md): Generate complete Python scripts that build polished PowerPoint decks with python-pptx and real slide content. Use when working with python pptx generator.
- [`qbr-plan`](presentations/qbr-plan/SKILL.md): Prepare a Quarterly Business Review. Use when: building QBR presentations, client performance reviews, or strategy updates.

### `research-and-synthesis` (5 skills)

- [`agents-md`](research-and-synthesis/agents-md/SKILL.md): This skill should be used when the user asks to \\"create AGENTS.md\\", \\"update AGENTS.md\\", \\"maintain agent docs\\", \\"set up CLAUDE.md\\", or needs to keep agent instructions concise. Enforces research-backed best practices for minimal, high-signal agent documentation. Use when working with agents md.
- [`context7-auto-research`](research-and-synthesis/context7-auto-research/SKILL.md): Automatically fetch latest library/framework documentation for Claude Code via Context7 API. Use when you need up-to-date documentation for libraries and frameworks or asking about React, Next.js, Prisma, or any other popular library.
- [`latex-paper-conversion`](research-and-synthesis/latex-paper-conversion/SKILL.md): This skill should be used when the user asks to convert an academic paper in LaTeX from one format (e.g., Springer, IPOL) to another format (e.g., MDPI, IEEE, Nature). It automates extraction, injection, fixing formatting, and compiling. Use when working with latex paper conversion.
- [`pubmed-database`](research-and-synthesis/pubmed-database/SKILL.md): Direct REST API access to PubMed. Advanced Boolean/MeSH queries, E-utilities API, batch processing, citation management. For Python workflows, prefer biopython (Bio.Entrez). Use this for direct HTTP/REST work or custom API implementations. Use when working with pubmed database.
- [`research-documentation`](research-and-synthesis/research-documentation/SKILL.md): Research topics and produce comprehensive written documentation. Synthesizes information into clear, well-structured, authoritative content pieces. Use when working with research documentation.

### `technical-writing` (40 skills)

- [`api-documentation`](technical-writing/api-documentation/SKILL.md): API documentation workflow for generating OpenAPI specs, creating developer guides, and maintaining comprehensive API documentation. Use when working with api documentation.
- [`api-documentation-generator`](technical-writing/api-documentation-generator/SKILL.md): Generate comprehensive, developer-friendly API documentation from code, including endpoints, parameters, examples, and best practices. Use when working with api documentation generator.
- [`api-documenter`](technical-writing/api-documenter/SKILL.md): Master API documentation with OpenAPI 3.1, AI-powered tools, and modern developer experience practices. Create interactive docs, generate SDKs, and build comprehensive developer portals. Use when working with api documenter.
- [`api-endpoint-builder`](technical-writing/api-endpoint-builder/SKILL.md): Builds production-ready REST API endpoints with validation, error handling, authentication, and documentation. Follows best practices for security and scalability. Use when working with api endpoint builder.
- [`api-onboarding`](technical-writing/api-onboarding/SKILL.md): Reduce time-to-first-API-call (TTFAC) by optimizing every step of the developer onboarding journey. This skill covers authentication simplification, sandbox environments, interactive documentation, and identifying and eliminating common failure points. Trigger phrases: \\"API. Use when working with api onboarding.
- [`architecture`](technical-writing/architecture/SKILL.md): Architectural decision-making framework. Requirements analysis, trade-off evaluation, ADR documentation. Use when making architecture decisions or analyzing system design.
- [`brain-to-docs`](technical-writing/brain-to-docs/SKILL.md): Interview the user to turn project vision and decisions into README and ADR documentation. Use when working with brain to docs.
- [`brand-guidelines`](technical-writing/brand-guidelines/SKILL.md): Write copy following Sentry brand guidelines. Use when writing UI text, error messages, empty states, onboarding flows, 404 pages, documentation, marketing copy, or any user-facing content. Covers both Plain Speech (default) and Sentry Voice tones.
- [`build-workspace-docs`](technical-writing/build-workspace-docs/SKILL.md): Use when regenerating README.md and WORK_AREAS.md in a managed library workspace. Always dry-run first to preview changes.
- [`building-components`](technical-writing/building-components/SKILL.md): Guide for building modern, accessible, and composable UI components. Use when building new components, implementing accessibility, creating composable APIs, setting up design tokens, publishing to npm/registry, or writing component documentation.
- [`code-documentation`](technical-writing/code-documentation/SKILL.md): Writing effective code documentation - API docs, README files, inline comments, and technical guides. Use for documenting codebases, APIs, or writing developer guides. Use when working with code documentation.
- [`code-documentation-code-explain`](technical-writing/code-documentation-code-explain/SKILL.md): You are a code education expert specializing in explaining complex code through clear narratives, visual diagrams, and step-by-step breakdowns. Transform difficult concepts into understandable explanations for developers at all levels. Use when working with code documentation code explain.
- [`code-documentation-doc-generate`](technical-writing/code-documentation-doc-generate/SKILL.md): You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. Generate API docs, architecture diagrams, user guides, and technical references using AI-powered analysis and industry best practices. Use when working with code documentation doc generate.
- [`context-driven-development`](technical-writing/context-driven-development/SKILL.md): Guide for implementing and maintaining context as a managed artifact alongside code, enabling consistent AI interactions and team alignment through structured project documentation. Use when working with context driven development.
- [`daily`](technical-writing/daily/SKILL.md): Documentation and capabilities reference for Daily. Use when working with daily.
- [`developer-onboarding`](technical-writing/developer-onboarding/SKILL.md): Get developers to \\"Hello World\\" fast with optimized quickstarts, tutorials, and sample apps. Trigger phrases: developer onboarding, time to first value, quickstart guide, hello world tutorial, developer activation, onboarding checklist, sample apps, getting started experience, reduce. Use when working with developer onboarding.
- [`docs-architect`](technical-writing/docs-architect/SKILL.md): Creates comprehensive technical documentation from existing codebases. Analyzes architecture, design patterns, and implementation details to produce long-form technical manuals and ebooks. Use when working with docs architect.
- [`docs-as-marketing`](technical-writing/docs-as-marketing/SKILL.md): Transform documentation into a powerful marketing channel that attracts, converts, and retains developers. This skill covers creating documentation that ranks in search, converts visitors into users, and accelerates adoption through exceptional information architecture and. Use when working with docs as marketing.
- [`docs-guard`](technical-writing/docs-guard/SKILL.md): Review generated or changed documentation before it ships, including READMEs, API references, docstrings, changelogs, tutorials, and documentation sites. Use when working with docs guard.
- [`documentation`](technical-writing/documentation/SKILL.md): Documentation generation workflow covering API docs, architecture docs, README files, code comments, and technical writing. Use when working with documentation.
- [`documentation-and-adrs`](technical-writing/documentation-and-adrs/SKILL.md): Records decisions and documentation. Use when making architectural decisions, changing public APIs, shipping features, or when you need to record context that future engineers and agents will need to understand the codebase.
- [`documentation-generation-doc-generate`](technical-writing/documentation-generation-doc-generate/SKILL.md): You are a documentation expert specializing in creating comprehensive, maintainable documentation from code. Generate API docs, architecture diagrams, user guides, and technical references using AI-powered analysis and industry best practices. Use when working with documentation generation doc generate.
- [`documentation-templates`](technical-writing/documentation-templates/SKILL.md): Documentation templates and structure guidelines. README, API docs, code comments, and AI-friendly documentation. Use when working with documentation templates.
- [`hugo-to-markdown`](technical-writing/hugo-to-markdown/SKILL.md): Convert Hugo documentation sites and Hugo-managed content into standard Markdown. Use when Agent needs to inspect a local Hugo repository, read hugo.toml or config files, content/, archetypes/, layouts/_shortcodes/, layouts/_markup/, and related docs content, then produce Markdown.
- [`image`](technical-writing/image/SKILL.md): Upload local images to GitHub and get canonical user-attachments embed URLs; use when asked to attach a screenshot to a PR, issue, or comment, or to embed before/after images in a README.
- [`imagen`](technical-writing/imagen/SKILL.md): AI image generation skill powered by Google Gemini, enabling seamless visual content creation for UI placeholders, documentation, and design assets. Use when working with imagen.
- [`interview-style-doc-building`](technical-writing/interview-style-doc-building/SKILL.md): Build structured strategy documents by asking one question at a time and patching the file. Use when working with interview style doc building.
- [`knowledge-distribution`](technical-writing/knowledge-distribution/SKILL.md): Share and distribute skill knowledge and documentation. Publishes capabilities with examples, documentation, and integration guides. Use when working with knowledge distribution.
- [`notebook-lm-api`](technical-writing/notebook-lm-api/SKILL.md): Interact with Google NotebookLM to query documentation with Gemini's source-grounded answers. Each question opens a fresh browser session, retrieves the answer exclusively from your uploaded documents, and closes. Use when working with notebook lm api.
- [`planning-documentation`](technical-writing/planning-documentation/SKILL.md): Document and communicate plans clearly. Structures implementation plans with tasks, decisions, and success criteria. Use when working with planning documentation.
- [`pr-merge-champion`](technical-writing/pr-merge-champion/SKILL.md): Optimize pull requests for quick approval and merging by ensuring clean diffs, comprehensive self-reviews, and structured documentation. Use when working with pr merge champion.
- [`presence`](technical-writing/presence/SKILL.md): When the user wants to optimize their GitHub profile, README, or project discoverability. Trigger phrases include \\"GitHub README,\\" \\"README optimization,\\" \\"GitHub profile,\\" \\"GitHub stars,\\" \\"GitHub discoverability,\\" \\"awesome lists,\\" or \\"GitHub marketing. Use when working with presence.
- [`readme`](technical-writing/readme/SKILL.md): You are an expert technical writer creating comprehensive project documentation. Your goal is to write a README.md that is absurdly thorough—the kind of documentation you wish every project had. Use when working with readme.
- [`reference-builder`](technical-writing/reference-builder/SKILL.md): Creates exhaustive technical references and API documentation. Generates comprehensive parameter listings, configuration guides, and searchable reference materials. Use when working with reference builder.
- [`source-driven-development`](technical-writing/source-driven-development/SKILL.md): Grounds every implementation decision in official documentation. Use when you want authoritative, source-cited code free from outdated patterns. Use when building with any framework or library where correctness matters.
- [`technical-tutorials`](technical-writing/technical-tutorials/SKILL.md): When the user wants to create step-by-step technical tutorials, quickstarts, or code walkthroughs. Trigger phrases include \\"tutorial,\\" \\"quickstart,\\" \\"getting started guide,\\" \\"walkthrough,\\" \\"step by step,\\" \\"how to guide,\\" \\"hands-on guide,\\" or \\"code tutorial. Use when working with technical tutorials.
- [`tutorial-engineer`](technical-writing/tutorial-engineer/SKILL.md): Creates step-by-step tutorials and educational content from code. Transforms complex concepts into progressive learning experiences with hands-on examples. Use when working with tutorial engineer.
- [`web-perf`](technical-writing/web-perf/SKILL.md): Analyzes web performance using Chrome DevTools MCP. Measures Core Web Vitals (LCP, INP, CLS) and supplementary metrics (FCP, TBT, Speed Index), identifies render-blocking resources, network dependency chains, layout shifts, caching issues, and accessibility gaps. Use when asked to audit, profile, debug, or optimize page load performance, Lighthouse scores, or site speed. Biases towards retrieval from current documentation over pre-trained knowledge.
- [`wiki-architect`](technical-writing/wiki-architect/SKILL.md): You are a documentation architect that produces structured wiki catalogues and onboarding guides from codebases. Use when working with wiki architect.
- [`wiki-page-writer`](technical-writing/wiki-page-writer/SKILL.md): You are a senior documentation engineer that generates comprehensive technical documentation pages with evidence-based depth. Use when working with wiki page writer.
