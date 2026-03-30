from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
from typing import Dict, List

from .mcp import MockMCPServer
from .models import AgentResult, Handoff, Workflow
from .registry import AgentFactory, ConfigRegistry


class WorkflowOrchestrator:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.registry = ConfigRegistry(root)
        self.tool_server = MockMCPServer()
        self.agent_factory = AgentFactory(self.tool_server)

    def _get_workflow(self, workflow_name: str) -> Workflow:
        workflows = self.registry.load_workflows()
        for workflow in workflows:
            if workflow.name == workflow_name:
                return workflow
        available = ", ".join(item.name for item in workflows)
        raise ValueError(f"Workflow '{workflow_name}' not found. Available: {available}")

    def run(self, workflow_name: str, task: str) -> Dict[str, object]:
        workflow = self._get_workflow(workflow_name)
        agents = self.agent_factory.build(self.registry.load_agents())
        handoff = Handoff(task=task, objective="")
        results: List[AgentResult] = []

        for agent_name in workflow.sequence:
            agent = agents[agent_name]
            result = agent.run(handoff)
            results.append(result)
            handoff = result.handoff

        return {
            "workflow": asdict(workflow),
            "results": [
                {
                    "agent_name": result.agent_name,
                    "summary": result.summary,
                    "handoff": asdict(result.handoff),
                }
                for result in results
            ],
            "tool_snapshot": self.tool_server.snapshot(),
            "final_handoff": asdict(handoff),
        }
