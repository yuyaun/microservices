from app.job.job_base import Job

class CleanupOrderJob(Job):
    name = "cleanup_order"

    def run(self) -> None:
        print(f"[{self.name}] Cleaning expired orders...")


if __name__ == "__main__":
    CleanupOrderJob().run()
