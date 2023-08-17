from fastapi import APIRouter
from models.user import User

router = APIRouter()

@router.post("/signup")
async def signup(user: User):
    await user.insert()
    return {"message": "User created"}

@router.post("/login")
async def login(username: str, password: str):
    # Add login logic, JWT generation, etc.
    pass
