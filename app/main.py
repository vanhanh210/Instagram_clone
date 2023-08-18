import motor.motor_asyncio
from beanie import Document, init_beanie
from fastapi import FastAPI
from app.models.user import User
from app.routers import authentication, comments, posts

app = FastAPI()

app.include_router(authentication.router)
app.include_router(posts.router)
app.include_router(comments.router)

DATABASE_URL = "mongodb://localhost:27017/?directConnection=true"
DATABASE_NAME = "instagram"

client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
database = client[DATABASE_NAME]

@app.on_event("startup")
async def on_startup():
    await init_beanie(database, document_models=[User])