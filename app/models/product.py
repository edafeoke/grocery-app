# app/models/product.py

from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from ..database import Base
from datetime import datetime


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)

    orders = relationship(
        "Order", secondary="order_products", back_populates="products")
