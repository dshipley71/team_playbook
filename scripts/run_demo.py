from __future__ import annotations

import json
from pathlib import Path

from team_playbook.orchestrator import WorkflowOrchestrator


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    orchestrator = WorkflowOrchestrator(repo_root)
    result = orchestrator.run(
        workflow_name="feature_delivery",
        task="Create a new internal team playbook workflow and release summary",
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
