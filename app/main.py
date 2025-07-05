import os
from fastapi import FastAPI
from app.api.router import api_router
from app.core.database import Base, engine
from app.job import scheduler

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(api_router)

if os.getenv("CRON_JOB", "false").lower() in {"1", "true", "yes"}:
    scheduler.start()
