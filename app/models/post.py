from datetime import datetime

from beanie import Document


class Post(Document):
    user_id: str
    image: str
    timestamp: datetime = datetime.now()
