# CLAUDE.md

## Purpose

This file defines implementation discipline for the team. It is the operational rulebook for how work should be carried out inside the repository.

It exists to prevent drift, unnecessary complexity, and low-quality handoffs.

---

## Working Principles

### 1. Be explicit
- State assumptions.
- State scope.
- State intended outputs.

### 2. Keep changes bounded
- Make the smallest set of changes needed.
- Do not rewrite unrelated areas.
- Do not introduce abstractions that are not needed yet.

### 3. Preserve intent
- Every output should remain aligned to the original objective.
- If scope changes, document the reason.

### 4. Write for handoff
- A teammate should understand the output without guessing.
- Summaries must be concrete and readable.

### 5. Validate before release
- Check that implementation matches plan.
- Check that review comments are addressed.
- Check that release notes match reality.

---

## Project Setup Rules

When starting a new project:

1. Create the repository structure.
2. Define `AGENTS.md`.
3. Define `CLAUDE.md`.
4. Define `SKILLS.md`.
5. Define workflows.
6. Define configuration files.
7. Add a runnable entry point.
8. Add at least one demo workflow.

A project is not considered operational until all eight are present.

---

## File Creation Rules

When creating files:

- use descriptive names,
- keep responsibilities separated,
- avoid mixing policy files with runtime logic,
- keep docs readable by humans,
- keep config machine-readable.

---

## Implementation Rules

### For code
- prefer simple, readable functions,
- use dataclasses for shared structured models,
- log major workflow steps,
- keep side effects localized,
- return structured results.

### For documentation
- explain purpose first,
- then process,
- then examples,
- then failure modes,
- then maintenance guidance.

### For configuration
- centralize config,
- avoid hidden magic values,
- keep names consistent with docs,
- keep workflow and role names aligned across files.

---

## Review Rules

Before calling work complete, verify:

- the request was understood correctly,
- the selected workflow was appropriate,
- the produced artifacts match the plan,
- the naming is consistent,
- the handoff is complete,
- the release summary is understandable.

If any of the above fails, mark the task as rework.

---

## Prompting Rules for Team Members

When using AI tools for project work:

- define the role,
- define the objective,
- define the required output format,
- define constraints,
- require assumptions to be explicit,
- require examples when teaching,
- require summaries for handoff.

Good prompts reduce ambiguity before implementation begins.

---

## Change Management Rules

When modifying this repo:

1. update the relevant docs,
2. update the related config,
3. update runtime code if the workflow changed,
4. run the demo path,
5. confirm the docs and runtime still match.

No operational rule should live only in code.
No workflow definition should live only in prose.

---

## Team Standard for “Clear as Day” Outputs

A deliverable is “clear as day” when:

- the reader understands the goal immediately,
- the steps are in the right order,
- the files and roles line up cleanly,
- there are no hidden assumptions,
- next steps are obvious.
