from typing import TYPE_CHECKING

from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import relationship

from app.db.base_class import Base


if TYPE_CHECKING:
    from app.models.rule import Rule
    from app.models.post import Post


class Board(Base):
    title = Column(String, nullable=False, comment="看板名稱")
    thumbnail = Column(String, comment="縮圖")
    content = Column(Text, nullable=False, comment="看板規則")

    rules = relationship("Rule")
    posts = relationship('Post', backref="board")