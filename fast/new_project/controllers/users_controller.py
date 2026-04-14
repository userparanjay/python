from sqlalchemy.orm import Session
from fastapi import BackgroundTasks
from schemas.users_schema import (LoginRequest,SignupRequest,UpdateUserProfile)
from services.user_service import (login_service,signup_service,update_user_service_by_id,get_user_by_id_service,change_password_service,reset_password_service,confirm_reset_password_service)
def login_controller(userDetails:LoginRequest,db:Session):
    return login_service(userDetails,db)

def signup_controller(userDetails:SignupRequest,background_tasks:BackgroundTasks,db:Session):
    return signup_service(userDetails,background_tasks,db)
    
def update_user_controller_by_id(id, username, profile_picture, db):
    return update_user_service_by_id(id, username, profile_picture, db)

def get_user_controller_by_id(id, db):
    return get_user_by_id_service(id, db)


def change_password_controller(old_password, new_password,id, db):
    return change_password_service(old_password, new_password,id, db)

def reset_password_controller(email,background_tasks,db):
    return reset_password_service(email,background_tasks,db)

def confirm_reset_password_controller(token, new_password, db):
    return confirm_reset_password_service(token, new_password, db)
