from pydantic import BaseModel

class CommentCreate(BaseModel):
    content: str
    post_id: str  

class Comment(BaseModel):
    id: str
    user_id: str
    content: str
    post_id: str
