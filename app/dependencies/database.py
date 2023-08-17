from beanie import init_beanie
import motor.motor_asyncio
from .settings import settings
from app.models import User, Post, Comment

async def init():
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.database_url)
    database = client.get_default_database()
    
    # Initialize beanie for each data model
    await init_beanie(database, document_models=[User, Post, Comment])
