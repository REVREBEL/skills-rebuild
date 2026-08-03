# Task: Audit, Refactor, and Rebuild the Agent Skills Library

## Objective

Review every skill currently stored in:

```text
agents/skills
```

Classify each skill, remove skills that do not fit the approved application stack, convert reusable Claude-specific skills into platform-neutral or Codex-compatible skills, consolidate overlapping skills, split oversized skills, and organize the final approved library into functional skill groups.

Use the attached `design-it` skill package as the structural reference. The desired pattern is:

* A parent `SKILL.md` that routes work to focused child skills
* Child folders containing narrowly scoped functional skills
* Clear trigger boundaries
* Minimal duplication between parent and child instructions
* Predictable folder and skill names
* A navigable index of available capabilities

Place all final, reorganized, production-ready skills in:

```text
agents/skills-rebuild
```

Move rejected or superseded source skills to:

```text
agents/not-needed
```

Do not permanently delete any source skill.

---

## Source and Destination Folders

### Source library

```text
agents/skills
```

Treat this as the source material. Do not perform broad destructive rewrites in this folder during the audit.

### Rejected or unnecessary skills

```text
agents/not-needed
```

Move skills here when they are:

* Built primarily for an application or framework outside the approved stack
* Explicitly tied to an excluded application
* Obsolete or technically invalid
* Fully superseded by another retained skill
* Too Claude-specific to convert without destroying their intended function
* Duplicative without containing unique guidance worth preserving
* Incomplete, unusable, or unsupported by the current environment

Preserve each rejected skill intact unless a renamed folder is required to avoid a collision.

### Final rebuilt library

```text
agents/skills-rebuild
```

This folder must contain only the finalized, reorganized, validated skill system.

Do not treat `skills-rebuild` as a dumping ground for lightly edited copies. Every item placed there must have a clear role in the final architecture.

---

## Authoritative Application Stack

Use the following document as the authoritative compatibility reference:

```text
https://docs.google.com/document/d/1NUQo22mRIji4yx5ORS3whPH3OghroRmX3VsxWEjDVr0/edit
```

When reviewing an application-specific skill, determine whether its primary application, platform, framework, or runtime is part of that approved stack.

The approved stack includes, but is not limited to:

### Development and infrastructure

* macOS
* Ubuntu
* Docker
* Docker Compose
* Node.js
* Python
* JavaScript
* TypeScript
* React
* Next.js
* Tailwind CSS
* shadcn/ui
* Radix UI
* GitHub
* GitHub Actions
* Vercel
* Nginx
* PM2
* Cloudflare Workers
* Cloudflare Tunnel
* Google Cloud Platform
* BigQuery
* PostgreSQL
* SQL
* pandas
* Drizzle ORM
* rclone
* REST APIs
* Webhooks
* Model Context Protocol

### AI and development environments

* ChatGPT
* Codex
* Claude
* Gemini
* Cursor
* Trae
* Google Antigravity
* Visual Studio Code
* Pieces
* Hugging Face

Claude appearing in the approved application profile does not override the special Claude-conversion requirements below. Final skills should not remain dependent on Claude Code unless the capability is intrinsically Claude-specific and cannot reasonably be generalized.

### Production and work platforms

* Google Workspace
* Google Drive
* Google Docs
* Google Sheets
* Google Slides
* Gmail
* Google Calendar
* Google Apps Script
* Google Workspace APIs
* n8n
* Linear
* Storybook
* Chrome DevTools
* Obsidian
* JSON Canvas
* Markdown
* JSON
* CSV

### Design, web, analytics, and content systems

* Figma
* Canva
* Google Stitch
* Adobe Creative Cloud
* Adobe Firefly
* Photoshop
* Illustrator
* Acrobat
* Adobe Express
* Freepik
* Webflow
* Google Analytics 4
* Google Tag Manager
* Google Search Console
* Google Business Profile

### Authentication and secrets

* 1Password
* 1Password Secrets Automation
* Clerk
* Google Cloud service accounts

### Hospitality commercial technology

* StayNTouch PMS
* SynXis CRS
* SynXis Booking Engine
* Duetto RMS
* IDeaS RMS
* Oracle OPERA Cloud PMS
* Sabre hospitality and distribution tools
* Booking.com Extranet
* Expedia Partner Central
* Google Hotel Ads
* Hotel metasearch platforms

Evaluate the skill’s **primary dependency**, not every passing reference. A generic development skill should not be rejected merely because one example mentions an unapproved library.

---

## Explicitly Excluded Technologies

Skills primarily built around the following should normally be moved to `agents/not-needed`:

