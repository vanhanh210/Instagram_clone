from fastapi import APIRouter, Depends, File, UploadFile

from app.dependencies.security import get_current_user
from app.models.post import Post
from app.models.user import User

router = APIRouter()

@router.post("/post/")
async def post_image(image: UploadFile = File(...), current_user: User = Depends(get_current_user)):
    post = Post(user_id=current_user.id, image=image.filename)
    await post.insert()
    return {"image": image.filename, "user": current_user.username}
