from __future__ import annotations

from typing import List

from .mcp import MockMCPServer
from .models import AgentConfig, AgentResult, Handoff


class BaseAgent:
    def __init__(self, config: AgentConfig, tool_server: MockMCPServer) -> None:
        self.config = config
        self.tool_server = tool_server

    @property
    def name(self) -> str:
        return self.config.name

    def run(self, handoff: Handoff) -> AgentResult:
        raise NotImplementedError


class IntakeAgent(BaseAgent):
    def run(self, handoff: Handoff) -> AgentResult:
        self.tool_server.log(f"{self.name} started")
        structured = Handoff(
            task=handoff.task,
            objective=f"Deliver requested outcome for task: {handoff.task}",
            constraints=["Keep outputs aligned with repository rules."],
            decisions=["Use structured five-stage workflow."],
            artifacts=["intake_summary"],
            risks=["Original request may omit hidden assumptions."],
            next_action="Create a concrete implementation plan.",
            notes={"intake": f"Structured request for: {handoff.task}"},
        )
        self.tool_server.write_note("intake_summary", structured.notes["intake"])
        return AgentResult(
            agent_name=self.name,
            summary="Structured incoming request into a standard handoff package.",
            handoff=structured,
        )


class PlannerAgent(BaseAgent):
    def run(self, handoff: Handoff) -> AgentResult:
        self.tool_server.log(f"{self.name} started")
        plan_steps: List[str] = [
            "clarify scope",
            "identify affected files",
            "implement changes",
            "review quality",
            "package release",
        ]
        planned = Handoff(
            task=handoff.task,
            objective=handoff.objective,
            constraints=handoff.constraints + ["Follow ordered workflow steps."],
            decisions=handoff.decisions + [f"Plan steps: {', '.join(plan_steps)}"],
            artifacts=handoff.artifacts + ["implementation_plan"],
            risks=handoff.risks + ["Implementation may drift if the plan is ignored."],
            next_action="Execute the implementation plan.",
            notes={
                **handoff.notes,
                "plan": " -> ".join(plan_steps),
            },
        )
        self.tool_server.write_note("implementation_plan", planned.notes["plan"])
        return AgentResult(
            agent_name=self.name,
            summary="Created an ordered implementation plan.",
            handoff=planned,
        )


class BuilderAgent(BaseAgent):
    def run(self, handoff: Handoff) -> AgentResult:
        self.tool_server.log(f"{self.name} started")
        build_summary = (
            f"Implemented task '{handoff.task}' using plan: "
            f"{handoff.notes.get('plan', 'no plan recorded')}"
        )
        built = Handoff(
            task=handoff.task,
            objective=handoff.objective,
            constraints=handoff.constraints,
            decisions=handoff.decisions + ["Kept implementation scoped to plan."],
            artifacts=handoff.artifacts + ["build_output"],
            risks=handoff.risks,
            next_action="Review the produced artifacts for correctness and readiness.",
            notes={
                **handoff.notes,
                "build": build_summary,
            },
        )
        self.tool_server.write_note("build_output", build_summary)
        return AgentResult(
            agent_name=self.name,
            summary="Produced a scoped implementation summary.",
            handoff=built,
        )


class ReviewerAgent(BaseAgent):
    def run(self, handoff: Handoff) -> AgentResult:
        self.tool_server.log(f"{self.name} started")
        review_status = "approved"
        review_note = "Artifacts are aligned with plan and ready for release."
        reviewed = Handoff(
            task=handoff.task,
            objective=handoff.objective,
            constraints=handoff.constraints,
            decisions=handoff.decisions + [f"Review status: {review_status}"],
            artifacts=handoff.artifacts + ["review_report"],
            risks=handoff.risks,
            next_action=(
                "Package release notes and final handoff."
                if review_status == "approved"
                else "Return task for rework."
            ),
            notes={
                **handoff.notes,
                "review": review_note,
                "review_status": review_status,
            },
        )
        self.tool_server.write_note("review_report", review_note)
        return AgentResult(
            agent_name=self.name,
            summary=f"Completed review with status: {review_status}.",
            handoff=reviewed,
        )


class ReleaseAgent(BaseAgent):
    def run(self, handoff: Handoff) -> AgentResult:
        self.tool_server.log(f"{self.name} started")
        release_note = (
            f"Released task '{handoff.task}'. "
            f"Summary: {handoff.notes.get('build', 'No build summary available.')}"
        )
        released = Handoff(
            task=handoff.task,
            objective=handoff.objective,
            constraints=handoff.constraints,
            decisions=handoff.decisions + ["Prepared final release package."],
            artifacts=handoff.artifacts + ["release_notes"],
            risks=handoff.risks,
            next_action="Share final handoff with downstream team.",
            notes={
                **handoff.notes,
                "release": release_note,
            },
        )
        self.tool_server.write_note("release_notes", release_note)
        return AgentResult(
            agent_name=self.name,
            summary="Prepared release notes and final handoff.",
            handoff=released,
        )
