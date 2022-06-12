from typing import TYPE_CHECKING

from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship, validates

from app.db.base_class import Base

if TYPE_CHECKING:
    from app.models.board_follow import BoardFollow
    from app.models.user_follow import UserFollow
    from app.models.post_collect import PostCollect
    from app.models.tag_follow import TagFollow
    from app.models.post import Post


class User(Base):
    first_name = Column(String, nullable=False, comment="名字")
    last_name = Column(String, nullable=False, comment="姓")
    email = Column(String, unique=True, nullable=False, comment="信箱")
    public = Column(Boolean, nullable=False, default=True, comment="是否公開")

    @validates('email')
    def validate_email(self, key, address):
        if '@' not in address:
            raise ValueError("failed simple email validation")
        return address
    hashed_password = Column(String, nullable=False, comment="密碼")
    superuser = Column(Boolean, default=False, nullable=False, comment="管理者")

    posts = relationship("Post", backref="user")
    user_followings = relationship('User', secondary=UserFollow, backref="followers")
    board_followings = relationship('Board', secondary=BoardFollow)
    tag_followings = relationship('Tag', secondary=TagFollow)
    post_collections = relationship('Post', secondary=PostCollect)
