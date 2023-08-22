from fastapi import APIRouter, Depends

from app.dependencies.database import comments_collection
from app.dependencies.security import get_current_user
from app.models.comment import (  # Importing the classes from comment.py
    Comment, CommentCreate)
from app.models.user import User
from typing import List


router = APIRouter()

@router.post("/posts/{post_id}/comments", response_model=str)
async def create_comment(post_id: str, comment: CommentCreate, current_user: User = Depends(get_current_user)):
    # Check if the post exists
    if not posts_collection.find_one({"id": post_id}):
        raise HTTPException(status_code=404, detail="Post not found")
    
    # Create comment data
    comment_data = {
        "id": str(uuid.uuid4()),
        "user_id": current_user.id,
        "post_id": post_id,
        "content": comment.content
    }
    
    # Insert comment data into the database
    comments_collection.insert_one(comment_data)
    
    return {"comment_id": comment_data["id"]}

@router.get("/posts/{post_id}/comments", response_model=List[Comment])
async def get_comments_for_post(post_id: str):
    comments = list(comments_collection.find({"post_id": post_id}))
    return comments
