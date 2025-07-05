from datetime import datetime
from app.job.job_base import Job

class SyncProductJob(Job):
    """Job to synchronize product information hourly."""

    name = "sync_product"
    cron = {"minute": 0}

    def should_run(self, now: datetime) -> bool:
        return now.minute == 0

    def run(self):
        print(f"[{self.name}] Syncing product info...")
