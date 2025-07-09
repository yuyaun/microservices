from fastapi import APIRouter

router = APIRouter()


@router.get("/")def get_orders() -> dict:
    """Return a list of orders."""
    return {"orders": []}

