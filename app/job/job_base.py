from abc import ABC, abstractmethod
from datetime import datetime

class Job(ABC):
    """Base class for scheduled jobs."""

    name: str = "UnnamedJob"
    cron: dict = {}

    @abstractmethod
    def should_run(self, now: datetime) -> bool:
        """Return True if the job should run at the given time."""
        ...

    @abstractmethod
    def run(self) -> None:
        """Execute the job logic."""
        ...
