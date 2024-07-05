# app/crud/order.py

from sqlalchemy.orm import Session
from ..models import Order, Product, OrderProducts
from ..schemas import OrderCreate, Order as OrderSchema


def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()


def get_orders(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Order).offset(skip).limit(limit).all()


def create_order(db: Session, order: OrderCreate, user_id: int):
    db_order = Order(
        user_id=user_id, total_price=order.total_price, status=order.status)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)


    print('-----adding to db')
    for product_id in order.product_ids:
        order_product = OrderProducts(
            order_id=db_order.id, product_id=product_id)
        db.add(order_product)

    db.commit()
    return db_order


def update_order(db: Session, order_id: int, updated_order: OrderCreate):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order:
        db_order.total_price = updated_order.total_price
        db_order.status = updated_order.status
        db.commit()
        db.refresh(db_order)
    return db_order


def delete_order(db: Session, order_id: int):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
    return db_order
