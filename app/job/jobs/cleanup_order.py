from datetime import datetime
from app.job.job_base import Job

class CleanupOrderJob(Job):
    name = "cleanup_order"

    def should_run(self, now: datetime) -> bool:
        return now.hour == 1 and now.minute == 0

    def run(self):
        print(f"[{self.name}] Cleaning expired orders...")