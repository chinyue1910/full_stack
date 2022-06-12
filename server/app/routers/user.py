from typing import List, Optional

from fastapi import APIRouter, Form, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from pydantic.networks import EmailStr

from app.service.user import userService
from app.crud.user import user as user_curd
from app.models import user as user_model
from app.schemas import token as token_scheme, user as user_schema
from app.utils import deps
from app.middleware.permission import PermissionMiddleware


router = APIRouter()


@router.post("/login", response_model=token_scheme.Token)
def login(db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    access_token = userService.authenticate(
        db, form_data.username, form_data.password)
    return {
        "access_token": access_token,
        "token_type": "bearer",
    }


@router.get("", response_model=List[user_schema.User])
@PermissionMiddleware.admin
def read_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user=Depends(deps.get_current_user)
):
    users = user_curd.index(db, skip, limit)
    return users


@router.post("", response_model=user_schema.User)
def create_user(
    user_in: user_schema.UserCreate,
    db: Session = Depends(deps.get_db),
):
    user = userService.create_user(db, user_in)
    return user


@router.patch("/{user_id}", response_model=user_schema.User)
@PermissionMiddleware.member
def update_user(
    user_id: int,
    db: Session = Depends(deps.get_db),
    password: str = Form(None),
    email: EmailStr = Form(None),
    current_user=Depends(deps.get_current_user)
):
    user = userService.update_user(db, user_id, password, email)
    return user


@router.get("/{user_id}", response_model=user_schema.User)
@PermissionMiddleware.member
def get_user(
    user_id: int,
    db: Session = Depends(deps.get_db),
    current_user=Depends(deps.get_current_user)
):
    user = user_curd.get(db, user_id)
    return user


@router.delete("/{user_id}")
@PermissionMiddleware.member
def delete_user(
    user_id: int,
    db: Session = Depends(deps.get_db),
    current_user=Depends(deps.get_current_user)
):
    user_curd.remove(db, user_id)
