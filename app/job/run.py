from app.job.registry import load_jobs
from app.core.logger import logger

def main():
    logger.info("[JobRunner] Running jobs once...")
    for job in load_jobs():
        try:
            logger.info(f"Running job: {job.name}")
            job.run()
        except Exception as e:
            logger.error(f"Error in {job.name}: {e}")

if __name__ == "__main__":
    main()