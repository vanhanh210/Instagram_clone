from fastapi import FastAPI
from config import settings
from models.user import init_db
from routers import user, post

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)

@app.on_event("startup")
async def on_startup():
    await init_db()
