from fastapi import APIRouter, Depends
from app.models.comment import Comment
from app.dependencies.security import get_current_user

router = APIRouter()

class CommentCreate(BaseModel):
    post_id: str
    content: str

@router.post("/comment/")
async def create_comment(comment: CommentCreate, user=Depends(get_current_user)):
    new_comment = await Comment(post_id=comment.post_id, user_id=user.id, content=comment.content).insert()
    return new_comment

@router.get("/comments/{post_id}")
async def get_all_comments(post_id: str):
    return await Comment.find(Comment.post_id == post_id).to_list()
