from beanie import Document, init_beanie
from pydantic import BaseModel
from typing import Optional
import datetime

class Post(Document):
    id: Optional[str]
    user_id: str
    image_url: str
    caption: Optional[str]
    created_at: datetime.datetime = datetime.datetime.now()
