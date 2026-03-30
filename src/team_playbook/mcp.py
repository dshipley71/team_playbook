from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, List


@dataclass
class MockMCPServer:
    """A tiny local MCP-style tool host for demo purposes."""

    notes: Dict[str, str] = field(default_factory=dict)
    log_entries: List[str] = field(default_factory=list)

    def _timestamp(self) -> str:
        return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    def log(self, message: str) -> str:
        entry = f"[{self._timestamp()}] {message}"
        self.log_entries.append(entry)
        return entry

    def write_note(self, key: str, content: str) -> None:
        self.notes[key] = content
        self.log(f"note_written key={key}")

    def read_note(self, key: str) -> str:
        value = self.notes.get(key, "")
        self.log(f"note_read key={key} found={bool(value)}")
        return value

    def snapshot(self) -> Dict[str, object]:
        return {
            "notes": dict(self.notes),
            "log_entries": list(self.log_entries),
        }
