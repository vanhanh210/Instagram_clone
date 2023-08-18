from datetime import datetime, timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr

from pymongo import MongoClient

# Placeholder values; replace with your actual secret key and JWT settings
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

router = APIRouter()

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str
    email: EmailStr
    exp: datetime
    
# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string
db = client["instagram"]  # Replace with your database name
users_collection = db["users"]  # Collection to store user data
    
# Placeholder function; replace with your actual user creation logic
def create_user(email: EmailStr, password: str):
    hashed_password = pwd_context.hash(password)
    user_data = {
        "email": email,
        "hashed_password": hashed_password
    }
    result = users_collection.insert_one(user_data)
    return result.inserted_id  # Return the ID of the inserted document

@router.post("/signup", response_model=Token)
async def signup_and_get_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Check if user with the given email already exists
    existing_user = get_user(email=form_data.username)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    # Create a new user with hashed password
    new_user_id = create_user(email=form_data.username, password=form_data.password)

    if not new_user_id:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to create user")
    
    # Retrieve the newly created user data based on the new_user_id
    new_user = users_collection.find_one({"_id": new_user_id})

     # Generate an access token for the new user
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": new_user["email"], "email": new_user["email"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

def get_user(email: EmailStr):
    user_data = users_collection.find_one({"email": email})
    return user_data    

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user_data = get_user(email=form_data.username)
    if not user_data:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    
    hashed_password = user_data.get("hashed_password")
    if not pwd_context.verify(form_data.password, hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")
    
    # Generate an access token for the user
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user_data["email"], "email": user_data["email"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# ... (other route definitions if needed)
