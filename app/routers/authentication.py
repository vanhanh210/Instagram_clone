from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user import User
from app.dependencies.database import users_collection
from app.settings import SECRET_KEY, ALGORITHM
from app.dependencies.security import get_password_hash, verify_password, create_access_token
import uuid

router = APIRouter()

@router.post("/signup")
async def signup(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_collection.find_one({"username": form_data.username})
    if user:
        raise HTTPException(status_code=400, detail="Username already exists")
    hashed_password = get_password_hash(form_data.password)
    new_user = {
        "id": str(uuid.uuid4()), 
        "username": form_data.username, 
        "hashed_password": hashed_password
    }
    users_collection.insert_one(new_user)
    return {"message": "User created successfully!"}

@router.post("/login", response_model=dict)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_collection.find_one({"username": form_data.username})
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token_data = {
        "sub": user["username"],
    }
    token = create_access_token(token_data)
    return {"access_token": token, "token_type": "bearer"}