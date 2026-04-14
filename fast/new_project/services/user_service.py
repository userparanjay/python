from fastapi import HTTPException,UploadFile,BackgroundTasks
from models.user_model import User
from db.database import SessionLocal
from sqlalchemy.orm import Session
from utils.email_service import (send_welcome_email,send_reset_password_email)
from middlewares.jwt_checker import verify_token_without_header
from schemas.users_schema import (LoginRequest,SignupRequest)
from utils.jwt_utils import (create_access_token,generate_reset_token)
import os
import uuid
import shutil
from utils.password_utils import (verify_password,hash_password)
UPLOAD_DIR = "uploads/profile_pictures"
def login_service(userDetails:LoginRequest,db:Session):
    try:
        user=db.query(User).filter(User.email==userDetails.email).first()
        if user:
            if verify_password(userDetails.password, user.hashed_password):
                token = create_access_token({
                        "id": user.id,
                        "email": user.email
                        })
                return ({
                        "message": "Login successful",
                         "access_token": token
                        })
            else:
                raise HTTPException(status_code=401, detail="Invalid password")
        else:
            raise HTTPException(status_code=404, detail="User not found or Invalid password")
    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail="Internal Server Error")


def signup_service(userDetails:SignupRequest, background_tasks: BackgroundTasks,db:Session):
    try:
        print(userDetails.email)
        existing_user = db.query(User).filter(User.email == userDetails.email).first()
        if existing_user:
          print(existing_user,">>>>")
          raise HTTPException(status_code=400, detail="User already exists")
        
        user_data = userDetails.model_dump()
        hashed_password = hash_password(user_data["password"])
        user_data.pop("password", None)
        user_data["hashed_password"] = hashed_password

        user=User(**user_data)
        db.add(user)
        db.commit()
        db.refresh(user)
        print(user,"signup")
        token = create_access_token({
                        "id": user.id,
                        "email": user.email
                        })
        background_tasks.add_task(send_welcome_email, user.email,user.username)
        return ({
                        "message": "Signup successful",
                         "access_token": token
                        })
    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail="Internal Server Error")

def get_user_by_id_service(id:str,db:Session):
    try:
        user = db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail="Internal Server Error")

def update_user_service_by_id(id:str,username:str,profile_picture:UploadFile,db:Session):
    try:
    
        user = db.query(User).filter(User.id ==id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if username:
            user.username = username
        filename = None
        if profile_picture:
            os.makedirs(UPLOAD_DIR, exist_ok=True)
            filename = f"{uuid.uuid4()}_{profile_picture.filename}"
            file_path = os.path.join(UPLOAD_DIR, filename)
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(profile_picture.file, buffer)

        if filename:
            user.profile_picture = filename
      
      
        db.commit()
        db.refresh(user)

        return user
    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail="Internal Server Error")
    
def change_password_service(old_password:str,new_password:str,id:str,db:Session):
    try:
        user = db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if not verify_password(old_password, user.hashed_password):
            raise HTTPException(status_code=400, detail="Incorrect old password")
        hashed_password = hash_password(new_password)
        user.hashed_password = hashed_password
        db.commit()
        db.refresh(user)
        return {"message": "Password changed successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail="Internal Server Error")
    
def reset_password_service(email,background_tasks,db):
    try:
        existing_user = db.query(User).filter(User.email == email).first()
        if not existing_user:
          raise HTTPException(status_code=400, detail="User does not exists")
        reset_token = generate_reset_token({
                        "id": existing_user.id,
                        "email": existing_user.email
                        })
        reset_link = f"http://localhost:8000/reset-password?token={reset_token}"
        background_tasks.add_task(send_reset_password_email, existing_user.email, reset_link)

    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail="Internal Server Error")
    
def confirm_reset_password_service(token, new_password, db):
    try:
        payload = verify_token_without_header(token)
        user_id = payload.get("id")
        if not user_id:
            raise HTTPException(status_code=400, detail="Invalid token")
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        hashed_password = hash_password(new_password)
        user.hashed_password = hashed_password
        db.commit()
        db.refresh(user)
        print(user,hashed_password,new_password,user,user_id,">>>>>")
        return {"message": "Password reset successfully"}
    except HTTPException as e:
        raise e
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail="Internal Server Error")

    

