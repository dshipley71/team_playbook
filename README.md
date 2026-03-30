# Team Playbook Repo

This repository is a self-contained team playbook and working Python scaffold for running AI development projects with:

- `AGENTS.md` for team and agent operating rules
- `CLAUDE.md` for implementation discipline and guardrails
- `SKILLS.md` for reusable capabilities
- workflow definitions for planning, building, reviewing, and releasing
- a lightweight orchestrator that runs agents against a task
- local mock MCP-style tools so the system works without external services

## What this repo is

This repo is designed to help a new AI development team:

1. understand how responsibilities are divided,
2. follow a repeatable operating model,
3. run a small end-to-end workflow locally,
4. extend the system as the project grows.

## Repository layout

```text
team_playbook_repo/
├── AGENTS.md
├── CLAUDE.md
├── SKILLS.md
├── README.md
├── pyproject.toml
├── config/
│   ├── agents.json
│   ├── skills.json
│   └── workflows.json
├── docs/
│   └── TEAM_WORKFLOWS.md
├── scripts/
│   └── run_demo.py
└── src/
    └── team_playbook/
        ├── __init__.py
        ├── agents.py
        ├── cli.py
        ├── mcp.py
        ├── models.py
        ├── orchestrator.py
        └── registry.py
```

## Quick start

### 1) Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Install the package in editable mode

```bash
pip install -e .
```

### 3) Run the demo workflow

```bash
python scripts/run_demo.py
```

or

```bash
python -m team_playbook.cli --workflow feature_delivery --task "Build a document ingestion feature with validation and release notes"
```

## What the demo does

The demo loads the defined agents, skills, and workflows from the config files, then runs a task through this sequence:

1. IntakeAgent
2. PlannerAgent
3. BuilderAgent
4. ReviewerAgent
5. ReleaseAgent

Each agent uses local mock MCP-style tools to:

- log actions,
- read/write notes,
- produce a simple structured result.

This is intentionally lightweight so the repo runs out of the box.

## How to adapt it

- Update `AGENTS.md` when team roles or responsibilities change.
- Update `CLAUDE.md` when implementation rules or review discipline need to change.
- Update `SKILLS.md` when the team adds reusable capabilities.
- Update `config/workflows.json` to add project-specific delivery flows.
- Replace mock MCP tools in `src/team_playbook/mcp.py` with real service integrations when ready.

## Recommended team usage

Use this repo in three layers:

### Layer 1: Governance

- `AGENTS.md`
- `CLAUDE.md`
- `SKILLS.md`

These define how the team works.

### Layer 2: Execution

- workflow definitions
- orchestrator
- agents
- skills

These define how tasks move through the system.

### Layer 3: Tooling

- local MCP-style tools
- future real integrations

These define how the system acts on the environment.

## Success criteria for a team using this repo

A task is considered well-executed when:

- the correct workflow is selected,
- each agent performs its defined role,
- outputs are handed off in a predictable structure,
- review happens before release,
- release artifacts summarize what was built and why.

## Next extension ideas

- add persistent storage,
- add real tool integrations,
- add test execution and gating,
- add richer prompt templates,
- add role-based workflow variants,
- add CI checks to verify config consistency.
