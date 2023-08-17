from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from app.models.post import Post
from app.dependencies.security import get_current_user

router = APIRouter()

class PostCreate(BaseModel):
    caption: str

@router.post("/post/")
async def create_post(post: PostCreate, user=Depends(get_current_user), file: UploadFile = File(...)):
    # You'd typically save the image and get its URL. For simplicity, I'm using a placeholder URL.
    image_url = "path_to_saved_image"
    new_post = await Post(user_id=user.id, image_url=image_url, caption=post.caption).insert()
    return new_post

@router.get("/posts/")
async def get_all_posts():
    return await Post.all()
