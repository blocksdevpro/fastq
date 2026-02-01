"""FastQ is a Python library for building distributed task queues."""

__version__ = "0.1.0"

from .core.task import Task
from .core.registry import task, get_task, clear_registry, list_tasks
from .exceptions import FastQTaskNotFoundException

__all__ = [
    "Task",
    "task",
    "get_task",
    "list_tasks",
    "clear_registry",
    "FastQTaskNotFoundException",
]