* Expo
* EAS Update
* AWS Lambda
* Azure Functions
* HashiCorp Vault
* AWS Secrets Manager
* Azure Key Vault
* Ditto session-mining tools
* GDB-specific workflows
* `gdb-cli`
* Ruby
* Rails
* Windows-specific administration
* Fedora-specific administration
* Azul-specific tooling

A skill may be retained only when its useful principles can be fully generalized without preserving the excluded dependency.

---

## Required Review Process

Review every skill individually. Every source skill must receive exactly one documented primary disposition:

1. **Keep as-is**
2. **Refine**
3. **Convert**
4. **Split**
5. **Merge**
6. **Move to not-needed**

Do not skip files because their names appear unimportant. Read the actual skill content and supporting files before deciding.

---

## Decision Criteria

### 1. Keep as-is

A skill may be kept substantially unchanged when it:

* Supports the approved application stack
* Has a clear and narrow purpose
* Uses correct, current instructions
* Has useful trigger conditions
* Does not duplicate another skill
* Is reasonably sized
* Does not rely on Claude-only tools or conventions
* Has no broken internal references
* Can fit cleanly into the rebuilt functional hierarchy

Minor metadata normalization is still permitted.

### 2. Refine

Refine a skill when its purpose is useful but its implementation needs improvement.

Common refinement reasons include:

* Vague trigger language
* Excessive repetition
* Outdated instructions
* Weak safety or validation rules
* Missing prerequisites
* Missing completion checks
* Incorrect tool names
* Poorly structured frontmatter
* Excessive examples obscuring the core workflow
* Instructions written for an agent environment that no longer exists
* Hardcoded paths that should be relative or configurable
* References to unavailable tools that can be replaced with supported equivalents

Refinement should preserve the useful intent while removing unnecessary bulk.

### 3. Convert

Convert a skill when it is currently Claude-specific but its capability is useful beyond Claude.

The converted version should be:

* Platform-neutral where possible
* Codex-compatible where platform neutrality is impractical
* Written around capabilities rather than proprietary tool names
* Free from Claude Code assumptions unless they are unavoidable

Scrub or replace references such as:

* Claude Code
* `CLAUDE.md`
* `.claude/`
* Claude-only slash commands
* Claude-only hooks
* Claude-only subagent syntax
* Claude-specific tool-call names
* Anthropic-specific prompt wrappers
* Claude-specific permission systems
* Claude-specific planning or task-list commands
* Statements assuming the active model is Claude
* Instructions telling the agent to use a Claude-only feature

Preserve the underlying workflow when it remains useful.

Examples:

* “Use Claude’s TodoWrite tool” should become a general requirement to maintain and update a task checklist.
* “Read CLAUDE.md” should become “Read the repository’s governing agent instructions,” with supported filenames or discovery rules.
* “Create a Claude subagent” should become “Delegate to a specialized agent when the active environment supports delegation.”
* Claude-specific file locations should become neutral configurable paths.

After conversion, search the rebuilt skill and its supporting files for remaining Claude-specific references.

Do not remove legitimate references to the Anthropic API when the skill is specifically about integrating or troubleshooting that API. However, such a skill should be moved to `not-needed` when Anthropic integration is not part of the approved working stack or cannot be generalized.

### 4. Split

Split a skill when it contains multiple independently useful capabilities that should have different triggers.

Signals that a split may be needed include:

* Multiple unrelated workflows in one file
* Separate workflows for creation, debugging, deployment, and auditing
* One section can be used without the others
* Different applications or runtimes require different prerequisites
* The skill is difficult to route because its description covers too many intents
* The file is very long because it combines several complete procedures

Length alone is not sufficient reason to split a skill. Split according to functional boundaries.

When splitting:

* Create one parent router skill when the children belong to the same functional family
* Move shared principles into the parent only when all children need them
* Keep execution details inside the child skills
* Avoid copying the same instructions into every child
* Document the relationship between the original skill and the new children

### 5. Merge

Merge skills when two or more skills:

* Trigger on substantially the same request
* Produce the same type of outcome
* Repeat most of the same instructions
* Differ only through minor wording or examples
* Represent fragmented parts of one natural workflow

Do not merge merely because two skills share a broad category.

When merging:

* Preserve every uniquely useful instruction
* Choose a clear canonical name
* Remove contradictions
* Consolidate frontmatter
* Record all original source paths in the audit manifest
* Move fully superseded originals to `agents/not-needed`
* Prevent duplicate triggers in the rebuilt library

### 6. Move to not-needed

Move a skill to `agents/not-needed` when:

