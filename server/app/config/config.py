import secrets

from pydantic import BaseSettings, Field
from typing import Optional


class Settings(BaseSettings):
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SECRET_KEY: str = "0a08a6bd868e1dc600b7af8e41ab87d34405593e5d133e779339bf96f24269c2"
    POSTGRES_USER: str = Field(..., env='POSTGRES_USER')
    POSTGRES_PASSWORD: str = Field(..., env='POSTGRES_PASSWORD')
    POSTGRES_SERVER: str = Field(..., env='POSTGRES_SERVER')
    POSTGRES_DB: str = Field(..., env='POSTGRES_DB')

    def SQLALCHEMY_DATABASE_URI(self):
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"


settings = Settings()
