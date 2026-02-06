from typing import Callable
from .core.registry import TaskRegistry


class FastQ:
    def __init__(self):
        self.registry = TaskRegistry()
        self.backend = None

    def task(
        self,
        func=None,
        *,
        name: str = "",
        timeout: float = 10,
        max_retries: int = 3,
        retry_delay: float = 5.0,
        retry_backoff: float = 2.0,
    ):
        def decorator(f):
            return self.registry.register(
                f,
                name=name,
                timeout=timeout,
                max_retries=max_retries,
                retry_delay=retry_delay,
                retry_backoff=retry_backoff,
            )
        if func:
            return decorator(func)
        return decorator
