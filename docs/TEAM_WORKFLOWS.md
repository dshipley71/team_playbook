# Team Workflows

## 1. Standard Feature Delivery

### Goal
Take a request from intake through release with review gating.

### Sequence
1. IntakeAgent structures the task.
2. PlannerAgent creates the plan.
3. BuilderAgent creates the deliverable.
4. ReviewerAgent verifies quality.
5. ReleaseAgent packages the result.

### Entry criteria
- a request exists,
- a workflow has been selected,
- required skills are available.

### Exit criteria
- deliverables exist,
- review is approved,
- release notes are ready.

---

## 2. Documentation Update Workflow

### Goal
Update docs while keeping rules, config, and runtime aligned.

### Sequence
1. IntakeAgent defines what changed.
2. PlannerAgent identifies affected files.
3. BuilderAgent updates documentation and config.
4. ReviewerAgent checks alignment.
5. ReleaseAgent summarizes the update.

---

## 3. Exploratory Design Workflow

### Goal
Explore an idea without committing to full release packaging.

### Sequence
1. IntakeAgent captures the problem.
2. PlannerAgent outlines options.
3. BuilderAgent produces a draft design.
4. ReviewerAgent evaluates feasibility.

### Notes
This workflow can stop after review if the team only needs a design recommendation.
