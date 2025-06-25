from pydantic import BaseModel, EmailStr
from typing import Optional

# -------------------
# User Schemas
# -------------------

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str


# -------------------
# Task Schemas
# -------------------

class TaskCreate(BaseModel):
    name: str

class TaskUpdate(BaseModel):
    name: Optional[str] = None
    is_done: Optional[bool] = None

class TaskOut(BaseModel):
    id: int
    name: str
    is_done: bool
    user_id: int

    class Config:
        orm_mode = True
