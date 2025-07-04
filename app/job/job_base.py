from abc import ABC, abstractmethod
from datetime import datetime

class Job(ABC):
    name: str = "UnnamedJob"

    @abstractmethod
    def should_run(self, now: datetime) -> bool:
        ...

    @abstractmethod
    def run(self):
        ...