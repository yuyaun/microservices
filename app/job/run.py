from datetime import datetime
from app.job.registry import load_jobs
from app.core.logger import logger

def main():
    now = datetime.now()
    logger.info(f"[JobRunner] {now} Running scheduled jobs...")
    for job in load_jobs():
        if job.should_run(now):
            try:
                logger.info(f"Running job: {job.name}")
                job.run()
            except Exception as e:
                logger.error(f"Error in {job.name}: {e}")

if __name__ == "__main__":
    main()