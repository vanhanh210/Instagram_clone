from pydantic import BaseModel
from fastapi import UploadFile, File
from app.models.user import User

class PostCreate(BaseModel):
    caption: str
    image: UploadFile = File(...)

class Post(BaseModel):
    id: str
    user_id: str
    caption: str  
    image_path: str 