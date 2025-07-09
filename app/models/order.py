from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Order(Base):
    """ORM model representing an order."""

    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)    customer_name = Column(String)

