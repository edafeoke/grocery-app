# app/schemas/order.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class OrderBase(BaseModel):
    user_id: int
    total_price: float
    status: Optional[str] = "pending"
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    total_price: Optional[float] = None
    status: Optional[str] = None
    updated_at: datetime = datetime.now()


class Order(OrderBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
