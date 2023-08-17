from typing import List
import beanie
from pydantic import BaseModel
from beanie import Document

class Post(Document):
    user_id: str
    image_url: str
    caption: str
    comments: List[str]
