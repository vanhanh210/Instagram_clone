from pydantic import BaseModel

class PostCreate(BaseModel):
    caption: str

class Post(BaseModel):
    id: str
    user_id: str
    caption: str  
    image_path: str
