from fastapi import FastAPI
from .routers import authentication, posts, comments

app = FastAPI()

app.include_router(authentication.router)
app.include_router(posts.router)
app.include_router(comments.router)
