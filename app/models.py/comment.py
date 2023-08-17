from beanie import Document, init_beanie
from pydantic import BaseModel
from typing import Optional
import datetime

class Comment(Document):
    id: Optional[str]
    post_id: str
    user_id: str
    content: str
    created_at: datetime.datetime = datetime.datetime.now()
