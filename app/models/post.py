from beanie import Document
from datetime import datetime

class Post(Document):
    user_id: str
    image: str
    caption: str = None  # Caption/description for the post
    timestamp: datetime = datetime.now()
