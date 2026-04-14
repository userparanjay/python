from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from models.user_model import User
from db.database import get_db
from dotenv import load_dotenv
import os
secure=HTTPBearer()
load_dotenv()

SECRET_KEY=os.getenv('SECRET_KEY')
ALGORITHM=os.getenv('ALGORITHM')

def role_checker(role:str):

    def checker(cred:HTTPAuthorizationCredentials=Depends(secure),db: Session = Depends(get_db)):
        token=cred.credentials
        try:
            decode_payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
            print(decode_payload,">>>>>>>>")
            user_exists=db.query(User).filter(User.id == decode_payload["id"]).first()
            print(user_exists,"user_exists")
            if not user_exists:
                raise HTTPException(status_code=404, detail="User does not exists")
            if user_exists.role != role:
                raise HTTPException(status_code=403, detail="User does not have the required role")
            return decode_payload
        except JWTError:
             raise HTTPException(
                status_code=401,
                detail="Invalid or expired token"
            )
    return checker
    
