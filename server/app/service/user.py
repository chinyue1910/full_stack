from datetime import timedelta

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.crud.user import user as crud
from app.schemas import user as user_schema
from app.utils import security
from app.config.config import settings


class UserService:
    def authenticate(self, db: Session, email: str, password: str):
        user = crud.get_by_email(db, email)
        if not user:
            raise HTTPException(
                status_code=400, detail="Incorrect email or password")
        if not security.verify_password(password, user.hashed_password):
            return None
        access_token_expires = timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = security.create_access_token(
            id=user.id, expires_delta=access_token_expires
        )
        return access_token

    def create_user(self, db: Session, user_in: user_schema.UserCreate):
        user = crud.get_by_email(db, user_in.email)
        if user:
            raise HTTPException(
                status_code=400,
                detail="The user with this username already exists in the system.",
            )
        user = crud.create(db, user_in)
        return user

    def update_user(self, db: Session, user_id: int, password: str, email: str):
        user = crud.get(user_id)
        user_in = user_schema.UserUpdate(**user)
        if password is not None:
            user_in.password = password
        if email is not None:
            user_in.email = email
        user = crud.update(db, user, user_in)
        return user

userService = UserService()