import os
import uuid

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, Header
from fastapi.security import OAuth2PasswordBearer

from app.dependencies.database import posts_collection
from app.dependencies.security import get_current_user, oauth2_scheme
from app.models.post import Post, PostCreate
from app.models.user import User

router = APIRouter()

@router.post("/create-post", response_model=str)
async def create_post(
    caption: str = Form(...),
    image: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    token: str = Depends(oauth2_scheme)  # Use oauth2_scheme as a dependency
):
    # Verify the access token (optional, depending on your use case)
    if authorization != "Bearer " + current_user.access_token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    # Save the uploaded image
    image_filename = os.path.join("uploads", f"{uuid.uuid4()}_{image.filename}")
    with open(image_filename, "wb") as buffer:
        buffer.write(image.file.read())
    
    # Create post data
    post_data = {
        "id": str(uuid.uuid4()),
        "user_id": current_user.id,
        "caption": caption,
        "image_path": image_filename
    }
    
    # Insert post data into the database
    posts_collection.insert_one(post_data)
    
    return {"post_id": post_data["id"]}
