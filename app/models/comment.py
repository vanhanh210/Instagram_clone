from beanie import Document
from datetime import datetime

class Comment(Document):
    post_id: str
    user_id: str
    content: str
    timestamp: datetime = datetime.now()
