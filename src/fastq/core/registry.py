import inspect
from typing import Callable, Dict, List
from fastq.exceptions import FastQTaskNotFoundException


# Global registry: task_name -> function
TASK_REGISTRY: Dict[str, Callable] = {}


def task(func: Callable) -> Callable:
    """
    Decorator to register a function as a task

    Usage:
        @fastq.task
        async def process_image(image_path: str):
            # Your code here
            pass
    The function is registered in the global registry with its __name__ as the key and the function as the value, can be called using the task name.
    """

    if not inspect.iscoroutinefunction(func):
        # TODO: implement sync task
        raise ValueError("Task function must be a coroutine function")

    # Register the function in the global registry
    TASK_REGISTRY[func.__name__] = func
    return func


def get_task(task_name: str) -> Callable:
    """
    Get a registered task by name

    Args:
        task_name: Name of the task

    Returns:
        Callable: The task function

    Raises:
        FastQTaskNotFoundException: If the task is not found

    """
    if task_name not in TASK_REGISTRY:
        raise FastQTaskNotFoundException(f"Task {task_name} not found")
    return TASK_REGISTRY[task_name]


def list_tasks() -> List[str]:
    """
    Get list of all registered tasks

    Returns:
        List[str]: List of task names
    """
    return list(TASK_REGISTRY.keys())


def clear_registry():
    """
    Clear the registrered tasks from the registry (useful for testing)
    """
    TASK_REGISTRY.clear()
