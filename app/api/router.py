"""Main API router wiring service-specific routers."""

from fastapi import APIRouter
from app.api.mcm.v1.router import router as mcm_router
from app.api.scm.v1.router import router as scm_router
from app.api.internal.v1.router import router as internal_router

api_router = APIRouter()
api_router.include_router(mcm_router, prefix="/mcm/v1")

