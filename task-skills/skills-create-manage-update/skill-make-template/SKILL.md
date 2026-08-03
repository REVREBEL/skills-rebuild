---

name: make-skill-template
description: 'Create, scaffold, structure, and validate Agent Skills. Use when asked to create a skill, make a new skill, scaffold a skill folder, generate a SKILL.md file, convert instructions into the Agent Skills format, organize bundled scripts or references, duplicate a skill template, or explain the Agent Skills specification.'
compatibility: 'Requires filesystem access to create skill folders and Markdown files. Validation commands require the repository skill-validation script and Node.js.'
metadata:
category: agents
type: meta-skill
source: custom
--------------

# Make Skill Template

Create new Agent Skills that follow the Agent Skills specification and are easy for an agent to discover, understand, and execute.

Use this skill to:

* Scaffold a new skill directory
* Generate or revise a `SKILL.md`
* Convert instructions into a valid Agent Skill
* Organize scripts, references, assets, and templates
* Improve skill discovery descriptions
* Validate an existing skill
* Duplicate this skill as a starting template

## When to Use This Skill

Use this skill when the user:

* Asks to create, make, build, or scaffold a skill
* Wants to generate a `SKILL.md` file
* Wants to add a specialized capability to an agent or GitHub Copilot setup
* Provides instructions that should be converted into Agent Skills format
* Needs help organizing bundled skill resources
* Wants to duplicate an existing skill as a starting point
* Needs help understanding the Agent Skills specification
* Wants to troubleshoot skill discovery or validation failures
* Wants to split, merge, normalize, or refine an existing skill

Do not use this skill merely to execute another skill’s workflow. Use it when the requested outcome is the skill definition or folder structure itself.

## Prerequisites

Before creating a skill, determine:

1. What job the skill must accomplish
2. When the skill should activate
3. What prompts, keywords, files, applications, or scenarios should trigger it
4. Which tools or environment capabilities it requires
5. Whether it needs bundled scripts, references, assets, or templates
6. Whether the requested capability already exists in another skill

Do not create a duplicate skill when an existing skill can be safely extended or refined.

## Core Design Principles

### One Clear Functional Job

Each child skill should solve one clearly defined job.

Avoid combining unrelated capabilities solely because they use the same application or programming language.

A parent router skill may cover a broader functional category, but it should route to focused child skills rather than contain every detailed workflow itself.

### Discovery-First Description

The `description` field is the primary mechanism for automatic skill discovery.

It must explain:

* What the skill does
* When it should be used
* Which scenarios trigger it
* Which keywords or file types users may mention

Do not rely on the body of the skill to compensate for a vague description.

### Progressive Disclosure

Keep the main `SKILL.md` concise and actionable.

Move long supporting material into:

* `references/` for documentation
* `scripts/` for executable automation
* `assets/` for static resources
* `templates/` for starter files the agent should modify

Do not embed extensive API documentation, large code samples, or dozens of examples in the main skill when they can be loaded only when needed.

### Capability-Based Instructions

Write instructions around the job that must be completed, not around a specific model identity.

Avoid unnecessary assumptions such as:

* The active model is Claude
* The active model is Codex
* A particular proprietary planning tool exists
* A specific slash-command system is available
* A tool is connected merely because the skill mentions it

When a workflow requires a specific application or tool, declare that requirement explicitly.

## Creating a New Skill

### Step 1: Define the Skill Boundary

Before creating files, write a compact definition containing:

* Primary job
* Trigger scenarios
* Required inputs
* Expected outputs
* Required tools
* Explicit exclusions
* Completion checks

Evaluate whether the requested capability should be:

* One standalone skill
* A child skill within an existing category
* A parent router with several child skills
* An extension to an existing skill

### Step 2: Choose the Skill Name

Create a lowercase, hyphenated name.

The folder name and frontmatter `name` must match exactly.

```text
skills/<skill-name>/
└── SKILL.md
```

Example:

```text
skills/browser-verification/
└── SKILL.md
```

Name requirements:

