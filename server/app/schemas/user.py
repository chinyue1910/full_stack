from typing import Optional

from pydantic import BaseModel, EmailStr, constr


class UserBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None


class UserCreate(UserBase):
    first_name: constr(min_length=1, max_length=20)
    last_name: constr(min_length=1, max_length=20)
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None

class UserInDB(UserBase):
    id: Optional[int] = None
    superuser: bool = False
    class Config:
        orm_mode = True


class User(UserInDB):
    pass
