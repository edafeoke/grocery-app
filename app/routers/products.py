from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, utils
from ..dependencies import get_db, check_admin

router = APIRouter(
    tags=['Product']
)


@router.post("/products/", response_model=schemas.product.Product)
def create_product(product: schemas.product.ProductCreate, db: Session = Depends(get_db), user: schemas.user.User=Depends(check_admin)):
    return crud.create_product(db=db, product=product)


@router.get("/products/", response_model=List[schemas.product.Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@router.put("/products/{id}", response_model=schemas.product.Product)
def read_products(id: int, product: schemas.product.ProductUpdate, db: Session = Depends(get_db), user: schemas.user.User = Depends(check_admin)):
    product = crud.update_product(db, id, product)
    return product

@router.delete('/products/{id}')
def delete_product(id: int, db: Session = Depends(get_db), admin: schemas.user.UserCheck = Depends(check_admin)):
    product = crud.delete_product(db, id)
    return product