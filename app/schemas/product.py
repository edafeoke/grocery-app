from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    created_at: datetime
    updated_at: datetime


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    updated_at: datetime = datetime.now()

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
