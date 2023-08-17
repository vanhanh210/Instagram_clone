from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from pydantic import BaseModel
from app.dependencies.security import create_access_token, get_current_user
from app.models.user import User
from app.settings import settings

router = APIRouter()

class UserCreate(BaseModel):
    email: str
    password: str
    full_name: str

class UserLogin(BaseModel):
    email: str
    password: str

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/signup/")
async def signup(user: UserCreate):
    user_in_db = await User.get(user.email)
    if user_in_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    hashed_password = pwd_context.hash(user.password)
    new_user = await User(email=user.email, hashed_password=hashed_password, full_name=user.full_name).insert()
    return new_user

@router.post("/login/")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.get(form_data.username)
    if not user or not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
