from fastq import Task
from typing import Optional
from abc import ABC, abstractmethod

class BaseBroker(ABC):

    @abstractmethod
    async def enqueue(self, task: Task) -> str:
        pass

    @abstractmethod
    async def dequeue(self) -> Optional[Task]:
        pass

    @abstractmethod
    async def save_result(self) -> None:
        pass


    @abstractmethod
    async def get_result(self, task_id: str) -> Optional[Task]:
        pass
