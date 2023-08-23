from fastapi import APIRouter, Depends, HTTPException
from app.dependencies.database import posts_collection, comments_collection
from app.dependencies.security import reusable_oauth2, validate_token
from app.models.post import Post

router = APIRouter()

@router.post("/create-post",)
async def create_post(caption: str, token: str = Depends(reusable_oauth2)):
    validate_token(token.credentials)
    
    post_data = {
        "caption": caption,
    }
    
    result = posts_collection.insert_one(post_data)
    
    if result:
        return {
            "message": "Post created",
            "post_id": str(result.inserted_id),
        }
    else:
        raise HTTPException(status_code=500, detail="Could not create post")
@router.get("/list-posts")
async def list_posts(token: str = Depends(reusable_oauth2)):
    validate_token(token.credentials)
    
    posts = list(posts_collection.find())

    # Convert ObjectId to string for each post and fetch associated comments
    for post in posts:
        post["_id"] = str(post["_id"])
        post_comments = list(comments_collection.find({"post_id": post["_id"]}))
        # Convert ObjectId to string for each comment
        for comment in post_comments:
            comment["_id"] = str(comment["_id"])
        post["comments"] = post_comments

    return posts