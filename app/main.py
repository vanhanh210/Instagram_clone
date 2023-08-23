from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

from app.dependencies import \
from app.routers import authentication, comments, posts

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")  

app.include_router(authentication.router)
app.include_router(posts.router)
app.include_router(comments.router)
