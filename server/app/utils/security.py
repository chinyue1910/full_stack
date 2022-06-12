from typing import Optional
from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

from app.config.config import settings

ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def create_access_token(id: int, expires_delta: Optional[timedelta] = None):
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expire, 'sub': str(id)}
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)
