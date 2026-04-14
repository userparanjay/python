from pydantic import BaseModel,Field
from typing import Optional

class ProductBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, example="iPhone 15")
    price: float = Field(..., gt=0,example=999.99)
    description: Optional[str] = Field(None, max_length=200,example="Apple smartphone with A16 chip")
    quantity: int = Field(..., ge=0,example=10)

class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=50)
    price: Optional[float] = Field(None, gt=0)
    description: Optional[str] = Field(None, max_length=200)
    quantity: Optional[int] = Field(None, ge=0)

class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True