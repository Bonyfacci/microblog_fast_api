import datetime

from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from src.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)

    text = Column(Text, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    number_of_views = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.datetime.now())

    owner = relationship("User", back_populates="all_posts")
    all_comments = relationship("Comment", back_populates="posts")

# Поля поста:
# текст поста,
# автор,
# кол-во просмотров,
# дата создания.
