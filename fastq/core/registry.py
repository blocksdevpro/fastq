import inspect
from typing import Callable
from dataclasses import dataclass

@dataclass
class TaskDef:
    name: str
    func: Callable
    timeout: float
    max_retries: int
    retry_delay: float
    retry_backoff: float

    @property
    def is_async(self):
        return inspect.iscoroutinefunction(self.func)


class TaskRegistry:
    def __init__(self):
        self._tasks: dict[str, TaskDef] = {}

    def register(
        self,
        func: Callable,
        name: str = "",
        timeout: float = 10,
        max_retries: int = 3,
        retry_delay: float = 5.0,
        retry_backoff: float = 2.0,
    ):
        task_name = name or func.__name__
        self._tasks[task_name] = TaskDef(
            name=task_name,
            func=func,
            timeout=timeout,
            max_retries=max_retries,
            retry_delay=retry_delay,
            retry_backoff=retry_backoff,
        )
        return func

    def get(self, name: str) -> TaskDef:
        if name not in self._tasks:
            raise KeyError(f"Task not registered: {name}")
        return self._tasks[name]
    
    def all(self) -> dict[str, TaskDef]:
        return dict(self._tasks)
        