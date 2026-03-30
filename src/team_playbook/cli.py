from __future__ import annotations

import argparse
import json
from pathlib import Path

from .orchestrator import WorkflowOrchestrator


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a team playbook workflow.")
    parser.add_argument("--workflow", required=True, help="Workflow name to run.")
    parser.add_argument("--task", required=True, help="Task description.")
    parser.add_argument(
        "--root",
        default=str(Path(__file__).resolve().parents[2]),
        help="Repository root containing config/.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    orchestrator = WorkflowOrchestrator(Path(args.root))
    output = orchestrator.run(workflow_name=args.workflow, task=args.task)
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
