from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.product import ProductCreate, Product
from services.product_service import create_product, get_product_by_id

router = APIRouter()

@router.post("/products/", response_model=Product)
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    db_product = get_product_by_id(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
