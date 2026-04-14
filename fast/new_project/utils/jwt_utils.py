from datetime import datetime, timedelta
from http.client import HTTPException
from dotenv import load_dotenv
from jose import jwt, JWTError
import os

load_dotenv()

SECRET_KEY=os.getenv('SECRET_KEY')
ALGORITHM=os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))

def create_access_token(data:dict):
    to_encode=data.copy()
    print(to_encode)

    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp":expire})

    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def generate_reset_token(data:dict):
    to_encode=data.copy()
    print(to_encode)

    expire=datetime.utcnow()+timedelta(minutes=2)

    to_encode.update({"exp":expire})

    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    
    return encoded_jwt

