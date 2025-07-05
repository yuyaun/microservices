from datetime import datetime
from app.job.job_base import Job

class CleanupOrderJob(Job):
    """Job to clean expired orders each day."""

    name = "cleanup_order"
    cron = {"hour": 1, "minute": 0}

    def should_run(self, now: datetime) -> bool:
        return now.hour == 1 and now.minute == 0

    def run(self):
        print(f"[{self.name}] Cleaning expired orders...")
