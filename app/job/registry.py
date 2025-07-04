import importlib
import pkgutil
from app.job.job_base import Job

def load_jobs():
    jobs = []
    package = "app.job.jobs"
    for _, module_name, _ in pkgutil.iter_modules(["app/job/jobs"]):
        module = importlib.import_module(f"{package}.{module_name}")
        for attr in dir(module):
            cls = getattr(module, attr)
            if isinstance(cls, type) and issubclass(cls, Job) and cls is not Job:
                jobs.append(cls())
    return jobs