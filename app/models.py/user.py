from beanie import Document, init_beanie
from pydantic import BaseModel, EmailStr
from typing import Optional
import datetime

class User(Document):
    class Settings:
        arbitrary_types_allowed = True

    id: Optional[str]
    email: EmailStr
    hashed_password: str
    full_name: Optional[str]
    created_at: datetime.datetime = datetime.datetime.now()
