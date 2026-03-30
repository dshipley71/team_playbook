from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

from .agents import BuilderAgent, IntakeAgent, PlannerAgent, ReleaseAgent, ReviewerAgent
from .mcp import MockMCPServer
from .models import AgentConfig, Skill, Workflow


class ConfigRegistry:
    def __init__(self, root: Path) -> None:
        self.root = root

    def _load_json(self, relative_path: str) -> dict:
        path = self.root / relative_path
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)

    def load_agents(self) -> List[AgentConfig]:
        payload = self._load_json("config/agents.json")
        return [AgentConfig(**item) for item in payload["agents"]]

    def load_skills(self) -> List[Skill]:
        payload = self._load_json("config/skills.json")
        return [Skill(**item) for item in payload["skills"]]

    def load_workflows(self) -> List[Workflow]:
        payload = self._load_json("config/workflows.json")
        return [Workflow(**item) for item in payload["workflows"]]


class AgentFactory:
    def __init__(self, tool_server: MockMCPServer) -> None:
        self.tool_server = tool_server

    def build(self, configs: List[AgentConfig]) -> Dict[str, object]:
        mapping = {}
        for config in configs:
            if config.name == "IntakeAgent":
                mapping[config.name] = IntakeAgent(config, self.tool_server)
            elif config.name == "PlannerAgent":
                mapping[config.name] = PlannerAgent(config, self.tool_server)
            elif config.name == "BuilderAgent":
                mapping[config.name] = BuilderAgent(config, self.tool_server)
            elif config.name == "ReviewerAgent":
                mapping[config.name] = ReviewerAgent(config, self.tool_server)
            elif config.name == "ReleaseAgent":
                mapping[config.name] = ReleaseAgent(config, self.tool_server)
            else:
                raise ValueError(f"Unknown agent config: {config.name}")
        return mapping
