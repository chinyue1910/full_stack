from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint

from app.db.base_class import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.post import Post

class PostCollect(Base):
    user_id = Column(Integer, ForeignKey('user.id'), comment="作者")
    post_id = Column(Integer, ForeignKey('post.id'), comment="文章")

    UniqueConstraint('user_id', 'post_id')