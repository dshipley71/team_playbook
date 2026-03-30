# SKILLS.md

## Purpose

This file defines reusable capabilities the team can apply across workflows.
A skill is a repeatable capability, not a job title.

Skills allow the team to separate **what must be done** from **who happens to do it**.

---

## Skill Catalog

### 1. requirements_structuring
**Description:** Convert messy requests into structured objectives, constraints, and acceptance criteria.

**Used by:** IntakeAgent, PlannerAgent

**Outputs:**
- structured request,
- acceptance criteria,
- open questions.

---

### 2. workflow_planning
**Description:** Break work into ordered steps with checkpoints and risks.

**Used by:** PlannerAgent

**Outputs:**
- plan,
- work breakdown,
- checkpoint list.

---

### 3. implementation_execution
**Description:** Create or modify project artifacts according to an approved plan.

**Used by:** BuilderAgent

**Outputs:**
- changed artifacts,
- implementation notes,
- summary of work.

---

### 4. quality_review
**Description:** Evaluate outputs for correctness, clarity, scope control, and maintainability.

**Used by:** ReviewerAgent

**Outputs:**
- findings,
- approval status,
- rework guidance.

---

### 5. release_packaging
**Description:** Prepare a clean handoff package and release notes for downstream use.

**Used by:** ReleaseAgent

**Outputs:**
- release notes,
- handoff summary,
- risk note.

---

### 6. documentation_authoring
**Description:** Write human-readable documentation that matches the runtime system.

**Used by:** all agents as needed

**Outputs:**
- docs,
- examples,
- workflow guides.

---

### 7. configuration_alignment
**Description:** Keep documentation, workflow config, and runtime naming synchronized.

**Used by:** PlannerAgent, BuilderAgent, ReviewerAgent

**Outputs:**
- aligned names,
- consistent config,
- reduced drift.

---

## Skill Usage Rules

1. Skills should be reusable.
2. Skills should produce observable outputs.
3. Skills should be named by capability, not by person.
4. Skills should be referenced consistently in workflows and code.

---

## Skill Expansion Guidance

Add a new skill when:

- a capability appears in multiple workflows,
- the team needs shared terminology,
- it improves handoff clarity,
- it prevents duplicated instructions.

Do not add a skill just because a task is unique.
Only add skills that the team expects to use repeatedly.
