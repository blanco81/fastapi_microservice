from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.category import CategoryCreate, Category
from services.category_service import create_category, get_category_by_id

router = APIRouter()

@router.post("/categories/", response_model=Category)
def create_new_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, category)


@router.get("/categories/{category_id}", response_model=Category)
def get_category(category_id: int, db: Session = Depends(get_db)):
    db_category = get_category_by_id(db, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


