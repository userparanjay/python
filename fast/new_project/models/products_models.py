from sqlalchemy import Column,Integer,String,Float
from db.database import Base

class Product(Base):
    __tablename__ = 'products'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50),nullable=False)
    price=Column(Float,nullable=False)
    description=Column(String(200),nullable=True)
    quantity=Column(Integer,nullable=False)