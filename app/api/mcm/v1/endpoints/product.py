from fastapi import APIRouter

router = APIRouter()


@router.get("/")def get_product() -> dict:
    """Return a sample product."""
    return {"product": "Sample product"}

