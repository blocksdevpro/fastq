

from typing import Optional
import asyncio
from fastq import Task
from typing import Dict


class MemoryBroker():
    """
    In-memory broker for testing purposes
    """
    def __init__(self):
        self.queue: asyncio.Queue[str] = asyncio.Queue()
        self.tasks: Dict[str, Task] = {}

    async def enqueue(self, task: Task) -> str:
        """
        Enqueue a task to the broker

        Args:
            task: Task to enqueue
        """
        await self.queue.put(task.id)
        self.tasks[task.id] = task
        return task.id

    async def dequeue(self) -> Optional[Task]:
        """
        Dequeue a task from the broker

        Returns:
            Task: Dequeued task
        """
        task_id = await self.queue.get()
        return self.tasks.get(task_id)