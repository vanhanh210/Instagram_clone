from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.models.user import User  # Importing the User model
from app.dependencies.database import users_collection
from app.settings import SECRET_KEY, ALGORITHM  # Importing the configurations
from app.dependencies.security import get_password_hash, verify_password
from jose import jwt
import datetime
import uuid


router = APIRouter()
TOKEN_EXPIRY = datetime.timedelta(days=1)

def hash_password(password: str):
    return get_password_hash(password)

@router.post("/signup")
async def signup(form_data: OAuth2PasswordRequestForm = Depends()):
    # Check if user exists
    user = users_collection.find_one({"username": form_data.username})
    if user:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    # Hash password
    hashed_password = hash_password(form_data.password)
    
    # Create new user and insert into database
    new_user = User(id=str(uuid.uuid4()), username=form_data.username, hashed_password=hashed_password)
    users_collection.insert_one(new_user.dict())
    
    return {"message": "User created successfully!"}

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_collection.find_one({"username": form_data.username})
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    # Create JWT token and return
    token_data = {
        "sub": user["username"],
        "exp": datetime.datetime.utcnow() + TOKEN_EXPIRY
    }
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    
    return {"access_token": token}
