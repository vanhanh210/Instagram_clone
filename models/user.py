import beanie
from pydantic import BaseModel
from beanie import init_beanie, Document
from config import settings

class User(Document):
    username: str
    hashed_password: str

async def init_db():
    await init_beanie(settings.MONGO_URI, document_models=[User])
