from datetime import datetime, timedelta

import jwt
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from app.dependencies.database import \
    users_collection  # Importing the users collection for direct interaction
from app.models.user import User
from app.settings import ALGORITHM  # Importing the required configurations
from app.settings import SECRET_KEY
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
# Password encryption and verification
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 password bearer instance for token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_password_hash(password: str):
    return password_context.hash(password)

def verify_password(plain_password, hashed_password):
    return password_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        print("Decoding JWT token...")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(f"Decoded payload: {payload}")
        
        print("Extracting userxname from payload...")
        username: str = payload.get("sub")
        print(f"Extracted username: {username}")
        
        if username is None:
            raise HTTPEpyxception(status_code=401, detail="Username not found in token.")
    except JWTError:
        raise HTTPException(status_code=401, detail="Error in JWT decoding or validation.")
    
    print("Fetching user from database...")
    user = users_collection.find_one({"username": username})
    print(f"Fetched user: {user}")
    
    if user is None:
        raise HTTPException(status_code=401, detail="User not found in database.")
    return User(**user)    