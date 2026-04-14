from datetime import datetime
from typing import Optional
from pydantic import BaseModel,Field
from fastapi import UploadFile

class SignupRequest(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, example="john_doe")
    email: str = Field(..., example="john@gmail.com")
    password: str = Field(..., min_length=6, example="strongpassword")

class LoginRequest(BaseModel):
    email: str = Field(..., example="john@gmail.com")
    password: str = Field(..., example="strongpassword")

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    created_at: datetime
    profile_picture: Optional[str] = None

    class Config:
        from_attributes = True
    
class SignupResponse(BaseModel):
    message: str
    access_token: str

class LoginResponse(BaseModel):
    message: str
    access_token: str

class UpdateUserProfile(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50, example="john_doe")
    profile_picture: Optional[UploadFile] = None
    
