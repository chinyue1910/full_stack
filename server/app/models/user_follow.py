from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint

from app.db.base_class import Base

if TYPE_CHECKING:
    from app.models.user import User

class UserFollow(Base):
    user_id = Column(Integer, ForeignKey('user.id'), comment="作者")
    follow_id = Column(Integer, ForeignKey('user.id'), comment="追蹤者")

    UniqueConstraint('user_id', 'follow_id')