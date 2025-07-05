from app.job.job_base import Job

class SyncProductJob(Job):
    name = "sync_product"

    def run(self) -> None:
        print(f"[{self.name}] Syncing product info...")


if __name__ == "__main__":
    SyncProductJob().run()
