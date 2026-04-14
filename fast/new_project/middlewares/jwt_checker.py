from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException
from dotenv import load_dotenv
from jose import jwt, JWTError
from fastapi import Depends
import os

security=HTTPBearer()
load_dotenv()

SECRET_KEY=os.getenv('SECRET_KEY')
ALGORITHM=os.getenv('ALGORITHM')
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token=credentials.credentials
    try:
        decode_payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return decode_payload
    except JWTError:
         raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )
    
def verify_token_without_header(token):
    try:
        print(token)
        decode_payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        print(decode_payload)
        return decode_payload
    except JWTError:
         raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

