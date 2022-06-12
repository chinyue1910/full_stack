from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, String, Integer

from app.db.base_class import Base

if TYPE_CHECKING:
    from app.models.board import Board

class Rule(Base):
    detail = Column(String, nullable=False, comment="規範內容")
    forbidden = Column(Integer, nullable=False, comment="禁言天數")
    board_id = Column(Integer, ForeignKey('board.id'), comment="看板")
