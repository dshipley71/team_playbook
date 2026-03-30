from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class Skill:
    name: str
    description: str


@dataclass
class AgentConfig:
    name: str
    role: str
    skills: List[str]


@dataclass
class Workflow:
    name: str
    description: str
    sequence: List[str]


@dataclass
class Handoff:
    task: str
    objective: str
    constraints: List[str] = field(default_factory=list)
    decisions: List[str] = field(default_factory=list)
    artifacts: List[str] = field(default_factory=list)
    risks: List[str] = field(default_factory=list)
    next_action: str = ""
    notes: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AgentResult:
    agent_name: str
    summary: str
    handoff: Handoff
