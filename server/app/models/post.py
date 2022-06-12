from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, String, Integer, Text
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from app.models.board import Board
    from app.models.user import User
    from app.models.post_tag import PostTag

class Post(Base):
    title = Column(String, nullable=False, comment="文章標題")
    content = Column(Text, nullable=False, comment="文章內容")
    board_id = Column(Integer, ForeignKey('board.id'), comment="看板")
    user_id = Column(Integer, ForeignKey('user.id'), comment="作者")
    
    tags = relationship('User', secondary=PostTag, backref="posts")