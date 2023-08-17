from fastapi import FastAPI
from app.dependencies import database
from app.routers import authentication, posts, comments

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await database.init()

app.include_router(authentication.router)
app.include_router(posts.router)
app.include_router(comments.router)
