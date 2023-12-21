from pydantic import BaseModel
#from schemas.category import CategoryBase

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    season: str

class ProductCreate(ProductBase):
    category_id: int

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True
