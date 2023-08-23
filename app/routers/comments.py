from fastapi import APIRouter, Depends, HTTPException, Form
from app.dependencies.database import comments_collection
from app.dependencies.security import reusable_oauth2, validate_token

router = APIRouter()

@router.post("/create-comment")
async def create_comment(
    content: str = Form(...),
    post_id: str = Form(...),
    token: str = Depends(reusable_oauth2)
):
    validate_token(token.credentials)
    
    comment_data = {
        "comment": content,
        "post_id": post_id
    }
    
    result = comments_collection.insert_one(comment_data)
    
    if result:
        return {
            "message": "Comment created",
            "comment_id": str(result.inserted_id),
        }
    else:
        raise HTTPException(status_code=500, detail="Could not create comment")

@router.get("/get-comments/{post_id}")
async def get_comments(post_id: str, token: str = Depends(reusable_oauth2)):
    validate_token(token.credentials)
    
    comments = list(comments_collection.find({"post_id": post_id}))

    # Convert ObjectId to string for each comment
    for comment in comments:
        comment["_id"] = str(comment["_id"])

    return comments
