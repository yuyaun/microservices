"""Internal API router registering health check endpoints."""

from fastapi import APIRouter
from app.api.internal.v1.endpoints import healthcheck

    healthcheck.router,
    prefix="/health",
    tags=["internal:health"],
)

