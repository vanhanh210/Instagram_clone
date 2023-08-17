from fastapi import APIRouter, HTTPException, Depends, Form
from fastapi.security import OAuth2PasswordRequestForm
from ..models.user import User, password_context
from ..dependencies.security import create_access_token, oauth2_scheme, verify_password
from pydantic import BaseModel

router = APIRouter()

class UserCreate(BaseModel):
    username: str
    password: str
    email: str

class Token(BaseModel):
    access_token: str
    token_type: str

@router.post("/signup/")
async def signup(username: str = Form(...), password: str = Form(...), email: str = Form(...)):
    user_in_db = await User.find_one({"username": username})
    if user_in_db:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = User.create_hashed_password(password)
    new_user = User(username=username, hashed_password=hashed_password, email=email)
    await new_user.insert()

    return {"message": "User successfully registered", "username": username}

@router.post("/token/", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.find_one({"username": form_data.username})
    if user is None or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
