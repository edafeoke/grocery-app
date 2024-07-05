from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

class UserCheck(UserBase):
    id: int
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str
