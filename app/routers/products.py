from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, utils
from ..dependencies import get_db, get_current_active_user

router = APIRouter(
    tags=['Product']
)


@router.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)


@router.get("/products/", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@router.put("/products/{id}", response_model=schemas.Product)
def read_products(id: int, db: Session = Depends(get_db)):
    products = crud.get_product(db, id)
    return products
