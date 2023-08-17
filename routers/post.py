from fastapi import APIRouter
from models.post import Post

router = APIRouter()

@router.post("/post")
async def post_image(post: Post):
    await post.insert()
    return {"message": "Post created"}

@router.post("/comment")
async def comment_on_post(post_id: str, comment: str):
    # Add logic to add a comment to a post
    pass