* Its primary application is outside the approved stack
* It is tied to an explicitly excluded technology
* It cannot be made useful without its unsupported dependency
* It is an obsolete implementation of a retained capability
* Another rebuilt skill fully supersedes it
* It contains no substantial reusable guidance
* It is broken beyond reasonable repair
* It is Claude-specific and cannot be converted
* It introduces unnecessary risk or unsupported behavior

Include a documented reason for every rejected skill.

---

## Rebuilt Skill Architecture

Use the attached `design-it` package as the architecture model, not as content to copy.

The final library should use a structure similar to:

```text
agents/skills-rebuild/
├── SKILL.md
├── README.md
├── development/
│   ├── SKILL.md
│   ├── nextjs/
│   │   └── SKILL.md
│   ├── github/
│   │   └── SKILL.md
│   └── debugging/
│       └── SKILL.md
├── infrastructure/
│   ├── SKILL.md
│   ├── docker/
│   │   └── SKILL.md
│   └── ubuntu-services/
│       └── SKILL.md
├── data-analytics/
│   ├── SKILL.md
│   ├── bigquery/
│   │   └── SKILL.md
│   └── data-transformation/
│       └── SKILL.md
└── ...
```

The exact categories must emerge from the reviewed skills. Do not create empty or artificial categories merely to match this example.

Likely functional categories may include:

* AI and agents
* Automation and integrations
* Data and analytics
* Design and UX
* Development
* Documentation and knowledge management
* Frontend and UI
* Infrastructure and deployment
* Marketing and SEO
* Research
* Testing and debugging
* Writing and content

Add hospitality technology only when enough retained skills justify a dedicated functional group.

Keep the hierarchy shallow:

```text
skills-rebuild/
  category/
    SKILL.md
    child-skill/
      SKILL.md
```

Avoid unnecessary third- and fourth-level nesting.

---

## Parent Router Requirements

Each functional category should have a parent `SKILL.md` that:

* Explains the category’s purpose
* Defines when the category should be used
* Routes requests to the correct child skill
* Lists each child skill and its relative path
* Distinguishes overlapping child triggers
* Includes important shared constraints
* Does not repeat each child’s full workflow
* Does not contain application instructions unrelated to the category
* Uses relative paths that work inside the repository

Create a root-level `agents/skills-rebuild/SKILL.md` that routes broadly between the functional categories.

---

## Child Skill Requirements

Each child skill should:

* Solve one clearly defined functional job
* Have a unique name
* Use a lowercase kebab-case folder name
* Contain a `SKILL.md`
* Include valid frontmatter
* Have a precise trigger description
* Define when to use and when not to use it
* State prerequisites
* Provide an ordered execution workflow
* Include validation or completion checks
* Describe important failure conditions
* Avoid hardcoded assumptions about the active model
* Avoid unsupported application dependencies
* Avoid duplicating its parent router
* Avoid claiming tools or permissions that may not exist
* Use relative file references
* Preserve important safety boundaries from the source material

Supporting files may remain beside a child skill when they are genuinely required.

---

## Frontmatter Normalization

Normalize skill frontmatter across the rebuilt library.

At minimum, include:

```yaml
---
name: example-skill
description: Clear trigger-oriented description of the skill.
category: development
risk: safe
source: rebuilt
source_type: derived
---
```

Retain other useful fields only when they have a clear function.

Remove or correct:

* Incorrect `tools` declarations
* Claude-only tool declarations
* Duplicated metadata
* Invalid YAML
* Conflicting names
* Stale dates that imply the rebuilt skill was created earlier than it was
* Unsupported application requirements
* Metadata that does not affect discovery, routing, provenance, or execution

Descriptions should explain when the skill should trigger, not merely define the subject.

---

## Audit Deliverables

Create the following inside:

```text
agents/skills-rebuild/_audit
```

### 1. `skills-inventory.csv`

Include one row for every original skill with these columns:

```text
source_path
original_name
primary_function
application_dependencies
claude_specific
decision
final_category
final_path
merged_into
split_into
reason
validation_status
```

Every source skill must appear exactly once.

### 2. `review-report.md`

Summarize:

* Total skills reviewed
* Skills kept as-is
* Skills refined
* Skills converted from Claude-specific instructions
* Skills split
* Skills merged
* Skills moved to `not-needed`
* Final functional categories
* Important architectural decisions
* Known limitations
* Any skills requiring human review

### 3. `merge-split-map.md`

Document:

* Every merge
* Every split
* Original source paths
* New canonical skill paths
* Why the restructure was necessary
* Which unique instructions were preserved

### 4. `claude-conversion-report.md`

