"""MCM API router registering product endpoints."""

from fastapi import APIRouter
from app.api.mcm.v1.endpoints import product

    product.router,
    prefix="/products",
    tags=["mcm:products"],
)