* Between 1 and 64 characters
* Lowercase letters, numbers, and hyphens only
* No spaces or underscores
* No consecutive hyphens
* No leading or trailing hyphen
* Descriptive of the skill’s functional job
* Must match the containing folder name

Prefer action-oriented names such as:

```text
create-google-doc
fix-github-actions
audit-user-flow
transform-csv-data
```

Avoid vague names such as:

```text
helpers
utilities
useful-tools
misc
general
```

### Step 3: Create the Skill Directory

Create the folder using the selected skill name:

```text
skills/<skill-name>/
```

Create the required file:

```text
skills/<skill-name>/SKILL.md
```

Do not add optional folders until the skill actually requires them.

### Step 4: Add YAML Frontmatter

Every skill requires YAML frontmatter containing at least `name` and `description`.

Use this structure:

```yaml
---
name: <skill-name>
description: '<What the skill does>. Use when <specific triggers, scenarios, file types, or keywords users might mention>.'
---
```

Optional fields may include:

```yaml
license: MIT
compatibility: 'Requires Node.js 22+, Git, and filesystem write access.'
metadata:
  category: development
  type: workflow
allowed-tools: tool-one tool-two
```

Only include optional fields when they have a real operational purpose.

## Frontmatter Field Requirements

| Field           | Required | Requirements                                                        |
| --------------- | -------: | ------------------------------------------------------------------- |
| `name`          |      Yes | 1–64 characters, lowercase letters, numbers, and hyphens only       |
| `description`   |      Yes | 1–1024 characters describing what the skill does and when to use it |
| `license`       |       No | License identifier or reference to a bundled `LICENSE.txt`          |
| `compatibility` |       No | 1–500 characters describing environment or dependency requirements  |
| `metadata`      |       No | Key-value properties for categorization, provenance, or routing     |
| `allowed-tools` |       No | Space-delimited list of pre-approved tools when supported           |

Do not add unsupported metadata merely to make the frontmatter appear more sophisticated.

## Writing the Description

### Required Components

A strong description contains:

1. The skill’s primary capability
2. The situations in which it should activate
3. Prompt language or keywords users may use
4. Relevant file types, tools, or applications
5. Important boundaries when ambiguity is likely

### Strong Example

```yaml
description: 'Test and verify local web applications using Playwright. Use when asked to check frontend functionality, reproduce UI defects, capture browser screenshots, inspect console errors, validate responsive behavior, or test Chrome, Firefox, and WebKit flows.'
```

### Weak Example

```yaml
description: 'Web testing helpers.'
```

The weak example does not explain the available capabilities or when the skill should be selected.

### Description Rules

* Write the description as a single quoted YAML string
* Prefer concrete verbs
* Include realistic trigger language
* Avoid promotional language
* Avoid generic descriptions that could match many unrelated skills
* Do not list capabilities the body does not actually support
* Keep overlapping skills distinguishable through their descriptions

## Writing the Skill Body

After the frontmatter, write the skill instructions in Markdown.

Recommended structure:

```markdown
# Skill Title

Brief explanation of the skill’s purpose.

## When to Use This Skill

Trigger conditions and boundaries.

## Prerequisites

Required tools, inputs, permissions, or dependencies.

## Workflow

Numbered steps for performing the task.

## Validation

Checks required before declaring completion.

## Troubleshooting

Common failures and corrective actions.

## References

Links to bundled supporting material.
```

Not every skill needs every section. Include only sections that improve execution.

## Workflow Authoring Rules

A strong workflow should:

* Use numbered steps
* Begin by grounding the target and required inputs
* Identify prerequisites before write operations
* Separate read, plan, execute, and verify stages
* Define safe handling for destructive actions
* Explain when user confirmation is required
* Include expected outputs
* Include failure and recovery behavior
* End with explicit completion checks

Avoid instructions that:

* Tell the agent to pretend a tool exists
* Depend on hidden model behavior
* Require unsupported background work
* Skip verification
* Repeat the same rule in multiple sections
* Mix several independent workflows without routing logic

## Optional Bundled Directories

Add optional directories only when they support the skill’s execution.

