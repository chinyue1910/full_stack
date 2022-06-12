from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from app.models.post import Post
    from app.models.tag import Tag

class PostTag(Base):
    post_id = Column(Integer, ForeignKey('post.id'), comment="文章")
    tag_id = Column(Integer, ForeignKey('tag.id'), comment="標籤")

    UniqueConstraint('post_id', 'tag_id')