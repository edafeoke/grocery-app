# app/models/order_products.py

from sqlalchemy import Column, Integer, ForeignKey
from ..database import Base


class OrderProducts(Base):
    __tablename__ = 'order_products'

    order_id = Column(Integer, ForeignKey('orders.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
