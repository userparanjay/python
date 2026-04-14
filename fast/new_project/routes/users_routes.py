from controllers.users_controller import (login_controller,signup_controller,update_user_controller_by_id,get_user_controller_by_id,change_password_controller,reset_password_controller,confirm_reset_password_controller)
from fastapi import APIRouter,UploadFile, File, Form,Depends,BackgroundTasks
from fastapi.responses import RedirectResponse
import os
from sqlalchemy.orm import Session
from db.database import get_db
from middlewares.jwt_checker import (verify_token,verify_token_without_header)
from schemas.users_schema import (LoginRequest,SignupRequest,SignupResponse,LoginResponse,UserResponse,UpdateUserProfile)

user_routes=APIRouter(
    tags=["users"]
)

@user_routes.post("/login")
def login(userDetails:LoginRequest,response_model=LoginResponse,db:Session=Depends(get_db)):
    return login_controller(userDetails,db)

@user_routes.post("/signup",response_model=SignupResponse)
def signup(userDetails:SignupRequest, background_tasks: BackgroundTasks,db:Session=Depends(get_db)):
    return signup_controller(userDetails,background_tasks,db)

@user_routes.put("/user/update",response_model=UserResponse)
def update_user(username: str = Form(None),
    profile_picture: UploadFile = File(None),db:Session=Depends(get_db), user = Depends(verify_token)):
    return update_user_controller_by_id(user["id"],username,profile_picture,db)

@user_routes.get("/user/me",response_model=UserResponse)
def get_me(db:Session=Depends(get_db), user = Depends(verify_token)):
    return get_user_controller_by_id(user["id"], db)

@user_routes.post("/change-password")
def change_password(old_password:str,new_password:str,db:Session=Depends(get_db), user = Depends(verify_token)):
    return change_password_controller(old_password,new_password,user["id"],db)

@user_routes.post("/reset-password")
def reset_password(email:str,background_tasks: BackgroundTasks,db:Session=Depends(get_db)):
    return reset_password_controller(email,background_tasks,db)

@user_routes.get("/reset-password")
def verify_reset_token(token: str):
    # Validate token first; then redirect to frontend reset page.
    verify_token_without_header(token)
    app_url = os.getenv("APP_URL", "http://localhost:3000").rstrip("/")
    return RedirectResponse(url=f"{app_url}/reset-password?token={token}")

@user_routes.post("/reset-password/confirm")
def confirm_reset_password(token: str, new_password: str, db: Session = Depends(get_db)):
    return confirm_reset_password_controller(token, new_password, db)
