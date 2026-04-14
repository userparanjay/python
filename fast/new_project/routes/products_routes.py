from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from db.database import get_db
from middlewares.jwt_checker import verify_token
from middlewares.role_checker import role_checker
from schemas.products_schema import (ProductCreate,ProductResponse,ProductUpdate)
from controllers.products_controller import (get_products_controller,create_product_controller,get_product_by_id_controller,update_product_by_id_controller,delete_product_by_id_controller)

router=APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get("",response_model=list[ProductResponse],summary="Get all product")
def get_products(search: str = None,skip: int = 0,
    limit: int = 10,db:Session=Depends(get_db)):
    return get_products_controller(search,skip,limit,db)

@router.post("",response_model=ProductResponse, summary="Create a new product")
def create_product(product:ProductCreate,db:Session=Depends(get_db), user = Depends(verify_token)):
    return create_product_controller(product,db)

@router.get("/{id}",response_model=ProductResponse)
def get_product(id:int,db:Session=Depends(get_db)):
    return get_product_by_id_controller(id,db)

@router.put("/{id}",response_model=ProductResponse)
def update_product_by_id(id:int,product:ProductUpdate,db:Session=Depends(get_db), user = Depends(verify_token)):
    return update_product_by_id_controller(id,product,db)

@router.delete("/{id}")
def delete_product_by_id(id:int,db:Session=Depends(get_db), user = Depends(role_checker("admin"))):
    return delete_product_by_id_controller(id,db)