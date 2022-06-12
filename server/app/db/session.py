from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.config import settings


engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URI(), echo=True, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
