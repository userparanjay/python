from sqlalchemy.orm import Session
from models.products_models import Product
from schemas.products_schema import (ProductCreate,ProductUpdate)
from fastapi import HTTPException

def get_products_service(search,skip,limit,db:Session):
    if search:
        products= db.query(Product).filter(Product.name.ilike(f"%{search}%")).offset(skip).limit(limit).all()
        return products
    products= db.query(Product).offset(skip).limit(limit).all()
    if not products:
        raise HTTPException(status_code=404, detail="No products found")
    return products

def create_product_service(product:ProductCreate,db:Session):
    try:
        new_product= Product(**product.model_dump())
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error creating product: {str(e)}")
    
def get_product_service(product_id:int,db:Session):
    try:
        product=db.query(Product).filter(Product.id==product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching product: {str(e)}")

def update_product_by_id_service(id:int,product_data:ProductUpdate,db:Session):
    try:
        product=db.query(Product).filter(Product.id==id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        items=product_data.model_dump(exclude_unset=True).items()
        for key, value in items:
            setattr(product, key, value)
        db.commit()
        db.refresh(product)
        return product
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating product: {str(e)}")

def delete_product_by_id_service(id:int,db:Session):
    try:
        product=db.query(Product).filter(Product.id==id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        db.delete(product)
        db.commit()
        return {"message": "Product deleted successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting product: {str(e)}")