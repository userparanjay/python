from sqlalchemy.orm import Session
from fastapi import HTTPException
from schemas.products_schema import (ProductCreate,ProductUpdate)
from services.product_service import (
    get_products_service,
    create_product_service,
    get_product_service,
    update_product_by_id_service,
    delete_product_by_id_service
)
def get_products_controller(search:str,skip:int,limit:int,db:Session):
    try:
        products= get_products_service(search,skip,limit,db)
        return products
    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail=str(e))
    
def create_product_controller(product_data:ProductCreate,db:Session):
    try:
        product = create_product_service(product_data, db)
        return product
    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    
def get_product_by_id_controller(id:int,db:Session):
    try:
        product=get_product_service(id,db)
        return product
    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    
def update_product_by_id_controller(id:int,product_data:ProductUpdate,db:Session):
    try:
        product=update_product_by_id_service(id,product_data,db)
        return product
    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
    
def delete_product_by_id_controller(id:int,db:Session):
    try:
        product=delete_product_by_id_service(id,db)
        return product
    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))