"""FastQ is a Python library for building distributed task queues."""

__version__ = "0.1.0"

from .core.task import Task
from .core.registry import task, get_task, clear_registry
from .exceptions import FastQTaskNotFoundException

__all__ = ["Task", "task", "get_task", "clear_registry", "FastQTaskNotFoundException"]
