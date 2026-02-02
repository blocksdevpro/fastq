import inspect
from typing import Callable, Dict, List
from fastq.exceptions import FastQTaskNotFoundException



class Registry:
    """
    Registry for storing and retrieving registered tasks.
    """
    def __init__(self):
        self.tasks: Dict[str, Callable] = {}

    def register(self, func: Callable) -> Callable:
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
        self.tasks[func.__name__] = func
        return func

    def get_task(self, task_name: str) -> Callable:
        """
        Get a registered task by name

        Args:
            task_name: Name of the task

        Returns:
            Callable: The task function

        Raises:
            FastQTaskNotFoundException: If the task is not found

        """
        if task_name not in self.tasks:
            raise FastQTaskNotFoundException(f"Task {task_name} not found")
        return self.tasks[task_name]

    def list_tasks(self) -> List[str]:
        """
        Get list of all registered tasks

        Returns:
            List[str]: List of task names
        """
        return list(self.tasks.keys())

    def clear_registry(self):
        """
        Clear the registrered tasks from the registry (useful for testing)
        """
        self.tasks.clear()