"""
Task model and registry for FastQ
"""

from enum import Enum
from typing import Any
from datetime import datetime
from dataclasses import dataclass, field
from fastq.utils import generate_uuid_str, datetime_now


class TaskStatus(str, Enum):
    """Task exception status"""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class Task:
    """
    Represents a task in the queue.
    Attributes:
        id: Unique task identifier
        name: Name of the task function
        status: Current execution status
        created_at: When task was created
        started_at: When task execution began
        completed_at: When task execution finished
        result: Task result (if completed)
        error: Error message (if failed)
        retry_count: Number of retry attempts
    """

    id: str = field(default_factory=lambda: generate_uuid_str())
    name: str = ""
    status: TaskStatus = TaskStatus.PENDING
    created_at: datetime = field(default_factory=lambda: datetime_now())
    started_at: datetime | None = None
    completed_at: datetime | None = None
    result: Any | None = None
    error: str | None = None
    retry_count: int = 0

    @property
    def is_finished(self) -> bool:
        """Check if task is in a terminal state"""
        return self.status in [
            TaskStatus.COMPLETED,
            TaskStatus.FAILED,
            TaskStatus.CANCELLED,
        ]

    def to_dict(self) -> dict:
        """Serialize task to dictionary"""
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat()
            if self.completed_at
            else None,
            "result": self.result,
            "error": self.error,
            "retry_count": self.retry_count,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Deserialize task from dictionary"""
        return cls(
            id=data["id"],
            name=data["name"],
            status=TaskStatus(data["status"]),
            created_at=datetime.fromisoformat(data["created_at"]),
            started_at=datetime.fromisoformat(data["started_at"])
            if data["started_at"]
            else None,
            completed_at=datetime.fromisoformat(data["completed_at"])
            if data["completed_at"]
            else None,
            result=data["result"],
            error=data["error"],
            retry_count=data["retry_count"],
        )
