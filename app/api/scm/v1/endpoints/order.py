from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_orders():
    return {"orders": []}