For every Claude-specific source skill, record:

* Original path
* Claude-specific dependencies found
* Whether it was converted or rejected
* Replacement language or workflow
* Final destination
* Remaining Anthropic references, if any
* Reason any remaining Anthropic reference is legitimate

### 5. `application-compatibility-report.md`

List application-specific skills and identify:

* Application or framework
* Whether it is approved
* Whether the skill was retained
* Whether it was generalized
* Whether it was moved to `not-needed`
* The reason for the decision

---

## File-Handling Rules

* Do not delete source skills.
* Use safe moves for rejected skills.
* Preserve supporting files when moving a rejected skill.
* Do not overwrite an existing folder without comparing its contents.
* Resolve naming collisions explicitly.
* Ignore and remove packaging artifacts such as:

```text
__MACOSX
.DS_Store
._*
```

* Do not copy secrets, credentials, `.env` contents, tokens, or generated dependencies.
* Do not include `node_modules`, build outputs, caches, or temporary files.
* Preserve source attribution where meaningful.
* Keep a traceable relationship between each original and rebuilt skill.

---

## Required Validation

Before declaring the task complete, verify all of the following:

### Coverage

* Every skill in `agents/skills` appears in the inventory.
* Every original skill has one documented decision.
* Every retained capability has a final destination.
* Every rejected skill has a reason.
* No skill silently disappears.

### Architecture

* The root router references every category.
* Every category router references its child skills.
* All referenced paths exist.
* No child is orphaned.
* No folder contains multiple unrelated skills without a router.
* The hierarchy does not contain unnecessary nesting.

### Content

* Rebuilt skills have valid frontmatter.
* Skill names are unique.
* Trigger descriptions are clear and non-overlapping.
* Relative links resolve.
* Supporting files exist.
* No skill references missing source files.
* No retained skill depends primarily on an excluded application.
* No retained skill contains obsolete tool calls.

### Claude conversion

Search the entire rebuilt library for terms including:

```text
Claude Code
CLAUDE.md
.claude/
TodoWrite
AskUserQuestion
Anthropic
claude-
```

Review every match manually.

A textual match does not automatically mean failure. Determine whether it is:

* An accidental remaining Claude-specific dependency
* Historical provenance in an audit file
* A legitimate Anthropic integration reference
* A comparison explaining that Claude-specific behavior was removed

Final execution skills must not retain accidental Claude-only assumptions.

### Duplication

* Search for near-identical skill descriptions.
* Search for repeated workflow sections.
* Confirm merged skills do not still coexist under old names.
* Confirm category routers do not duplicate child instructions.
* Confirm similar skills have distinct trigger boundaries.

### Quality

* Large skills have been evaluated for functional splitting.
* Tiny skills have been evaluated for consolidation.
* Code examples support the approved stack.
* Instructions clearly distinguish required actions from optional recommendations.
* Each workflow includes a completion or validation step.
* No skill claims work was performed without a verification requirement.

---

## Work Sequence

Perform the work in this order:

1. Inventory all source skills and supporting files.
2. Read the authoritative application-stack document.
3. Inspect the attached `design-it` structure.
4. Identify application-specific dependencies.
5. Identify Claude-specific skills and references.
6. Identify duplicates and overlapping triggers.
7. Identify oversized multi-function skills.
8. Produce the initial decision inventory.
9. Design the final functional category structure.
10. Build parent routers.
11. Convert, refine, merge, and split child skills.
12. Move rejected source skills to `agents/not-needed`.
13. Place all final versions in `agents/skills-rebuild`.
14. Generate audit reports.
15. Validate paths, metadata, references, routing, and coverage.
16. Perform a final search for unsupported and Claude-specific dependencies.
17. Report the completed results with counts and unresolved review items.

Do not reorganize first and analyze later. Complete the inventory and decision pass before performing broad file moves.

---

## Completion Standard

The task is complete only when:

* Every original skill has been reviewed
* Every decision is documented
* Rejected skills are safely quarantined
* Claude-specific skills are converted or rejected
* Duplicate capabilities are consolidated
* Oversized skills are appropriately split
* Final skills are grouped into functional router-based categories
* The rebuilt library is internally navigable
* All paths and references validate
* The audit reports reconcile with the actual filesystem
* `agents/skills-rebuild` contains a coherent production-ready skill library rather than a collection of unreviewed copies

At completion, provide a concise summary containing:

* Number of source skills reviewed
* Number retained
* Number refined
* Number converted
* Number merged
* Number split
* Number moved to `not-needed`
* Final category list
* Validation results
* Any decisions still requiring human judgment
