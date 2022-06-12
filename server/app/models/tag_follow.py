from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint

from app.db.base_class import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.tag import Tag

class TagFollow(Base):
    user_id = Column(Integer, ForeignKey('user.id'), comment="作者")
    follow_id = Column(Integer, ForeignKey('tag.id'), comment="標籤")

    UniqueConstraint('user_id', 'follow_id')