| Folder        | Purpose                                                  | Use When                                                            |
| ------------- | -------------------------------------------------------- | ------------------------------------------------------------------- |
| `scripts/`    | Executable Python, Bash, JavaScript, or other automation | The workflow benefits from repeatable code execution                |
| `references/` | Documentation the agent reads when needed                | Detailed APIs, schemas, policies, or long-form guides are required  |
| `assets/`     | Static files used without modification                   | The skill needs images, fonts, diagrams, or fixed resources         |
| `templates/`  | Starter files the agent modifies                         | The workflow produces code, documents, configurations, or scaffolds |

### Complete Example Structure

```text
my-awesome-skill/
├── SKILL.md
├── LICENSE.txt
├── scripts/
│   └── helper.py
├── references/
│   ├── api-reference.md
│   └── examples.md
├── assets/
│   └── diagram.png
└── templates/
    └── starter.ts
```

## Bundled Resource Rules

### Scripts

Place executable automation in `scripts/`.

Scripts should:

* Have a clear entry point
* Validate inputs
* Return useful errors
* Avoid embedded secrets
* Use relative paths when possible
* Include comments only where they improve maintenance
* Be referenced from `SKILL.md`
* Be tested before the skill is considered complete

### References

Place detailed documentation in `references/`.

Use references for:

* API documentation
* Schemas
* Policies
* Long examples
* Tool-specific procedures
* Platform limitations
* Extended troubleshooting

The main skill should identify exactly when each reference should be read.

### Assets

Place static files in `assets/`.

Use assets for resources consumed as-is, such as:

* Images
* Diagrams
* Fonts
* Icons
* Fixed data files

Do not place editable starter code in `assets/`.

### Templates

Place editable starter files in `templates/`.

Use templates for:

* Application scaffolds
* Configuration files
* Document layouts
* Reusable code structures
* Starter prompts
* Example manifests

Clearly state which values the agent must replace.

## Parent and Child Skill Architecture

Use a parent router when a functional category contains several independently triggered skills.

Example:

```text
design/
├── SKILL.md
├── audit-interface/
│   └── SKILL.md
├── create-prototype/
│   └── SKILL.md
└── implement-design/
    └── SKILL.md
```

The parent skill should:

* Explain the category
* Route requests to the correct child
* Distinguish overlapping triggers
* Define shared constraints
* Reference child paths
* Avoid duplicating complete child workflows

Each child skill should:

* Solve one functional job
* Have a precise trigger description
* Define prerequisites
* Include its own execution workflow
* Include completion checks
* Avoid repeating the parent skill

Keep the hierarchy shallow unless deeper nesting is clearly necessary.

## Duplicating This Template

To use this skill as a starting point:

1. Copy the complete `make-skill-template/` folder.
2. Rename the copied folder using a lowercase, hyphenated skill name.
3. Open the copied `SKILL.md`.
4. Change the frontmatter `name` to match the folder.
5. Replace the description with a keyword-rich discovery description.
6. Replace the body with instructions for the new capability.
7. Remove template sections the new skill does not need.
8. Add bundled directories only when required.
9. Update all relative paths.
10. Run validation.

Do not leave template examples or placeholder content in the completed skill.

## Converting Existing Instructions Into a Skill

When the user supplies notes, documentation, or a task prompt:

1. Identify the functional job.
2. Extract trigger phrases and use cases.
3. Identify prerequisites and required tools.
4. Separate instructions from examples and background information.
5. Convert procedures into an ordered workflow.
6. Move long supporting content into references when appropriate.
7. Add validation and failure-handling requirements.
8. Write discovery-oriented frontmatter.
9. Check for application-specific assumptions.
10. Remove duplicated or contradictory instructions.
11. Validate the resulting folder and `SKILL.md`.

Preserve the user’s intended behavior, but do not preserve accidental ambiguity or poor organization.

## Refining an Existing Skill

When improving an existing skill, evaluate:

* Whether the description triggers correctly
* Whether the skill has one clear purpose
* Whether it overlaps another skill
* Whether it is too large and should be split
* Whether small related skills should be merged
* Whether instructions depend on an unavailable tool
* Whether references are stale or broken
* Whether supporting files are actually used
* Whether the workflow includes verification
* Whether the skill contains model-specific assumptions
* Whether its folder and frontmatter names match

