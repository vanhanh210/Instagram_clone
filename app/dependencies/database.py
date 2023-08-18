import motor.motor_asyncio
from beanie import init_beanie

from app.models.user import User

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/?directConnection=true")
database = client["instagram"]

# Initialize Beanie with the User model
init_beanie(database, document_models=[User])
