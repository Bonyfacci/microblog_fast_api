from pydantic import BaseModel


class CommentBase(BaseModel):
    owner_id: int
    text: str


class CommentCreate(CommentBase):
    post_id: int


class Comment(CommentBase):
    id: int
    post_id: int

    class Config:
        from_attributes = True


class CommentDetails(CommentBase):
    pass
