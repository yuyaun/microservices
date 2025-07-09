from app.core.database import SessionLocal
from app.models.order import Order


def create_order(customer_name: str) -> Order:
    """Create and persist a new order."""

    db = SessionLocal()
    order = Order(customer_name=customer_name)
    db.add(order)
    db.commit()
    db.refresh(order)
    db.close()    return order

