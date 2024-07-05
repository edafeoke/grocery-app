# app/routers/orders.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from ..dependencies import get_db, get_current_active_user
from ..schemas import Order as OrderSchema, OrderCreate
from ..models.user import User
from ..crud import order as crud_order

router = APIRouter(tags=['Order'])


@router.get("/", response_model=List[OrderSchema])
def read_orders(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    orders = crud_order.get_orders(db, skip=skip, limit=limit)
    return orders


@router.get("/{order_id}", response_model=OrderSchema)
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud_order.get_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


@router.post("/", response_model=OrderSchema)
def create_order(order: OrderCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return crud_order.create_order(db, order=order, user_id=current_user.id)


@router.put("/{order_id}", response_model=OrderSchema)
def update_order(order_id: int, order: OrderCreate, db: Session = Depends(get_db)):
    db_order = crud_order.update_order(
        db, order_id=order_id, updated_order=order)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


@router.delete("/{order_id}", response_model=OrderSchema)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud_order.delete_order(db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order
