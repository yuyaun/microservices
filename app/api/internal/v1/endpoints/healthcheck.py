from fastapi import APIRouter

router = APIRouter()


@router.get("/")def healthcheck() -> dict:
    """Return service health status."""
    return {"status": "ok"}

