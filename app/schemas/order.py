# app/schemas/order.py

from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from ..schemas.product import Product


class OrderBase(BaseModel):
    
    total_price: float
    status: Optional[str] = "pending"
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class OrderCreate(OrderBase):
    product_ids: List[int]


class OrderUpdate(BaseModel):
    total_price: Optional[float] = None
    status: Optional[str] = None
    updated_at: datetime = datetime.now()


class Order(OrderBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    products: List[Product] = []

    class Config:
        orm_mode = True
