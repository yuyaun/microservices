from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Order(Base):
    """ORM model representing an order."""

    __tablename__ = "orders"
    def __repr__(self) -> str:
        """Return a debug representation of the order."""
        return f"<Order id={self.id} customer_name='{self.customer_name}'>"
    id = Column(Integer, primary_key=True, index=True)    customer_name = Column(String)

