from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from app.job.jobs.cleanup_order import CleanupOrderJob
from app.job.jobs.sync_product import SyncProductJob
from app.core.logger import log_event


def create_scheduler() -> BackgroundScheduler:
    """Create and configure the background scheduler."""
    scheduler = BackgroundScheduler()

    # Register jobs with their cron schedules. Comment out any job you want to disable.
    scheduler.add_job(
        CleanupOrderJob().run,
        CronTrigger(hour=1, minute=0),
        id="cleanup_order",
        name="cleanup_order",
    )
    scheduler.add_job(
        SyncProductJob().run,
        CronTrigger(minute=0),
        id="sync_product",
        name="sync_product",
    )
    log_event("scheduler", "register_jobs", {"jobs": ["cleanup_order", "sync_product"]})
    return scheduler


scheduler = create_scheduler()


def start() -> None:
    """Start the background scheduler."""
    scheduler.start()
    log_event("scheduler", "start", {})


def shutdown() -> None:
    """Shutdown the background scheduler."""
    scheduler.shutdown()
    log_event("scheduler", "shutdown", {})


if __name__ == "__main__":
    start()
    try:
        # Keep the script running to allow scheduled jobs to execute
        import time

        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        shutdown()