Do not split solely because a skill is long. Split when separate sections have independent triggers or outcomes.

Do not merge solely because two skills share an application. Merge only when they represent the same natural job or workflow.

## Validation

Run the repository validation command when available:

```bash
npm run skill:validate
```

If the repository uses a different command, discover and use the project’s documented validator.

Do not claim validation succeeded unless the validator was actually executed.

## Validation Checklist

Confirm all of the following:

* [ ] Folder name uses lowercase letters, numbers, and hyphens
* [ ] Folder name contains no consecutive hyphens
* [ ] Frontmatter `name` exactly matches the folder name
* [ ] `name` is between 1 and 64 characters
* [ ] `description` is between 1 and 1024 characters
* [ ] `description` explains what the skill does
* [ ] `description` explains when the skill should be used
* [ ] `description` contains useful discovery keywords
* [ ] Description is wrapped in single quotes
* [ ] YAML frontmatter parses correctly
* [ ] Body instructions are clear and actionable
* [ ] The main body remains under 500 lines when practical
* [ ] Large supporting details are moved into references
* [ ] Bundled files are referenced using valid relative paths
* [ ] Bundled assets are under 5 MB each unless the environment explicitly permits larger files
* [ ] Scripts contain no embedded secrets
* [ ] Templates contain no unmarked production credentials
* [ ] Optional folders exist only when used
* [ ] Trigger boundaries do not substantially overlap another skill
* [ ] The workflow includes completion checks
* [ ] The skill does not claim unsupported tools or permissions
* [ ] Validation completes successfully, or failures are documented

## Troubleshooting

### Skill Is Not Discovered

Possible causes:

* Description is too vague
* Trigger keywords are missing
* Description explains only the subject, not the use case
* Another skill has a broader overlapping description
* Folder name and frontmatter name do not match
* The skill directory is outside the configured discovery path

Resolution:

1. Add concrete capabilities to the description.
2. Add realistic user trigger language.
3. Include relevant applications, scenarios, and file types.
4. Narrow overlapping skill descriptions.
5. Confirm the skill is located in the correct directory.
6. Re-run validation or indexing.

### Validation Fails on the Name

Possible causes:

* Uppercase letters
* Spaces or underscores
* Consecutive hyphens
* Folder and frontmatter names differ
* Leading or trailing hyphen
* Name exceeds the permitted length

Resolution:

Rename the folder and update the frontmatter so they match exactly.

### Description Is Rejected

Possible causes:

* Description is too short
* Description exceeds the maximum length
* YAML quoting is invalid
* Description omits trigger scenarios

Resolution:

Rewrite it as one single-quoted string explaining both what the skill does and when it should activate.

### Bundled Resource Cannot Be Found

Possible causes:

* Incorrect relative path
* File was renamed
* Path is relative to the wrong working directory
* Filename case differs
* Resource was excluded from the repository

Resolution:

Reference files relative to the skill root and confirm the path exists using the exact filename and case.

### Skill Has Become Too Large

Possible causes:

* Multiple independent workflows are combined
* Extensive documentation is embedded in the main file
* Examples repeat the instructions
* Application-specific variants are mixed together

Resolution:

* Move detailed documentation to `references/`
* Move executable logic to `scripts/`
* Split independent jobs into child skills
* Add a parent router when several related child skills remain

### Two Skills Trigger on the Same Requests

Resolution:

1. Compare their expected outcomes.
2. Merge them if they perform the same job.
3. Narrow their descriptions if their jobs are distinct.
4. Add explicit “use when” and “do not use when” boundaries.
5. Ensure the parent router explains the difference.

## Completion Requirements

A newly created or revised skill is complete only when:

* The folder structure is valid
* The frontmatter is valid
* The name matches the folder
* The description supports reliable discovery
* The workflow is executable
* Required bundled resources exist
* Relative references resolve
* Completion checks are defined
* Validation passes or failures are clearly reported
* No template placeholders remain

## References

* Agent Skills specification: https://agentskills.io/specification
