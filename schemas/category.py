from typing import List
from pydantic import BaseModel
from schemas.product import Product

class CategoryBase(BaseModel):
    name: str
    description: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int
    products: List['Product'] = []

    class Config:
        from_attributes = True

