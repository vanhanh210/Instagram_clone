from pydantic import BaseModel

class CommentCreate(BaseModel):
    content: str
    post_id: str  # We'll use this when creating a new comment

class Comment(BaseModel):
    id: str
    user_id: str
    content: str
    post_id: str
