import motor.motor_asyncio
from beanie import init_beanie
from ..models.user import User
from ..models.post import Post
from ..models.comment import Comment
import settings 

client = MongoClient(settings.mongodb_uri, settings.port)
db = client[instagram]]

# Initialize Beanie after defining the models
init_beanie(database, document_models=[User, Post, Comment])
