"""SCM API router registering order endpoints."""

from fastapi import APIRouter
from app.api.scm.v1.endpoints import order

    order.router,
    prefix="/orders",
    tags=["scm:orders"],
)

