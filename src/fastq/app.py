

from typing import Callable
from fastq.core.registry import Registry
from fastq.brokers.memory import MemoryBroker


class FastQ:
    """
    FastQ application
    """
    def __init__(self, broker: MemoryBroker):
        self.registry = Registry()
        self.broker = broker


    def task(self, func: Callable) -> Callable:
        """
        Decorator to register a function as a task

        Usage:
            @fastq.task
            async def process_image(image_path: str):
                # Your code here
                pass
        The function is registered in the app's registry with its __name__ as the key and the function as the value, can be called using the task name.
        """
        
        return self.registry.register(func)
    
    def register_task(self, func: Callable) -> None:
        """
        Register a task in the app's registry

        Usage:
            fastq.register_task(task)
        The task is registered in the app's registry with its __name__ as the key and the function as the value, can be called using the task name.
        """
        self.registry.register(func)