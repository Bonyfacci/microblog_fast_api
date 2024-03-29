from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from src.database import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)

    owner_id = Column(Integer, ForeignKey("users.id"))
    text = Column(Text, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"))

    owner = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")

# Поля комментария:
# автор,
# содержание,
# пост.
