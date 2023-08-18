from datetime import datetime

from beanie import Document


class Comment(Document):
    post_id: str
    user_id: str
    content: str
    timestamp: datetime = datetime.now()
