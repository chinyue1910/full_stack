from typing import Optional

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.utils import security
from app.config.config import settings
from app.schemas import token as token_scheme
from app.crud.user import user as curd
from app.models.user import User as user_model

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/login")


def get_db():
    with SessionLocal() as session:
        yield session


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    payload = jwt.decode(
        token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = token_scheme.TokenPayload(**payload)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = curd.get(db, token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
