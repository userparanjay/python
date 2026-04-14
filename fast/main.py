from fastapi import FastAPI
from product_model import Products
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

products = [
    Products(
        id=1,
        name="Laptop",
        price=999.99,
        description="this is a laptop",
        quantity=10
    ),
    Products(
        id=2,
        name="Mouse",
        price=19.99,
        description="this is a mouse",
        quantity=50
    ),
    Products(
        id=3,
        name="Keyboard",
        price=49.99,
        description="this is a keyboard",
        quantity=30
    )
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def greet():
    return {"message": "Hello World"}

@app.get("/products")
def get_products():
    return products

@app.get("/product/{id}")
def get_product(id:int):
    return next((p for p in products if p.id == id),None)
   

@app.post("/products")
def add_product(product:Products):
    products.append(product)
    return {"message": "Product added successfully"}

@app.put("/products/{id}")
def update_product(id:int,product:Products):
    old_product=next((p for p in products if p.id == id),None)
    print(old_product)
    if (old_product):
        products.remove(old_product)
        products.append(product)
    return products

@app.delete("/products/{id}")
def delete_product(id):
    id=int(id)
    product=next((p for p in products if p.id == id),None)
    if (product):
        products.remove(product)
        print(products,">>>>")
    return products