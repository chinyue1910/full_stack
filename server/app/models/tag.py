from sqlalchemy import Column, String, Integer

from app.db.base_class import Base

class Tag(Base):
    title = Column(String, nullable=False, comment="標籤名稱")
