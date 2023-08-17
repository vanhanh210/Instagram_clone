from fastapi import APIRouter, Depends
from ..models.user import User
from ..models.comment import Comment
from ..dependencies.security import get_current_user

router = APIRouter()

@router.post("/comment/")
async def post_comment(post_id: str, content: str, current_user: User = Depends(get_current_user)):
    comment = Comment(post_id=post_id, user_id=current_user.id, content=content)
    await comment.insert()
    return {"content": content, "user": current_user.username}
